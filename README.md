# VOIS TASK

 Author : Ibrahim Nasr 


```python
# Install numpy 
!pip install --user pandas
```


```python
# Import library 
import pandas as pd
```


```python
# Load the CSV file into a DataFrame
file_name = 'Employees.csv'
df = pd.read_csv(file_name)
```


```python
# Display Employee CSV 
print(df.head(df.shape[0]))
```

            Name   Gender  Age      Salary(USD)
       0    Mark      M  20.3650         1000
       1   John       M  60.3226         1200
       2  Edward      M  42.2650         3000
       3   Salah      M  31.3800         5000
       4   Ahmed      M  42.6800         1700
       5    Sara      F  25.3640         1900
       6   Julia      F  21.2857         1950
       7   John       M  60.3226         1200
       8    Mark      M  20.3650         1000
    

```python
# Remove duplication
def remove_duplication():
    df.drop_duplicates(inplace=True)

remove_duplication()    
print(df.head(df.shape[0]))
```

          Name  Gender      Age  Salary(USD)
      0    Mark      M  20.3650         1000
      1   John       M  60.3226         1200
      2  Edward      M  42.2650         3000
      3   Salah      M  31.3800         5000
      4   Ahmed      M  42.6800         1700
      5    Sara      F  25.3640         1900
      6   Julia      F  21.2857         1950
    


```python
# remove decimal 
def remove_decimal(col_name):
    df[col_name] = df[col_name].astype(int)
    
remove_decimal('Age')
print(df.head(df.shape[0]))        
```

          Name  Gender  Age  Salary(USD)
      0    Mark      M   20         1000
      1   John       M   60         1200
      2  Edward      M   42         3000
      3   Salah      M   31         5000
      4   Ahmed      M   42         1700
      5    Sara      F   25         1900
      6   Julia      F   21         1950
    


```python
def convert_usd_egp(usd_rate_egp,col_name):
    df['Salary(EGP)'] = df[col_name] * usd_rate_egp
    
convert_usd_egp(30.8991,'Salary(USD)')    
print(df.head(df.shape[0]))        
```

        Name  Gender  Age  Salary(USD)  Salary(EGP)
    0    Mark      M   20         1000    30899.100
    1   John       M   60         1200    37078.920
    2  Edward      M   42         3000    92697.300
    3   Salah      M   31         5000   154495.500
    4   Ahmed      M   42         1700    52528.470
    5    Sara      F   25         1900    58708.290
    6   Julia      F   21         1950    60253.245
    


```python
# Calcualte average ages 
def calculate_average_age(col_name):
    return df[col_name].mean()

print(calculate_average_age('Age'))
```

    34.42857142857143
    


```python
# Calcualte median
def calculate_median_salaries(col_name):
    return df[col_name].median()

print(calculate_median_salaries('Salary(USD)')) # median -> USD
print(calculate_median_salaries('Salary(EGP)')) # median -> egypt  
```

    1900.0
    58708.29
    


```python
# Calculate ratio 
def calculate_ratio_gender(col_name):
    return df[col_name].value_counts() / df.shape[0]

print(calculate_ratio_gender('Gender'))
```

    M    0.714286
    F    0.285714
    Name: Gender, dtype: int64
    


```python
def create_new_employee_file(new_file_name):
    df.to_csv(new_file_name,index=False)
    
create_new_employee_file('EmployeeNew.csv')

new_file_name = 'EmployeeNew.csv'
df_new = pd.read_csv(new_file_name)
df_new = df_new.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
print(df_new.head(df_new.shape[0]))
```

        Name  Gender  Age  Salary(USD)  Salary(EGP)
    0    Mark      M   20         1000    30899.100
    1   John       M   60         1200    37078.920
    2  Edward      M   42         3000    92697.300
    3   Salah      M   31         5000   154495.500
    4   Ahmed      M   42         1700    52528.470
    5    Sara      F   25         1900    58708.290
    6   Julia      F   21         1950    60253.245
