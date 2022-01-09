import pickle

import machine
import results
from airplane_helpers import *
from airplane import Airplane


def save_bernoulli_nb(bernoulli_nb):
    bernoulli_nb_file = open('bernoulli_nb.dat', 'wb')
    pickle.dump(bernoulli_nb, bernoulli_nb_file)


def load_bernoulli_nb_from_file(file_name):
    bernoulli_nb = "Can't think of what to put here as a placeholder"
    try:
        bernoulli_nb_file = open('bernoulli_nb.dat', 'rb')
        bernoulli_nb = pickle.load(bernoulli_nb_file)
    except():
        print("Error: file not found")

    return bernoulli_nb


def main():
    size_of_array = 100000
    supersonic_rate = 9
    number_of_tests = 100

    airplane_array = generate_airplane_array(size_of_array, supersonic_rate)
    threshold = 0.45
    bernoulli_nb = load_bernoulli_nb_from_file('bernoulli_nb.dat')
    # bernoulli_nb = machine.generate_bernoulli_nb(airplane_array, threshold)

    average_accuracy = results.get_average_accuracy(number_of_tests, bernoulli_nb, size_of_array, supersonic_rate)
    accuracy_output = format((average_accuracy * 100), '.2f')
    threshold_percent = str(threshold * 100) + '%'
    print("Size of array:", size_of_array)
    print("Every " + str(supersonic_rate) + " planes is a supersonic plane")
    print("Number of tests:", number_of_tests)
    print("Threshold:", threshold_percent)
    print("Average Accuracy: " + accuracy_output + "%")

    # save_bernoulli_nb(bernoulli_nb)


main()

