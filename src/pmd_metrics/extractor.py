import os
from subprocess import call
from .pmdParser import parse, diff

dir_path = os.path.dirname(os.path.realpath(__file__))

# run checkstyle on files
current_out_dir = dir_path + '/current'
previous_out_dir = dir_path + '/previous'

def extract(currentFile, previousFile, previousExists):
    print(">>>>>>>>>>>>>>>>>>>>>PMD<<<<<<<<<<<<<<<<<<<<<<<")

    current_xml = current_out_dir + '/current.xml'
    previous_xml = previous_out_dir + '/previous.xml'
    
    # parse xml
    res = list()
    delta = None
    previous_res = None
    call("pmd -d " + currentFile + " -f xml -R rulesets/internal/all-java.xml -r " + current_xml, shell=True)
    current_res =  parse(current_xml, current_out_dir)

    if previousExists:
        call("pmd -d " + previousFile +
         " -f xml -R rulesets/internal/all-java.xml -r " + previous_xml, shell=True)
        previous_res = parse(previous_xml, previous_out_dir)
        delta = diff(current_out_dir, previous_out_dir)
        res.append(delta)
        res.append(current_res)
        res.append(previous_res)
    else :
        res.append(current_res)
        res.append(current_res)
        res.append(current_res)

    # deleteFolderContents(dir_path + '/current') 
    # deleteFolderContents(dir_path + '/previous')

    # return res
    return res


def deleteFolderContents(folderName):
    folder = folderName
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)