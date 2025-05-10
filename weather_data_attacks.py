import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.decomposition import PCA
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score, f1_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import os


print("Evaluating the Decision Tree, SVM (RBF), and XGBoost on Weather dataset", flush=True)
os.makedirs("results", exist_ok=True) #the resulting roc curves and confusion matricies will be in this directory

#Loading and cleaning. Removing xss and scanning due to low amounts of those attacks
df = pd.read_csv("Train_Test_IoT_Weather.csv")
df = df[~df["type"].isin(["xss", "scanning"])]
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
df_numeric = df[numeric_cols].copy()
df_numeric["type"] = df["type"].values

#Balancing different types of attacks
min_samples = df_numeric["type"].value_counts().min()
df_balanced = df_numeric.groupby("type").apply(
    lambda x: x.sample(n=min_samples, random_state=42)
).reset_index(drop=True)

#Encode
le = LabelEncoder()
df_balanced["type"] = le.fit_transform(df_balanced["type"])
X = df_balanced.drop(columns=["type"])
y = df_balanced["type"]

# Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_selected = SelectKBest(mutual_info_classif, k='all').fit_transform(X_scaled, y)
X_pca = PCA(n_components=0.95).fit_transform(X_selected)

#Stratified CV
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# SVM parameter tuning
svm_param_grid = {
    "C": [0.1, 1, 10,100,1000, 5000, 10000],
    "gamma": [0.0001, 0.001, 0.01, 0.1, "scale", "auto"],
    "kernel": ["rbf"]
}
print("🔧 Tuning SVM...", flush=True)
svm_grid = GridSearchCV(SVC(), svm_param_grid, scoring="f1_macro", cv=skf, n_jobs=-1)
svm_grid.fit(X_pca, y)

best_svm = svm_grid.best_estimator_
print(f"Best SVM params: {svm_grid.best_params_}", flush=True)

# 3 different models
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "SVM (RBF Tuned)": best_svm,
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="mlogloss", random_state=42)
}

#Evaluation of models
def evaluate_model(name, model):
    acc_scores, f1_scores = [], []

    for fold, (train_idx, test_idx) in enumerate(skf.split(X_pca, y), start=1):
        X_train, X_test = X_pca[train_idx], X_pca[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred) #accuracy score
        f1 = f1_score(y_test, y_pred, average="macro") #f1 score

        acc_scores.append(acc)
        f1_scores.append(f1)

        print(f"\nFold {fold} – {name}", flush=True)
        print(f"Accuracy: {acc:.4f} | Macro F1: {f1:.4f}", flush=True)
        print("Classification Report:\n", classification_report(
            y_test, y_pred, target_names=le.classes_, zero_division=0
        ), flush=True)

        if fold == 1:
            ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
            plt.title(f"{name} – Confusion Matrix (Fold 1)")
            plt.savefig(f"results/conf_matrix_{name.replace(' ', '_')}.png")
            plt.close()

    print(f"\n{name} – Avg Accuracy: {np.mean(acc_scores):.4f}", flush=True)
    print(f"{name} – Avg Macro F1 Score: {np.mean(f1_scores):.4f}", flush=True)

#Run all models
for model_name, model in models.items():
    evaluate_model(model_name, model)

print("\nFinal evaluation complete. Results saved in ./results", flush=True)
