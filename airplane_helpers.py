from airplane import Airplane


def generate_airplane_array(size_of_array, supersonic_rate):
    new_airplane_array = []
    for current_index in range(0, size_of_array):
        if needs_supersonic_aircraft(current_index, supersonic_rate):
            is_supersonic = True
        else:
            is_supersonic = False

        aircraft_id = current_index

        new_aircraft = Airplane(is_supersonic, aircraft_id)
        new_airplane_array.append(new_aircraft)

    return new_airplane_array


def needs_supersonic_aircraft(current_index, supersonic_rate):
    supersonic_threshold = 0
    current_index_value = current_index + 1

    if current_index_value % supersonic_rate == supersonic_threshold:
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


def count_supersonic_aircraft(is_supersonic_array):
    supersonic_count = 0

    for is_supersonic_value in is_supersonic_array:
        if is_supersonic_value:
            supersonic_count += 1

    return supersonic_count


def count_subsonic_aircraft(is_supersonic_array, supersonic_aircraft_count):
    total_number_of_aircraft = len(is_supersonic_array)
    subsonic_count = total_number_of_aircraft - supersonic_aircraft_count

    return subsonic_count


def get_supersonic_and_subsonic_counts(is_supersonic_array):
    supersonic_count = count_supersonic_aircraft(is_supersonic_array)
    subsonic_count = count_subsonic_aircraft(is_supersonic_array, supersonic_count)

    return supersonic_count, subsonic_count

