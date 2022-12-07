import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))

from random_forest import RandomForest


data = [['Shortbread', 0.15, 0.2],
        ['Shortbread', 0.15, 0.3],
        ['Shortbread', 0.2, 0.25],
        ['Shortbread', 0.25, 0.4],
        ['Shortbread', 0.3, 0.35],
        ['Sugar', 0.05, 0.25],
        ['Sugar', 0.05, 0.35],
        ['Sugar', 0.1, 0.3],
        ['Sugar', 0.15, 0.4],
        ['Sugar', 0.25, 0.35]]

forest_size_dict = {}

forest_sizes_to_test = [1, 5, 10, 50, 100, 500, 1000]
for forest_size in forest_sizes_to_test:
    print(forest_size)
    forest_size_dict[forest_size] = 0
    for datapoint_to_test in data:
        working_data = [datapoint for datapoint in data if datapoint != datapoint_to_test]
        working_forest = RandomForest()
        working_forest.fit(forest_size, working_data)

        if working_forest.predict(datapoint_to_test[1:]) == datapoint_to_test[0]:
            forest_size_dict[forest_size] += 1
    forest_size_dict[forest_size] = forest_size_dict[forest_size] / len(data)

print(forest_size_dict)