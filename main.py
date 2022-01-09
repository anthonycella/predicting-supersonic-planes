from sklearn.naive_bayes import BernoulliNB

import machine
from airplane import Airplane
import numpy as np


def is_match(prediction, actual_result):
    if prediction == actual_result:
        return True
    else:
        return False


def fill_array(empty_array):
    new_array = empty_array
    for current_index in range(0, len(empty_array)):
        if current_index % 4 == 0:
            is_supersonic = True
        else:
            is_supersonic = False

        new_array[current_index] = Airplane(is_supersonic, current_index)

    return new_array


def get_speed_array(airplane_array):
    speed_array = []

    for airplane in airplane_array:
        speed = airplane.get_air_speed_in_knots()
        speed_array.append(speed)

    return speed_array


def get_is_supersonic_array(airplane_array):
    is_supersonic_array = []

    for airplane in airplane_array:
        is_supersonic = airplane.is_supersonic_aircraft()
        is_supersonic_array.append(is_supersonic)

    return is_supersonic_array


def get_id_array(airplane_array):
    airplane_id_array = []

    for airplane in airplane_array:
        airplane_id = airplane.get_aircraft_id()
        airplane_id_array.append(airplane_id)

    return airplane_id_array


def print_out_array_to_console(airplane_array):
    for airplane in airplane_array:
        print(airplane)


def print_accuracy_to_console(accuracy_number):
    accuracy_percent = format(accuracy_number, '%.2f')
    print("Accuracy: " + accuracy_percent)


def main():
    size = 1000000
    empty_array = [None] * size

    filled_array = fill_array(empty_array)
    # print_out_array_to_console(filled_array)

    speed_array = get_speed_array(filled_array)
    is_supersonic_array = get_is_supersonic_array(filled_array)
    airplane_id_array = get_id_array(filled_array)

    simple_machine = BernoulliNB()

    X = np.array([airplane_id_array, speed_array])
    X = X.reshape(size, 2)
    Y = np.array(is_supersonic_array)

    simple_machine.fit(X, Y)
    predictions = simple_machine.predict(X[2:200])
    actual_results = Y[2:200]

    true_predictions = machine.count_true_predictions(predictions)
    print(str(true_predictions))

    print(simple_machine.score(X, Y))


main()

