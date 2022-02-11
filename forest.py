from data.extract_data import get_patients
from random_forest.tree import *
import pickle


def build_forest(file_path_name, tree_depth, columns_wanted):
    wants_to_include_standard_of_truth = True
    patients = get_patients(file_path_name, wants_to_include_standard_of_truth)

    data_types = get_data_types(columns_wanted)

    forest = construct_forest_by_data_types(patients, tree_depth, data_types)
    return forest


def build_forest_all_variables(file_path_name, tree_depth):
    wants_to_include_standard_of_truth = True
    patients = get_patients(file_path_name, wants_to_include_standard_of_truth)

    data_types = get_all_data_types()

    forest = construct_forest_by_data_types(patients, tree_depth, data_types)
    return forest


def get_forest_prediction(forest, patient):
    true_count = 0
    false_count = 0

    for tree in forest:
        prediction = traverse_and_get_prediction(tree, patient)
        if prediction is True:
            true_count += 1
        else:
            false_count += 1

    if true_count >= false_count:
        return True
    else:
        return False


def construct_forest_by_all_data_types(patients, tree_depth):
    forest = []
    data_types = get_all_data_types()

    for data_type in data_types:
        new_tree = construct_decision_tree_from_patients(patients, data_type, tree_depth)
        forest.append(new_tree)

    load_forest(forest, patients)

    return forest


def construct_forest_by_data_types(patients, tree_depth, data_types):
    forest = []

    for data_type in data_types:
        new_tree = construct_decision_tree_from_patients(patients, data_type, tree_depth)
        forest.append(new_tree)

    load_forest(forest, patients)

    return forest


def load_forest(forest, patients):
    # this function is meant to set the predictions on each of the leaf nodes
    for tree in forest:
        add_patients_to_tree(tree, patients)
        traverse_and_set_predictions(tree)


def load_forest_from_file(file_name):
    file = open(file_name, 'rb')
    forest = pickle.load(file)
    file.close()
    return forest


def load_forests_from_file(file_name, number_of_forests):
    file = open(file_name, 'rb')
    forests = []

    for i in range(0, number_of_forests):
        forest = pickle.load(file)
        forests.append(forest)

    file.close()

    return forests


def save_forest_to_file(file_name, forest):
    file = open(file_name, 'wb')
    pickle.dump(forest, file_name)
    file.close()


def save_forests_to_file(file_name, forests):
    for forest in forests:
        save_forest_to_file(file_name, forest)
