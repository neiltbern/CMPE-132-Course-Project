
#!/bin/bash

# Output file
output="IoT_Botnet_5pc.csv"

# Remove output file if it already exists
rm -f "$output"

# Add header from the first file
head -n 1 UNSW_2018_IoT_Botnet_Full5pc_1.csv > "$output"

# Append content (excluding headers) from all files
for file in UNSW_2018_IoT_Botnet_Full5pc_*.csv; do
    tail -n +2 "$file" >> "$output"
done

echo "Combined CSV saved as $output"