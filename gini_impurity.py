#
# Author: Anthony Cella
# a file containing all of the functions associated with
# gini impurity. Gini Impurity is the amount of error that occurs
# when a certain split point is used as the decision point for
# a prediction. The lower gini impurity the better. For more information
# on what a split point is, see slit_point.py
# Last updated: 1/29/22
#

from random_forest.probability import *
from random_forest.tree import get_nodes_from_split_point


def get_total_gini_impurity(left_list, right_list):

    # This function is used to determine how good a split point is
    # in being the decision point on the prediction of the tree.
    # The gini impurity is the quantity representing the amount of error
    # that occurs when a certain split point is used as a decision point.
    # The lower gini impurity the better. The total is determined by adding
    # up the gini impurities of the left and right nodes.

    left_gini_impurity = get_gini_impurity(left_list)
    right_gini_impurity = get_gini_impurity(right_list)

    total_gini_impurity = left_gini_impurity + right_gini_impurity
    return total_gini_impurity


def get_gini_impurity_dictionary_by_split_points(patients, split_points, data_type):

    # This function is used to be able to choose the best split point.
    # It returns a dictionary of gini_impurity : split_point key/value pairs.
    # This makes is so the computer can find the lowest gini impurity in the keys
    # and choose the split point accordingly.

    gini_impurity_dictionary = {}
    for split_point in split_points:
        value = split_point

        left_patients, right_patients = get_nodes_from_split_point(patients, split_point, data_type)

        left_gini_impurity_value = get_gini_impurity(left_patients)
        right_gini_impurity_value = get_gini_impurity(right_patients)

        left_gini_impurity_weight = len(left_patients) / len(patients)
        right_gini_impurity_weight = len(right_patients) / len(patients)

        left_gini_impurity = left_gini_impurity_value * left_gini_impurity_weight
        right_gini_impurity = right_gini_impurity_value * right_gini_impurity_weight

        gini_impurity = left_gini_impurity + right_gini_impurity
        key = gini_impurity

        gini_impurity_dictionary[key] = value

    return gini_impurity_dictionary


def get_gini_impurity(patient_list):

    # This function is used to determine how good a split point is
    # in being the decision point on the prediction of the tree.
    # The gini impurity is the quantity representing the amount of error
    # that occurs when a certain split point is used as a decision point.
    # The lower gini impurity the better.

    probability_class_zero = get_probability_class_zero(patient_list)
    probability_class_one = get_probability_class_one(patient_list)

    probability_class_zero_squared = probability_class_zero ** 2
    probability_class_one_squared = probability_class_one ** 2

    gini_impurity = 1 - (probability_class_one_squared + probability_class_zero_squared)
    return gini_impurity
