import csv
import pandas as pd
import numpy as np




def writeFeatureRows(featureRows, dataSetName):
    headers = list()
    # find out what should be the names of the features (column names)
    for featureDict in featureRows:
        for key in featureDict.keys():
            if key not in headers:
                headers.append(key)
    
    with open('trainingset/'+dataSetName, 'w', newline='') as trainingSet:
        csvWriter = csv.writer(trainingSet)
        csvWriter.writerow(headers)
        for featureDict in featureRows:
            newLine = list()
            for col in headers:
                if col in featureDict.keys():
                    newLine.append(featureDict[col])
                else:
                    newLine.append(0)
            csvWriter.writerow(newLine)


