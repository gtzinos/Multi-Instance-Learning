from config.labels_constants import *
from config.data_constants import *

import pandas as pd
from utils.most_significant import *
from utils.new_preprocessing import *


def main():
    #Train labels most significant
    train_most_significant = getMostSignificantLabel(DATA_PATH + TRAIN_LABELS_NAME, LABELS_SEPERATOR, LABELS_NAMES)
    print("Train Most Significant: ", train_most_significant)

    #Test labels most significant
    test_most_significant = getMostSignificantLabel(DATA_PATH + TEST_LABELS_NAME, LABELS_SEPERATOR, LABELS_NAMES)
    print("Test Most Significant: ", test_most_significant)

    #Preprocessing train file
    convert_labels_to_binary(DATA_PATH + TRAIN_LABELS_NAME, 2,
                            DATA_PATH + "new_" + TRAIN_LABELS_NAME)
    convert_labels_to_binary(DATA_PATH + TEST_LABELS_NAME, 2,
                            DATA_PATH + "new_" + TEST_LABELS_NAME)

    #convert_sentences_to_binary("./data/train-sentlabel.dat", 2, "./data/new_train-sentlabel.dat")
    convert_sentences_to_binary(
        "./data/test-sentlabel.dat", 2, "./data/new_test-sentlabel.dat")

main()