#!/bin/bash
#SBATCH --job-name=weather_attacks
#SBATCH --output=output.txt
#SBATCH --error=error.txt
#SBATCH --time=02:00:00
#SBATCH --partition=condo
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=32G

module load python3/3.8.8

python weather.py

echo "weather job completed successfully!"
