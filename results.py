#
# Author: Anthony Cella
# a file containing functions that determine
# approximately how accurate a tree or forest is.
# Last updated: 1/29/22
#

from random_forest.forest import get_forest_prediction
from random_forest.tree import traverse_and_get_prediction


def get_tree_accuracy(tree, patients):

    # This is here to determine how accurate a particular
    # decision tree is in whether or not a patient actually
    # has parkinson's.

    number_of_correct_predictions = 0
    number_of_results = len(patients)

    for patient in patients:
        prediction = traverse_and_get_prediction(tree, patient)
        result = patient.has_parkinsons()

        if prediction == result:
            number_of_correct_predictions += 1

    tree_accuracy = number_of_correct_predictions / number_of_results
    return tree_accuracy


def get_forest_accuracy(forest, patients):

    # This is here to determine how accurate a whole forest
    # is in whether or not a patient actually has parkinson's.
    # This takes one prediction from the forest rather than
    # every prediction of the individual trees.

    number_of_correct_predictions = 0
    number_of_results = len(patients)

    for patient in patients:
        prediction = get_forest_prediction(forest, patient)
        result = patient.has_parkinsons()

        if prediction == result:
            number_of_correct_predictions += 1

    forest_accuracy = number_of_correct_predictions / number_of_results
    return forest_accuracy
