import pandas as pd

# Load the Excel file and select the sheet '1UniNo', starting from the second row as the header
df = pd.read_excel(r'C:\Users\DELL\Flutter\Factly_assignment\Users\DELL\Flutter\Factly_assignment\AISHE2014-15.xlsx', sheet_name='1UniNo', header=1)

# Drop the first row and the 34th row (indexing starts from 0)
df = df.drop(df.index[0])  # Drop the first row
df = df.drop(df.index[33]) # Drop the 34th row (index 33)

# Get the column names from the DataFrame
data = df.columns

# Initialize an empty list to store new column names
new_data = []

# Iterate through each column name to standardize it
for x in data:
    if type(x) == str:
        x = x.lower()           # Convert to lowercase
        x = x.replace(" ", "_") # Replace spaces with underscores
        x = x.replace("-", "_") # Replace hyphens with underscores
        new_data.append(x)      # Append the standardized name to the new_data list

# Create a dictionary mapping old column names to new column names
mydic = dict(zip(data, new_data))

# Rename the columns in the DataFrame using the dictionary
df.rename(columns=mydic, inplace=True)

# Reshape the DataFrame using pd.melt
# id_vars: Column to keep fixed
# value_vars: Columns to unpivot (columns to be melted)
# value_name: Name of the resulting variable column
# var_name: Name of the resulting value column
new_df = pd.melt(df, id_vars=new_data[0], value_vars=new_data[1:14], value_name='type_of_university', var_name='number_of_universities')

# Add additional columns to the DataFrame
add_data = {'unit': 'number_of_universities in Absolute Number', 'note': " "}
new_df = new_df.assign(**add_data)

# Replace empty cells with np.nan
new_df.fillna('np.nan', inplace=True)

# Save the processed DataFrame to an Excel file
new_df.to_excel('AISHE2014_15_processed.xlsx', index=False)

# Print the resulting DataFrame
print(new_df)
