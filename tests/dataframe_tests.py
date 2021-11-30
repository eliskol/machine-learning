import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))

from dataframe import DataFrame

data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict, column_order=['John', 'Sarah', 'Pete'])
assert df1.column_order == ['John', 'Sarah', 'Pete']
assert df1.to_array() == [[2, 3, 1], [1, 1, 0], [0, 4, 1], [2, 0, 0]]

df2 = df1.select_columns(['Sarah', 'Pete'])
assert df2.column_order == ['Sarah', 'Pete']
assert df2.to_array() == [[3, 1], [1, 0], [4, 1], [0, 0]]

df3 = df1.select_rows([1, 3])
assert df3.column_order == ['John', 'Sarah', 'Pete']
assert df3.to_array() == [[1, 1, 0], [2, 0, 0]]

arr = [['Kevin', 'Fray', 5],
       ['Charles', 'Trapp', 17],
       ['Anna', 'Smith', 13],
       ['Sylvia', 'Mendez', 9]]

df4 = DataFrame.from_array(arr, column_order=['firstname', 'lastname', 'age'])
# print(df4.to_array())
# print(df4.to_json())
df5 = DataFrame.from_json(df4.to_json(), ['lastname', 'firstname', 'age'])
print(df5.to_array(), '\n')

df6 = df5.order_by('lastname', ascending=False)
print(df6.to_array())