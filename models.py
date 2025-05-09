import os
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Dataset directory in same folder as script
dataset_dir = "./Train_Test_IoT_Dataset"
csv_files = [f for f in os.listdir(dataset_dir) if f.endswith(".csv")]

# Attack types to exclude
excluded_types = {"xss", "scanning"}

for file in csv_files:
    print(f"\n📂 Processing file: {file}", flush=True)
    file_path = os.path.join(dataset_dir, file)
    df = pd.read_csv(file_path)

    if "type" not in df.columns:
        print("❌ 'type' column missing. Skipping this file.", flush=True)
        continue

    # Filter out excluded types
    df = df[~df["type"].isin(excluded_types)]

    # Drop non-numeric and identifier columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    df_numeric = df[numeric_cols].copy()
    df_numeric["type"] = df["type"].values

    # Balance classes
    counts = df_numeric["type"].value_counts()
    min_samples = counts.min()

    df_balanced = (
        df_numeric.groupby("type")
        .apply(lambda x: x.sample(n=min_samples, random_state=42))
        .reset_index(drop=True)
    )

    # Encode labels
    le = LabelEncoder()
    df_balanced["type"] = le.fit_transform(df_balanced["type"])

    # Prepare X and y
    X = df_balanced.drop(columns=["type"])
    y = df_balanced["type"]

    # Normalize features
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

    # Models to evaluate
    models = {
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "SVM (Linear)": SVC(kernel="linear", probability=True, random_state=42),
        "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="mlogloss", random_state=42)
    }

    skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

    for model_name, model in models.items():
        print(f"\n{model_name} on {file}", flush=True)
        acc_scores = []
        f1_scores = []

        for fold, (train_idx, test_idx) in enumerate(skf.split(X, y), start=1):
            X_train, X_test = X[train_idx], X[test_idx]
            y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            acc = accuracy_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred, average="macro")

            acc_scores.append(acc)
            f1_scores.append(f1)

            print(f"\nFold {fold} -----------------------------", flush=True)
            print(f"Accuracy: {acc:.4f}, Macro F1 Score: {f1:.4f}", flush=True)
            print("Classification Report:", flush=True)
            print(classification_report(y_test, y_pred, target_names=le.classes_, zero_division=0), flush=True)

        print(f"\nAvg Accuracy for {model_name}: {np.mean(acc_scores):.4f}", flush=True)
        print(f"Avg Macro F1 Score for {model_name}: {np.mean(f1_scores):.4f}", flush=True)

print("\nAll evaluations complete.", flush=True)
