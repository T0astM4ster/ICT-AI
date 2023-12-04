import pandas as pd

# Read the source CSV file
source_file = pd.read_csv('test.csv')

# Choose the column you want to copy
column_to_copy = source_file['House_Price'].copy()  # Copy the column to avoid modifying the original DataFrame

# Reset the index to avoid duplicate labels
column_to_copy = column_to_copy.reset_index(drop=True)

# Read the destination CSV file
destination_file = pd.read_csv('out.csv')

# Insert the column into the destination CSV file
destination_file['New'] = column_to_copy

# Write the updated data to a new CSV file
destination_file.to_csv('new.csv', index=False)