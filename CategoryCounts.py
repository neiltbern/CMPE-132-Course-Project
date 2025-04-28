import pandas as pd

# Define your column names
columns = [
    'pkSeqID', 'stime', 'flgs', 'proto', 'saddr', 'sport', 'daddr', 'dport',
    'pkts', 'bytes', 'state', 'ltime', 'seq', 'dur', 'mean', 'stddev', 'smac',
    'dmac', 'sum', 'min', 'max', 'soui', 'doui', 'sco', 'dco', 'spkts', 'dpkts',
    'sbytes', 'dbytes', 'rate', 'srate', 'drate', 'attack', 'category', 'subcategory'
]

chunk_size = 50000   # adjust this to smaller/larger if needed

total_counts = {}

chunks = pd.read_csv(
    "Datasets/IoT_Botnet_Full.csv",
    sep=',',
    header=None,
    names=columns,
    dtype={'sport': str, 'dport': str},
    chunksize=chunk_size,
    low_memory=False
)

for i, chunk in enumerate(chunks):
    print(f"Processing chunk {i}")
    # Count categories in this chunk
    counts = chunk['category'].value_counts()
    # Accumulate counts
    for category, count in counts.items():
        if category in total_counts:
            total_counts[category] += count
        else:
            total_counts[category] = count

# Now print the final counts
print("\n=== Final Category Counts ===")
for category, count in total_counts.items():
    print(f"{category}: {count}")

'''
=== Final Category Counts ===
DoS: 33005194
Normal: 9543
Reconnaissance: 1821639
Theft: 1587
DDoS: 38532480
'''