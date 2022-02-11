from helper_methods.true_and_false_counts import *


def get_probability_class_zero(patient_list):
    number_of_patients = len(patient_list)

    if number_of_patients == 0:
        return 0

    false_count = get_false_count(patient_list)

    probability_class_zero = false_count / number_of_patients
    return probability_class_zero


def get_probability_class_one(patient_list):
    number_of_patients = len(patient_list)

    if number_of_patients == 0:
        return 0

    true_count = get_true_count(patient_list)

    probability_class_one = true_count / number_of_patients
    return probability_class_one
