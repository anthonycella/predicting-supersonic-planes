from sklearn.naive_bayes import BernoulliNB
from airplane import Airplane
import numpy


def generate_airplane_array(size_of_array, supersonic_rate):
    new_array = [] * size_of_array
    for current_index in range(0, len(new_array)):
        if needs_supersonic_aircraft(current_index, supersonic_rate):
            is_supersonic = True
        else:
            is_supersonic = False

        aircraft_id = current_index

        new_array[current_index] = Airplane(is_supersonic, aircraft_id)

    return new_array


def needs_supersonic_aircraft(current_index, supersonic_rate):
    supersonic_threshold = 0
    supersonic_value = current_index * supersonic_rate

    if current_index % supersonic_value == supersonic_threshold:
        return True
    else:
        return False


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


def get_x_component(airplane_array):
    airplane_id_array = get_id_array(airplane_array)
    speed_array = get_speed_array(airplane_array)
    length_of_arrays = len(airplane_array)

    x_component = numpy.array([airplane_id_array, speed_array])
    x_component = x_component.reshape(length_of_arrays, 2)

    return x_component


def get_y_component(airplane_array):
    is_supersonic_array = get_is_supersonic_array(airplane_array)
    return is_supersonic_array


def generate_x_and_y(size_of_array, every_nth_aircraft_is_a_supersonic_plane):
    supersonic_rate = float(1 / every_nth_aircraft_is_a_supersonic_plane)
    airplane_array = generate_airplane_array(size_of_array, supersonic_rate)

    x_component = get_x_component(airplane_array)
    y_component = get_y_component(airplane_array)

    return x_component, y_component


def count_true_predictions(boolean_array):
    count = 0

    for boolean in boolean_array:
        if boolean:
            count += 1

    return count
