from collections import defaultdict

import pandas as pd
import numpy as np

def getMostSignificantLabel(labelDF):
    shapeOfDF = labelDF.shape
    numberOfColumns = shapeOfDF[1]
    listOfLabelSum = {}
    colNameSumList = defaultdict(list)
    # colNameSumList = list()

    columnNames = list(df.columns.values)

    for i in range(0, numberOfColumns):
        colNameSumTuple = pd.Series(df[columnNames[i]].sum(), index=[columnNames[i]])
        colNameSumList[colNameSumTuple[0]].append(columnNames[i])

    mostInsignificantLabel = max(colNameSumList.items())

    print(mostInsignificantLabel)
    print(mostInsignificantLabel[1][0])
    print(colNameSumList)
    return mostInsignificantLabel[1][0]