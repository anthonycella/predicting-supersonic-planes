def probability_of_supersonic(number_of_supersonic_aircraft_value, number_of_total_aircraft_value):
    number_of_supersonic_aircraft = float(number_of_supersonic_aircraft_value)
    number_of_total_aircraft = float(number_of_total_aircraft_value)

    probability_of_supersonic_aircraft = number_of_supersonic_aircraft / number_of_total_aircraft
    return probability_of_supersonic_aircraft


def probability_of_not_supersonic(number_of_subsonic_aircraft_value, number_of_total_aircraft_value):
    number_of_subsonic_aircraft = float(number_of_subsonic_aircraft_value)
    number_of_total_aircraft = float(number_of_total_aircraft_value)

    probability_of_not_supersonic_aircraft = number_of_subsonic_aircraft / number_of_total_aircraft
    return probability_of_not_supersonic_aircraft


def probability_velocity_given_supersonic(velocity_value, speed_array, is_supersonic_array):
    total_number_of_aircraft = float(len(speed_array))
    velocity_count = 0.0
    laplace_smoothing_numerator = 1.0
    laplace_smoothing_denominator = 2.0

    for current_index in range(0, len(speed_array)):
        current_speed = speed_array[current_index]
        is_supersonic = is_supersonic_array[current_index]

        if current_speed == velocity_value and is_supersonic:
            velocity_count += 1

    probability_of_velocity_given_supersonic = (velocity_count + laplace_smoothing_numerator) / (total_number_of_aircraft + laplace_smoothing_denominator)
    return probability_of_velocity_given_supersonic


def probability_velocity_given_not_supersonic(velocity_value, speed_array, is_supersonic_array):
    total_number_of_aircraft = float(len(speed_array))
    velocity_count = 0.0

    for current_index in range(0, len(speed_array)):
        current_speed = speed_array[current_index]
        is_supersonic = is_supersonic_array[current_index]

        if current_speed == velocity_value and not is_supersonic:
            velocity_count += 1

    probability_of_velocity_given_not_supersonic = velocity_count / total_number_of_aircraft
    return probability_of_velocity_given_not_supersonic


def get_numerator(velocity_value, speed_array, is_supersonic_array, number_of_total_aircraft,
                  number_of_supersonic_aircraft):
    p_of_supersonic = probability_of_supersonic(number_of_supersonic_aircraft, number_of_total_aircraft)
    p_of_v_given_supersonic = probability_velocity_given_supersonic(velocity_value, speed_array, is_supersonic_array)

    numerator = (p_of_supersonic * p_of_v_given_supersonic)
    return numerator


def get_denominator(velocity_value, speed_array, is_supersonic_array, number_of_total_aircraft,
                    number_of_supersonic_aircraft, number_of_subsonic_aircraft):
    probability_of_numerator = get_numerator(velocity_value, speed_array, is_supersonic_array, number_of_total_aircraft,
                                             number_of_supersonic_aircraft)
    p_of_not_supersonic = probability_of_not_supersonic(number_of_subsonic_aircraft, number_of_total_aircraft)
    p_of_v_given_not_supersonic = probability_velocity_given_not_supersonic(velocity_value, speed_array,
                                                                            is_supersonic_array)

    denominator = probability_of_numerator + (
            p_of_not_supersonic * p_of_v_given_not_supersonic)
    return denominator


def probability_of_supersonic_given_velocity(velocity_value, speed_array, is_supersonic_array, number_of_total_aircraft,
                                             number_of_supersonic_aircraft, number_of_subsonic_aircraft):
    numerator = get_numerator(velocity_value, speed_array, is_supersonic_array, number_of_total_aircraft,
                              number_of_supersonic_aircraft)
    denominator = get_denominator(velocity_value, speed_array, is_supersonic_array, number_of_total_aircraft,
                                  number_of_supersonic_aircraft, number_of_subsonic_aircraft)

    probability = numerator / denominator
    return probability
