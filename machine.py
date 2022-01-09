from bernoullinb import *
from airplane_helpers import *


def generate_bernoulli_nb(airplane_array, threshold):
    speed_array = get_speed_array(airplane_array)
    is_supersonic_array = get_is_supersonic_array(airplane_array)
    number_of_total_aircraft = len(airplane_array)
    number_of_supersonic_aircraft = count_supersonic_aircraft(is_supersonic_array)
    number_of_subsonic_aircraft = count_subsonic_aircraft(is_supersonic_array, number_of_supersonic_aircraft)
    max_speed = 1133

    bernoulli_nb = BernoulliNB(speed_array, is_supersonic_array, number_of_total_aircraft,
                               number_of_supersonic_aircraft, number_of_subsonic_aircraft, max_speed, threshold)

    return bernoulli_nb


def get_predictions(airplane_array, bernoulli_nb):
    predictions = []
    speed_array = get_speed_array(airplane_array)

    for speed in speed_array:
        prediction = bernoulli_nb.predict(speed)
        predictions.append(prediction)

    return predictions


