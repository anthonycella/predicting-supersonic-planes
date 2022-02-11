#
# Author: Anthony Cella
# A class for patient objects that have an id, age, a number of custom variables, and/or a standard of truth
# Last updated 1/29/22
#

def patient_has_parkinsons_by(standard_of_truth):
    # Converts the standard of truth input notation to boolean form for the computer to better understand
    # Not to be confused with has_parkinsons(self) which is a getter for the patient's has_parkinsons attribute
    if standard_of_truth == 1:
        return True
    else:
        return False


class Patient:

    # the * enables different number arguments to be input. This is used in case the user does not want to input
    # standard of truth as an argument
    def __init__(self, *arguments):
        self.__patient_id = arguments[0]
        self.__age = arguments[1]
        self.__variable_one = arguments[2]
        self.__variable_two = arguments[3]
        self.__variable_three = arguments[4]
        self.__variable_four = arguments[5]
        self.__variable_five = arguments[6]
        self.__variable_six = arguments[7]
        self.__variable_seven = arguments[8]
        self.__variable_eight = arguments[9]
        self.__variable_nine = arguments[10]

        if len(arguments) == 12:
            standard_of_truth = arguments[11]
            self.__has_parkinsons = patient_has_parkinsons_by(standard_of_truth)

        else:
            self.__has_parkinsons = None

    def set_has_parkinsons(self, true_or_false):
        self.__has_parkinsons = true_or_false

    def get_variable_one(self):
        return self.__variable_one

    def get_variable_two(self):
        return self.__variable_two

    def get_variable_three(self):
        return self.__variable_three

    def get_variable_four(self):
        return self.__variable_four

    def get_variable_five(self):
        return self.__variable_five

    def get_variable_six(self):
        return self.__variable_six

    def get_variable_seven(self):
        return self.__variable_seven

    def get_variable_eight(self):
        return self.__variable_eight

    def get_variable_nine(self):
        return self.__variable_nine

    def get_patient_id(self):
        return self.__patient_id

    def has_parkinsons(self):
        return self.__has_parkinsons

    def __str__(self):
        return "Patient Name: " + self.__patient_id + '\n' + "Age: " + str(self.__age) + '\n' \
            "Has Parkinson's: " + str(self.__has_parkinsons) + '\n' + "Variable One: " \
               + str(self.__variable_one) + '\n' + "Variable Two: " \
               + str(self.__variable_two) + '\n' + "Variable Three: " + str(self.__variable_three) \
               + '\n' + "Variable Four: " + str(self.__variable_four) + '\n' \
               + "Variable Five: " + str(self.__variable_five) + '\n' \
               + "Variable Six: " + str(self.__variable_six) + '\n' \
               + "Variable Seven: " + str(self.__variable_seven) + '\n' + "Variable Eight: " + str(self.__variable_eight) \
               + '\n' + "Variable Nine: " + str(self.__variable_nine)
