import csv
import os.path
from .ruleClassifier import classifyRule
import xml.etree.ElementTree as ET


def parse(pathToXML, outDir):
    xmlReport = pathToXML
    csvReport = outDir + "/parsed.csv"
    csvAggregatedReport = outDir + "/aggregated.csv"

    file_exists = os.path.isfile(xmlReport)
    if file_exists:
        tree = ET.parse(xmlReport)
        root = tree.getroot()

        rows = list()

        fileName = root[0].get('name')

        # line, severity, message, source
        for violation in root[0]:
            row = list()
            beginLine = violation.get('beginline')
            endLine = violation.get('endline')
            beginColumn = violation.get('begincolumn')
            endColumn = violation.get('endcolumn')
            rule = violation.get('rule')
            ruleset = violation.get('ruleset')
            rule_classified = classifyRule(rule)
            className = violation.get('class')
            methodName = violation.get('method')
            variable = violation.get('variable')
            priority = violation.get('priority')
            message = violation.text
            message_clean = message.replace('\n', '')

            row.append(message_clean)
            row.append(beginLine)
            row.append(endLine)
            row.append(beginColumn)
            row.append(endColumn)
            row.append(rule)
            row.append(ruleset)
            row.append(rule_classified)
            row.append(className)
            row.append(methodName)
            row.append(variable)
            row.append(priority)

            rows.append(row)

        dataRows = list()
        with open(csvReport, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            headers = [
                'message',
                'beginLine',
                'endLine',
                'beginColumn',
                'endColumn',
                'rule',
                'ruleset',
                'classified_rule',
                'className',
                'methodName',
                'variable',
                'priority',
                'filePath'
            ]
            writer.writerow(headers)
            for row in rows:
                dataRows.append(row)
                writer.writerow([
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                    fileName
                ])
        print(">>> PMD Report parsed!")
        
        dataDict = {}
        category_row = 7
        for row in dataRows:
            if row[category_row] in dataDict:
                dataDict[row[category_row]] += 1
            if row[category_row] not in dataDict:
                dataDict[row[category_row]] = 1
        
        with open(csvAggregatedReport, 'w', newline='') as outfile:
            headerRow = list(dataDict)
            headerRow.append('FilePath')
            valueRow = list(dataDict.values())
            valueRow.append(fileName)
            writer = csv.writer(outfile)
            writer.writerow(headerRow)
            writer.writerow(valueRow)
            
        print(">>> PMD Report aggregated!")
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

    print(">>> PMD Diff generated!")
    return delta
