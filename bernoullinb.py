import probability


def generate_probability_vocabulary(speed_array, is_supersonic_array, number_of_total_aircraft,
                                    number_of_supersonic_aircraft, number_of_subsonic_aircraft, max_speed):
    probability_vocabulary = []

    for velocity_value in range(0, max_speed):
        probability_supersonic_given_v = probability.probability_of_supersonic_given_velocity(velocity_value,
                                                                                              speed_array,
                                                                                              is_supersonic_array,
                                                                                              number_of_total_aircraft,
                                                                                              number_of_supersonic_aircraft,
                                                                                              number_of_subsonic_aircraft)
        # print(probability_supersonic_given_v) # debugger statement
        probability_vocabulary.append(probability_supersonic_given_v)

    return probability_vocabulary


def generate_prediction_vocabulary(probability_vocabulary, threshold):
    prediction_vocabulary = []

    for probability_value in probability_vocabulary:
        if probability_value >= threshold:
            prediction_vocabulary.append(True)
        else:
            prediction_vocabulary.append(False)

    return prediction_vocabulary


class BernoulliNB:
    def __init__(self, speed_array, is_supersonic_array, number_of_total_aircraft,
                 number_of_supersonic_aircraft, number_of_subsonic_aircraft, max_speed, threshold):
        self.__probability_vocabulary = generate_probability_vocabulary(speed_array, is_supersonic_array,
                                                                        number_of_total_aircraft,
                                                                        number_of_supersonic_aircraft,
                                                                        number_of_subsonic_aircraft, max_speed)
        self.__prediction_vocabulary = generate_prediction_vocabulary(self.__probability_vocabulary, threshold)

    def get_prediction_vocabulary(self):
        return self.__prediction_vocabulary

    def set_prediction_vocabulary(self, new_threshold):
        self.__prediction_vocabulary = generate_prediction_vocabulary(self.__probability_vocabulary, new_threshold)

    def predict(self, speed):
        prediction = self.__prediction_vocabulary[speed]
        return prediction
