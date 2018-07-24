import os
from subprocess import call
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))

def extract(currentFile, previousFile, previousExists):
    jar = dir_path + '/cd.jar'
    output = dir_path+'/tmp/scc.csv'
    if previousExists:
        call(['java', '-jar', jar, currentFile, previousFile, output])
    
    res = list()
    changes = dict()
    severities = dict()

    with open(output, 'r', newline='') as scc:
        scc_reader = csv.reader(scc)
        for line in scc_reader:
            if line[0] in changes:
                changes[line[0]] = changes[line[0]]+1
            elif line[0] not in changes:
                changes[line[0]] = 1
            if line[1] in severities:
                severities[line[1]] = severities[line[1]]+1
            elif line[1] not in severities:
                severities[line[1]] = 1

    res.append(changes)
    res.append(severities)

    return res