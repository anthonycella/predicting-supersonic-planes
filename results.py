import machine
from airplane_helpers import *
from bernoullinb import BernoulliNB


def get_average_accuracy(number_of_tests, bernoulli_nb, size_of_array, supersonic_rate):
    accuracies = get_accuracies(number_of_tests, bernoulli_nb, size_of_array, supersonic_rate)
    total_accuracy_value = get_total_accuracy_value(accuracies)

    average_accuracy = total_accuracy_value / number_of_tests
    return average_accuracy


def get_total_accuracy_value(accuracies):
    total_accuracy_value = 0.0

    for accuracy in accuracies:
        total_accuracy_value += accuracy

    return total_accuracy_value


def get_accuracies(number_of_tests, bernoulli_nb, size_of_array, supersonic_rate):
    accuracies = []
    for i in range(0, number_of_tests):
        airplane_array = generate_airplane_array(size_of_array, supersonic_rate)
        predictions = machine.get_predictions(airplane_array, bernoulli_nb)
        actual_results = get_is_supersonic_array(airplane_array)

        accuracy = get_accuracy(predictions, actual_results)
        accuracies.append(accuracy)

    return accuracies


def get_accuracy(predictions, actual_results):
    total_number = float(len(actual_results))
    number_of_correct_matches = get_number_of_correct_matches(predictions, actual_results)

    accuracy = number_of_correct_matches / total_number
    return accuracy


def get_number_of_correct_matches(predictions, actual_results):
    number_of_correct_matches = 0.0

    for current_index in range(0, len(actual_results)):
        prediction = predictions[current_index]
        actual_result = actual_results[current_index]

        if prediction == actual_result:
            number_of_correct_matches += 1

    return number_of_correct_matches
