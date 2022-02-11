#
# Author: Anthony Cella
# a file containing the main function, the file to run the application on.
# Last updated: 1/29/22
#


from data.extract_data import get_patients
from helper_methods.results import get_tree_accuracy, get_forest_accuracy
from random_forest.forest import *


# Instructions

# ------------------- Software -------------------------------- #
# Make sure your python interpreter is using python 3.10
# The code will not run properly on older versions
# If you need to update:
# 1. go to the python website and download the latest version
# 2. create a new project and configure the python interpreter to the latest version
# 3. download this code into that project
# ------------------------------------------------------------ #

# ------------------ Data Input ---------------------------------------------- #
# Computer will ignore the first row, so do not put anything you want read in row 1
# Put the standard of truth in Column B (the second column)
# Put variables you want read anywhere in columns D - L (columns 4 - 12)
# ---------------------------------------------------------------------------- #

# ------------------ Execution ------------------------------------------------ #
# put the file path name in the variable file_path_name as a String
# put how deep you want the trees in tree_depth. number of leaf nodes corresponds to: 2 ^ (tree_depth - 1)
#   (so if you want 8 different possible spots for patients to land on you would put: tree_depth = 4)
# put which columns you want to read in columns_wanted in format [col#, col#, col#...] between 4 and 12 inclusive
# ------------------------------------------------------------------------------ #

def main():
    file_path_name = "../data/Olympus DaTQUANT values for Anthony.csv"
    tree_depth = 3
    columns_wanted = [4, 5, 9, 6]

    patients = get_patients(file_path_name, True)

    random_forest = build_forest(file_path_name, tree_depth, columns_wanted)
    forest_accuracy = get_forest_accuracy(random_forest, patients)

    print(forest_accuracy)


main()
