import pandas as pd

# Load the Excel file and select the sheet '6TotalEnr', using the first and second rows as headers for different DataFrames
df = pd.read_excel(r'C:\Users\DELL\Flutter\Factly_assignment\Users\DELL\Flutter\Factly_assignment\AISHE2015-16.xlsx', sheet_name='6TotalEnr', header=1)
df_2 = pd.read_excel(r'C:\Users\DELL\Flutter\Factly_assignment\Users\DELL\Flutter\Factly_assignment\AISHE2015-16.xlsx', sheet_name='6TotalEnr', header=2)

# Store the columns from the second DataFrame
data_2 = df_2.columns

# Drop the first row from the initial DataFrame (likely a header or unnecessary row)
df = df.drop(df.index[0])

# Store the columns from the initial DataFrame
data = df.columns
temp = '0'
new_column = []

# Standardize column names and handle unnamed columns
for x in data:
    x = x.lower()              # Convert to lowercase
    x = x.replace(" ", "_")    # Replace spaces with underscores
    x = x.replace("-", "_")    # Replace hyphens with underscores
    
    if 'unnamed' not in x:
        temp = x
        new_column.append(x)
    if 'unnamed' in x:
        x = temp
        new_column.append(x)

new_column_2 = []

# Standardize second set of column names
for x in data_2:
    x = x.lower()
    x = x.replace(" ", "_")
    x = x.replace("-", "_")
    if 'unnamed' in x:
        x = " "
        new_column_2.append(x)
    elif 'female' in x:
        x = 'female'
        new_column_2.append(x)
        continue
    elif 'male' in x:
        x = 'male'
        new_column_2.append(x)
    elif 'total' in x:
        x = 'total'
        new_column_2.append(x)

# Combine standardized column names
column_fin = []
for x in range(0, len(new_column)):
    column_fin.append(str(new_column[x]) + "_" + str(new_column_2[x]))

# Create a dictionary to rename the columns in the DataFrame
mydic = dict(zip(data, column_fin))

# Rename the columns in the DataFrame
df.rename(columns=mydic, inplace=True)

# Drop specific rows (these indices might be different in your dataset)
df = df.drop([1])
df = df.drop([38])

# Reshape the DataFrame using pd.melt
new_df = pd.melt(df, id_vars=column_fin[1], value_vars=column_fin[1:29], value_name='number_of_enrollments', var_name='level')

# Add additional columns to the DataFrame
add_data = {'unit': 'number_of_enrollments_in_absolute_number', 'note': " "}
new_df = new_df.assign(**add_data)

# Replace empty cells with np.nan
new_df.fillna( 'np.nan', inplace=True)

# Save the processed DataFrame to an Excel file
new_df.to_excel('AISHE2015_16_processed.xlsx', index=False)

# Print the resulting DataFrame
print(new_df)
