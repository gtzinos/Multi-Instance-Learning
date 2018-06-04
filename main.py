from config.labels_constants import *
from config.data_constants import *

import pandas as pd
from utils.most_significant import *


def main():
    train_most_significant = getMostSignificantLabel(DATA_PATH + TRAIN_LABELS_NAME, LABELS_SEPERATOR, LABELS_NAMES)
    print("Train Most Significant: ", train_most_significant)

    test_most_significant = getMostSignificantLabel(DATA_PATH + TEST_LABELS_NAME, LABELS_SEPERATOR, LABELS_NAMES)
    print("Test Most Significant: ", test_most_significant)

main()