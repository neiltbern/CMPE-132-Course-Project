import pandas as pd

print("Im here!\n", flush=True)
# Load the dataset
df = pd.read_csv("Datasets/IoT_Botnet_5pc.csv")  # assuming it's tab-separated

# Get unique values in the 'category' column
#unique_categories = df['category'].unique()

# Print the unique categories
#print("Unique categories in the dataset:", flush=True)
#for category in unique_categories:
#    print(category, flush=True)

# Count the number of instances for each unique category
category_counts = df['category'].value_counts()

# Print the counts
print("Number of instances per category:", flush=True)
print(category_counts, flush=True)
