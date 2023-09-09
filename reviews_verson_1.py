# add your code here
import pandas as pd
# import numpy as np
import zipfile

# Specify the path to your .zip file
zip_file_path = "data/winemag-data-130k-v2.csv.zip"

# Extract the contents of the .zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    csv_file_name = zip_ref.namelist()[0]
    with zip_ref.open(csv_file_name) as csv_file:
        df = pd.read_csv(csv_file)

sum_by_column_key = df.groupby('country')['points'].sum()

country = []
country_count = []
country_ave = []

for i in df['country'].unique():
    try:
        country.append(i)
        country_count.append(df['country'].value_counts()[i])
        country_ave.append(
            sum_by_column_key[i] / df['country'].value_counts()[i])
    except:
        # country.append("np.nan")
        country_count.append(0)
        country_ave.append(0)

d = {
    'country': country,
    'count': country_count,
    'points': country_ave
}

out_data_frame = pd.DataFrame(d)
out_data_frame['points'] = out_data_frame['points'].round(1)

print(out_data_frame)
out_data_frame.to_csv('data_version_1/reviews-per-country.csv', index=False)

print("reviews-per-country.csv has been created")
