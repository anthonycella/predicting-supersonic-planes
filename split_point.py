#
# Author: Anthony Cella
# a file containing all of the functions related to split points.
# a split point is a point at which the computer, whether less than or greater than,
# can possibly determine whether or not a patient has parkinson's or not.
# Last updated: 1/29/22
#

def get_split_points_by_values(numbered_values):

    # This is here to get all of the possible decision points
    # of the variable being analyzed the machine can
    # choose between "True" and "False" on whether it predicts the patient
    # has parkinson's or not.

    split_points = []

    for current_index in range(0, len(numbered_values) - 1):
        next_index = current_index + 1

        current_point = numbered_values[current_index]
        next_point = numbered_values[next_index]

        split_point_unrounded = (current_point + next_point) / 2
        split_point = round(split_point_unrounded, 5)
        split_points.append(split_point)

    return split_points


def get_best_split_point(patients, split_points, data_type):

    # This is here to decide the best decision point that most
    # accurately predicts whether or not the patient has parkinson's.
    # This is determined by the split point with the lowest "Gini Impurity".
    # Details on this can be found in gini_impurity.py

    from helper_methods.gini_impurity import get_gini_impurity_dictionary_by_split_points
    gini_impurity_dictionary = get_gini_impurity_dictionary_by_split_points(patients, split_points, data_type)
    gini_impurities = gini_impurity_dictionary.keys()

    best_gini_impurity = min(gini_impurities)
    best_split_point = gini_impurity_dictionary[best_gini_impurity]

    return best_split_point
