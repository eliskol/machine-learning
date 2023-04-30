from decision_tree import DecisionTree
import random


class RandomForest:
    def fit(
        self,
        num_trees,
        datapoints,
        maximum_depth_constraint=None,
        minimum_split_size=None,
    ):
        self.trees = []
        for i in range(num_trees):
            random_subset_of_data = random.choices(datapoints, k=num_trees)
            current_tree = DecisionTree()
            current_tree.fit(
                random_subset_of_data, maximum_depth_constraint, minimum_split_size
            )
            self.trees.append(current_tree)

    def predict(self, datapoint):
        class_dict = {}
        for tree in self.trees:
            predicted_class_of_datapoint = tree.predict(datapoint)
            if predicted_class_of_datapoint in class_dict:
                class_dict[predicted_class_of_datapoint] += 1
            else:
                class_dict[predicted_class_of_datapoint] = 1
        return max(class_dict, key=class_dict.get)
