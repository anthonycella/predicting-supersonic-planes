import random
from random import random

from numpy.random import randint


def choose_top_speed_in_knots(is_supersonic):
    if is_supersonic:
        return 1133
    else:
        return 566


def generate_air_speed_in_knots(top_speed_in_knots):
    air_speed_in_knots = randint(0, top_speed_in_knots)
    return air_speed_in_knots


class Airplane:
    def __init__(self, is_supersonic_aircraft=False, aircraft_id=-1):
        self.__is_supersonic_aircraft = is_supersonic_aircraft
        top_speed_in_knots = choose_top_speed_in_knots(self.__is_supersonic_aircraft)
        self.__air_speed_in_knots = generate_air_speed_in_knots(top_speed_in_knots)
        self.__aircraft_id = aircraft_id

    def is_supersonic_aircraft(self):
        return self.__is_supersonic_aircraft

    def get_air_speed_in_knots(self):
        return self.__air_speed_in_knots

    def get_aircraft_id(self):
        return self.__aircraft_id

    def __str__(self):
        return "Is Supersonic Aircraft: " + str(self.__is_supersonic_aircraft) + "\tAir Speed In Knots: " \
               + str(self.__air_speed_in_knots) + "\tID: " + str(self.__aircraft_id)

