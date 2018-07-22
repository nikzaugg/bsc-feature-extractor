import csv

def parse(fileLoc, fileName):
    data = list()
    with open(fileLoc, 'r', newline='') as csv_file:
        csvReader = csv.reader(csv_file)
        for line in csvReader:
            data.append(line)

    res = dict()
    res_keys = data[0][3:]
    res_values = list()
    for line in data:
        if line[0] == fileName.replace('/', '\\'):
            res_values = line[3:]
    
    res = dict(zip(res_keys, res_values))
    return res
    