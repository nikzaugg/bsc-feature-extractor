import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def loadData(projectName):

    changeMetrics = list()
    patchFiles = list()

    with open(dir_path+'/'+projectName + '/changeMetrics.csv', 'r', newline='') as csvChangeMetrics:
        csvReader = csv.reader(csvChangeMetrics, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in csvReader:
            changeMetrics.append(row)

    with open(dir_path+'/'+projectName + '/patchFiles.csv', 'r', newline='') as csvpatchFiles:
        csvReader = csv.reader(csvpatchFiles, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in csvReader:
            patchFiles.append(row)

    res = list()
    res.append(changeMetrics)
    res.append(patchFiles)

    return res

def extract(changeData, row):
    revision_nr = row[5]
    commit_id = row[6]
    file_path = row[9]
    
    changeInfo = changeData[0]
    gerritInfo = changeData[1]

    nrev = 0
    featureRow = list()

    resKeys = changeInfo[0][2:]

    for entry in changeInfo:
        if entry[0] == file_path and entry[1] == commit_id:
            nrev = int(entry[2]) - 1
            if nrev == 0:
                pass
    
    if nrev > 0:
        for entry in changeInfo:
            if entry[0] == file_path and entry[2] == str(nrev):
                featureRow = entry[2:]

    resValues = featureRow
    res = dict(zip(resKeys, resValues))

    patchLinesAdd = 0
    patchLinesDel = 0

    for entry in gerritInfo:
        if  entry[1] == revision_nr and entry[3] == file_path:
            patchLinesAdd = entry[4]
            patchLinesDel = entry[5]

    res['PATCH_LINES_ADD'] = patchLinesAdd
    res['PATCH_LINES_DEL'] = patchLinesDel

    return res