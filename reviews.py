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

# print(df['country'].unique())
# print(df['country'].value_counts()['US'])
country = []
country_count = []
for i in df['country'].unique():
    try:
        country.append(i)
        country_count.append(df['country'].value_counts()[i])

    except:
        # country.append("np.nan")
        country_count.append(0)

d = {
    'country': country,
    'count': country_count
}

print(d)

out_data_frame = pd.DataFrame(d)
out_data_frame.to_csv('data/reviews-per-country.csv')

# data_out_to_csv = pd.DataFrame(d, index=['country', 'count'])
# data_out_to_csv.to_csv('data/reviews-per-country.csv')

print(out_data_frame)
