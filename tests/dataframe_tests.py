import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))

from dataframe import DataFrame

data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict, column_order=['John', 'Sarah', 'Pete'])
print(df1.to_array())

df2 = df1.select_columns(['Sarah', 'Pete'])

df3 = df1.select_rows([1, 3])
print(df3.to_array())

arr = [['Kevin', 'Fray', 5],
       ['Charles', 'Trapp', 17],
       ['Anna', 'Smith', 13],
       ['Sylvia', 'Mendez', 9]]

df4 = DataFrame.from_array(arr, column_order=['firstname', 'lastname', 'age'])
