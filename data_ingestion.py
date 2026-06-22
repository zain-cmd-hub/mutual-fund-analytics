import pandas as pd
import os

folder_path = "data/raw"

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)

        print("\n" + "="*50)
        print("File:", file)

        df = pd.read_csv(file_path)

        print("Shape:", df.shape)
        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())