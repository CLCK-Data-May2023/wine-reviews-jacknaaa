# add your code here
import pandas as pd
import zipfile

# Specify the path to your .zip file
zip_file_path = "data/winemag-data-130k-v2.csv.zip"

# Extract the contents of the .zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    csv_file_name = zip_ref.namelist()[0]
    with zip_ref.open(csv_file_name) as csv_file:
        df = pd.read_csv(csv_file)

print(df.head())
