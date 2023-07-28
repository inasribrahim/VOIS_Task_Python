# Import library 
import pandas as pd



# Load the CSV file into a DataFrame
file_name = 'Employees.csv'
df = pd.read_csv(file_name)




# Display Employee CSV 
print(df.head(df.shape[0]))



# Remove duplication
def remove_duplication():
    df.drop_duplicates(inplace=True)

remove_duplication()    
print(df.head(df.shape[0]))




# remove decimal 
def remove_decimal(col_name):
    df[col_name] = df[col_name].astype(int)
    
remove_decimal('Age')
print(df.head(df.shape[0]))        




def convert_usd_egp(usd_rate_egp,col_name):
    df['Salary(EGP)'] = df[col_name] * usd_rate_egp
    
convert_usd_egp(30.8991,'Salary(USD)')    
print(df.head(df.shape[0]))        




# Calcualte average ages 
def calculate_average_age(col_name):
    return df[col_name].mean()

print(calculate_average_age('Age'))




# Calcualte median
def calculate_median_salaries(col_name):
    return df[col_name].median()

print(calculate_median_salaries('Salary(USD)')) # median -> USD
print(calculate_median_salaries('Salary(EGP)')) # median -> egypt  



# Calculate ratio 
def calculate_ratio_gender(col_name):
    return df[col_name].value_counts()

print(calculate_ratio_gender('Gender'))




def create_new_employee_file(new_file_name):
    df.to_csv(new_file_name,index=False)
    
create_new_employee_file('EmployeeNew.csv')

new_file_name = 'EmployeeNew.csv'
df_new = pd.read_csv(new_file_name)
df_new = df_new.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
print(df_new.head(df_new.shape[0]))
