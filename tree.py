from data.data_type import *
from helper_methods.true_and_false_counts import *
from helper_methods.split_point import *


def construct_decision_tree_from_patients(patients, data_type, tree_depth):
    if tree_depth == 0:
        return
    else:
        tree_depth -= 1

    sorted_patients = sort_patients_by_data_type(patients, data_type)
    data_points = get_data_points_by_data_type(patients, data_type)
    split_points = get_split_points_by_values(data_points)

    if len(split_points) == 0:
        return

    best_split_point = get_best_split_point(sorted_patients, split_points, data_type)

    child_left_patients, child_right_patients = get_nodes_from_split_point(patients, best_split_point, data_type)

    left_child = construct_decision_tree_from_patients(child_left_patients, data_type, tree_depth)
    right_child = construct_decision_tree_from_patients(child_right_patients, data_type, tree_depth)

    decision_tree = Tree(left_child, right_child, best_split_point, data_type)
    return decision_tree


def get_nodes_from_split_point(patient_list, split_point, data_type):
    left_node_patients = []
    right_node_patients = []

    for patient in patient_list:
        point = get_data_by_data_type(patient, data_type)
        if point < split_point:
            left_node_patients.append(patient)
        else:
            right_node_patients.append(patient)

    return left_node_patients, right_node_patients


def add_patients_to_tree(tree, patients):
    # this function goes through all of the "patients" provided
    # and adds them to the "tree" provided on the leaf nodes they belong to
    # using the traverse_and_add_patient() method which is located in class tree

    for patient in patients:
        traverse_and_add_patient(tree, patient)


def traverse_and_add_patient(tree, patient):
    # this function is meant to add a patient on its corresponding leaf node
    # on the tree. if the data from the patient is below the split point it goes to
    # the left node. Otherwise it goes right if the right node exists.
    # When it reaches the bottom it adds the patient and stops.

    # Note: this function is recursive

    left_node = tree.get_left()
    right_node = tree.get_right()
    data_type = tree.get_data_type()

    if left_node is None and right_node is None:
        tree.append_patient(patient)

    data = get_data_by_data_type(patient, data_type)
    split_point = tree.get_split_point()

    if data < split_point and left_node is not None:
        traverse_and_add_patient(left_node, patient)
    elif right_node is not None:
        traverse_and_add_patient(right_node, patient)
    elif left_node is not None:
        traverse_and_add_patient(left_node, patient)


def traverse_and_set_predictions(tree):
    # this function goes through every node on the tree
    # until it reaches all of the leaf nodes
    # when it does, it set's that leaf node's prediction
    # with the set_prediction method found in class tree

    left_node = tree.get_left()
    right_node = tree.get_right()

    if left_node is None and right_node is None:
        tree.set_prediction()
    elif left_node is None:
        traverse_and_set_predictions(right_node)
    elif right_node is None:
        traverse_and_set_predictions(left_node)
    else:
        traverse_and_set_predictions(left_node)
        traverse_and_set_predictions(right_node)


def traverse_and_get_prediction(tree, patient):
    left_node = tree.get_left()
    right_node = tree.get_right()
    prediction = tree.get_prediction()
    data_type = tree.get_data_type()

    if prediction is not None:
        return prediction
    elif left_node is None:
        return traverse_and_get_prediction(right_node, patient)
    elif right_node is None:
        return traverse_and_get_prediction(left_node, patient)
    else:
        split_point = tree.get_split_point()
        data = get_data_by_data_type(patient, data_type)

        if data < split_point:
            return traverse_and_get_prediction(left_node, patient)
        else:
            return traverse_and_get_prediction(right_node, patient)


def traverse_and_print_predictions(tree):
    left_node = tree.get_left()
    right_node = tree.get_right()

    if left_node is None and right_node is None:
        prediction = tree.get_prediction()
        print(prediction)
    elif left_node is None:
        traverse_and_print_predictions(right_node)
    elif right_node is None:
        traverse_and_print_predictions(left_node)
    else:
        traverse_and_print_predictions(left_node)
        traverse_and_print_predictions(right_node)


class Tree:

    def __init__(self, left=None, right=None, split_point=None, data_type=None):
        self.__left = left
        self.__right = right
        self.__patients = []
        self.__split_point = split_point
        self.__data_type = data_type
        self.__prediction = None

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right

    def set_patients(self, patients):
        self.__patients = patients

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def get_patients(self):
        return self.__patients

    def get_split_point(self):
        return self.__split_point

    def get_data_type(self):
        return self.__data_type

    def append_patient(self, patient):
        self.__patients.append(patient)

    def set_prediction(self):
        patients = self.__patients
        true_count = get_true_count(patients)
        false_count = get_false_count(patients)

        if true_count >= false_count:
            self.__prediction = True
        else:
            self.__prediction = False

    def get_prediction(self):
        return self.__prediction
