import sys

sys.path.insert(1, sys.path[0].replace("tests", "src"))

from decision_tree import DecisionTree

data = [
    ["Shortbread", 0.15, 0.2],
    ["Shortbread", 0.15, 0.3],
    ["Shortbread", 0.2, 0.25],
    ["Shortbread", 0.25, 0.4],
    ["Shortbread", 0.3, 0.35],
    ["Sugar", 0.05, 0.25],
    ["Sugar", 0.05, 0.35],
    ["Sugar", 0.1, 0.3],
    ["Sugar", 0.15, 0.4],
    ["Sugar", 0.25, 0.35],
]

# maximum depth testing
max_depth_dict = {}
for max_depth in range(1, len(data) + 1):
    max_depth_dict[max_depth] = 0
    for datapoint_to_test in data:
        working_data = [
            datapoint for datapoint in data if datapoint != datapoint_to_test
        ]
        working_tree = DecisionTree()
        working_tree.fit(working_data, max_depth)
        if working_tree.predict(datapoint_to_test[1:]) == datapoint_to_test[0]:
            max_depth_dict[max_depth] += 1
    max_depth_dict[max_depth] = max_depth_dict[max_depth] / (len(data))
print(max_depth_dict)

# minimum split size testing
min_split_dict = {}
for min_split_size in range(1, len(data) + 2):
    min_split_dict[min_split_size] = 0
    for datapoint_to_test in data:
        working_data = [
            datapoint for datapoint in data if datapoint != datapoint_to_test
        ]
        working_tree = DecisionTree()
        working_tree.fit(working_data, None, min_split_size)
        if working_tree.predict(datapoint_to_test[1:]) == datapoint_to_test[0]:
            min_split_dict[min_split_size] += 1
    min_split_dict[min_split_size] = min_split_dict[min_split_size] / (len(data))
print(min_split_dict)
