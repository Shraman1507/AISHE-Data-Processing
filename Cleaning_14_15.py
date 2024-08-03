import pandas as pd


df = pd.read_excel(r'C:\Users\DELL\Flutter\Factly_assignment\Users\DELL\Flutter\Factly_assignment\AISHE2014-15.xlsx', sheet_name='1UniNo', header=1)


df = df.drop(df.index[0])  # Drop the first row
df = df.drop(df.index[33]) # Drop the 34th row (index 33)


data = df.columns


new_data = []


for x in data:
    if type(x) == str:
        x = x.lower()           # Convert to lowercase
        x = x.replace(" ", "_") # Replace spaces with underscores
        x = x.replace("-", "_") # Replace hyphens with underscores
        new_data.append(x)      # Append the standardized name to the new_data list


mydic = dict(zip(data, new_data))


df.rename(columns=mydic, inplace=True)


new_df = pd.melt(df, id_vars=new_data[0], value_vars=new_data[1:14], value_name='type_of_university', var_name='number_of_universities')


add_data = {'unit': 'number_of_universities in Absolute Number', 'note': " "}
new_df = new_df.assign(**add_data)


new_df.fillna('np.nan', inplace=True)


new_df.to_excel('AISHE2014_15_processed.xlsx', index=False)

# Print the resulting DataFrame
print(new_df)
