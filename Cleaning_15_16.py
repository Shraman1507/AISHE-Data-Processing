import pandas as pd


df = pd.read_excel(r'C:\Users\DELL\Flutter\Factly_assignment\Users\DELL\Flutter\Factly_assignment\AISHE2015-16.xlsx', sheet_name='6TotalEnr', header=1)
df_2 = pd.read_excel(r'C:\Users\DELL\Flutter\Factly_assignment\Users\DELL\Flutter\Factly_assignment\AISHE2015-16.xlsx', sheet_name='6TotalEnr', header=2)


data_2 = df_2.columns


df = df.drop(df.index[0])


data = df.columns
temp = '0'
new_column = []


for x in data:
    x = x.lower()             
    x = x.replace(" ", "_")   
    x = x.replace("-", "_")    
    
    if 'unnamed' not in x:
        temp = x
        new_column.append(x)
    if 'unnamed' in x:
        x = temp
        new_column.append(x)

new_column_2 = []


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


column_fin = []
for x in range(0, len(new_column)):
    column_fin.append(str(new_column[x]) + "_" + str(new_column_2[x]))


mydic = dict(zip(data, column_fin))


df.rename(columns=mydic, inplace=True)


df = df.drop([1])
df = df.drop([38])


new_df = pd.melt(df, id_vars=column_fin[1], value_vars=column_fin[1:29], value_name='number_of_enrollments', var_name='level')


add_data = {'unit': 'number_of_enrollments_in_absolute_number', 'note': " "}
new_df = new_df.assign(**add_data)


new_df.fillna( 'np.nan', inplace=True)


new_df.to_excel('AISHE2015_16_processed.xlsx', index=False)

# Print the resulting DataFrame
print(new_df)
