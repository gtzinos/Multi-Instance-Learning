from config.labels import *
import pandas as pd
from utils.most_significant import *
from utils.preprocessing import *


def main():
    df = pd.read_csv("test-label", header= None, sep=LABEL_SEPERATOR,
                 names = LABELS_NAMES)

    most_significant = getMostSignificantLabel(df)

    print(most_significant)

main()