import numpy as np

def getLineFrequencies(lineString):
    frequenciesArray = [int(frequency) for frequency in lineString.split(" ")]
    return frequenciesArray

def getLabelIndexByFrequency(frequencies, isMin):
    if isMin:
        return frequencies.tolist().index(min(frequencies))
    else:
        return frequencies.tolist().index(max(frequencies))

def main():
    labelsFile=open("validData.dat", "r")

    allFrequencies = getLineFrequencies(labelsFile.readline())

    for lineString in labelsFile:
        newFrequencies = getLineFrequencies(lineString)
        allFrequencies = np.add(allFrequencies, newFrequencies)

    print(allFrequencies)

    print(getLabelIndexByFrequency(allFrequencies, True))

main()