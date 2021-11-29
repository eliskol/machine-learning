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
print(df2.to_array())

df3 = df1.select_rows([1, 3])
print(df3.to_array())
