import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

dictNames = list(["TOT_LINES", "BLANK_LINES", "COMMENTS", "EMBEDDED", "COMPILER_DIRECT", "DATA_DECL", "EXEC_INSTR", "LOGIC_SLOC", "PHYS_SLOC", "CC1_TOT", "CC1_AVG"])

def aggregate(previousExists):
    sloc_current = dir_path + '/current-result/TOTAL_outfile.csv'
    cplx_current = dir_path + '/current-result/outfile_cyclomatic_cplx.csv'
    
    csvData_current = list()
    keys_current = dictNames
    values_current = list()
    # Compute SLOC metrics
    with open(sloc_current) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            csvData_current.append(row)
        for i in range(9):
            values_current.append(csvData_current[11][i])
        csvfile.close()

    # Compute Cyclomatic Complexity
    with open(cplx_current) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        cplxRows = list()
        for row in readCSV:
            cplxRows.append(row)
        values_current.append(cplxRows[11][0])
        values_current.append(cplxRows[11][3])
        csvfile.close()

    res_current = dict(zip(keys_current, values_current))

    if previousExists:
        sloc_previous = dir_path + '/previous-result/TOTAL_outfile.csv'
        cplx_previous = dir_path + '/previous-result/outfile_cyclomatic_cplx.csv'

        csvData_previous = list()
        keys_previous = dictNames
        values_previous = list()
        # Compute SLOC metrics
        with open(sloc_previous) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                csvData_previous.append(row)
            for i in range(9):
                values_previous.append(csvData_previous[11][i])
            csvfile.close()

        # Compute Cyclomatic Complexity
        with open(cplx_previous) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            cplxRows = list()
            for row in readCSV:
                cplxRows.append(row)
            values_previous.append(cplxRows[11][0])
            values_previous.append(cplxRows[11][3])
            csvfile.close()

        res_previous = dict(zip(keys_previous, values_previous))

        diff = dict()
        for (k,v) in res_current.items():
            diff[k] = float(v) - float(res_previous[k])

        res = list()
        res.append(diff)
        res.append(res_current)
        res.append(res_previous)
        
    else:
        res = list()
        res.append(res_current)
        res.append(res_current)
        res.append(res_current)

    return res