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

country_counts = df['country'].value_counts()
# print(country_counts)
points = df.groupby('country').points.mean().round(1)
# print(points)
answer = pd.merge(country_counts, points, on='country')
# print(answer)

answer.to_csv('data/reviews-per-country.csv')
