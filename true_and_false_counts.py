#
# Anthony Cella
# A class containing two functions (get_false_count and get_true_count)
# which are meant to count the number of false/true results on whether or not
# each patient in the patient list has parkinson's
# Last updated 1/23/22
#

def get_false_count(patient_list):
    # this function is meant to count the number of
    # patients that resulted in 'False' for parkinson's
    false_count = 0

    for patient in patient_list:
        patient_has_parkinsons = patient.has_parkinsons()

        if not patient_has_parkinsons:
            false_count += 1

    return false_count


def get_true_count(patient_list):
    # this function is meant to count the number of
    # patients that resulted in 'True' for parkinson's
    true_count = 0

    for patient in patient_list:
        patient_has_parkinsons = patient.has_parkinsons()

        if patient_has_parkinsons:
            true_count += 1

    return true_count









