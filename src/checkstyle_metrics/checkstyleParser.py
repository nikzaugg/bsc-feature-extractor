import csv
import xml.etree.ElementTree as ET
import os.path
from .ruleClassifier import classifyRule


def parse(pathToXML, outDir):

    xmlReport = pathToXML
    csvReport = outDir + "/parsed.csv"
    csvAggregatedReport = outDir + "/aggregated.csv"

    file_exists = os.path.isfile(pathToXML)
    if file_exists:
        tree = ET.parse(xmlReport)

        root = tree.getroot()

        rows = list()

        fileName = root.findall('file')[0].get('name')

        # line, severity, message, source
        for error in root[0].findall('error'):
            row = list()
            line = error.get('line')
            column = error.get('column')
            severity = error.get('severity')
            message = error.get('message')
            rule = error.get('source')
            cleanRule = rule.replace(
                'com.puppycrawl.tools.checkstyle.checks.', ' ')
            sep = '.'
            cleanRuleShort = cleanRule.split(sep, 1)[-1]
            cleanRuleShortNoCheck = cleanRuleShort.replace("Check", "")
            classifiedRule = classifyRule(cleanRuleShortNoCheck)

            row.append(line)
            row.append(column)
            row.append(severity)
            row.append(message)
            row.append(cleanRuleShortNoCheck)
            row.append(classifiedRule)
            rows.append(row)

        dataRows = list()
        with open(csvReport, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            headers = ['Line', 'Column', 'Severity', 'Message',
                       'Rule', 'Classified_Rule', 'File_Path']
            writer.writerow(headers)
            for row in rows:
                dataRows.append(row)
                writer.writerow([
                    row[0], row[1], row[2], row[3], row[4], row[5], fileName
                ])
        print(">>> Checkstyle Report parsed!")

        dataDict = {}
        for row in dataRows:
            if row[5] in dataDict:
                dataDict[row[5]] += 1
            if row[5] not in dataDict:
                dataDict[row[5]] = 1

        with open(csvAggregatedReport, 'w', newline='') as outfile:
            headerRow = list(dataDict)
            headerRow.append('FilePath')
            valueRow = list(dataDict.values())
            valueRow.append(fileName)
            writer = csv.writer(outfile)
            writer.writerow(headerRow)
            writer.writerow(valueRow)
            
        print(">>> Checkstyle Report aggregated!")
        return dataDict
        


def diff(currentReportDir, previousReportDir):
    dataRows_left = list()
    dataRows_right = list()
    left = dict()
    right = dict()
    leftReport = currentReportDir + '/aggregated.csv'
    rightReport = previousReportDir + '/aggregated.csv'

    with open(leftReport, 'r', newline='') as leftcsv:
        for row in leftcsv:
            cleanRow = row.replace("\r\n", "")
            dataRows_left.append(cleanRow)

        categories_left = dataRows_left[0].split(",")
        values_left = dataRows_left[1].split(",")

        left = dict(zip(categories_left, values_left))

    with open(rightReport, 'r', newline='') as rightcsv:
        for row in rightcsv:
            cleanRow = row.replace("\r\n", "")
            dataRows_right.append(cleanRow)

        categories_right = dataRows_right[0].split(",")
        values_right = dataRows_right[1].split(",")

        right = dict(zip(categories_right, values_right))

    # print(len(left) ,left)
    # print(len(right), right)

    delta = dict()
    # left
    for key, val in left.items():

        if key in right.keys():
            if ".java" not in left[key]:
                difference = int(right[key]) - int(left[key])
                # print(int(right[key]), " - ",int(left[key]), "  =  ", difference)
                delta[key] = difference
        else:
            delta[key] = left[key]

    # right
    for key, val in right.items():
        # if key from right is not in left
        if key not in left.keys():
            delta[key] = right[key]

    delta["FilePath"] = right["FilePath"]
    # print(len(delta), delta)

    print(">>> Checkstyle Diff generated!")
    return delta
