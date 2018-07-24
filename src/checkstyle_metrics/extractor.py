import os
from subprocess import call
from .checkstyleParser import parse, diff

dir_path = os.path.dirname(os.path.realpath(__file__))

# Location of Checks.xml
sun_checks = dir_path + "/checks/sun_checks.xml"
google_checks = dir_path + "/checks/google_checks.xml"

# run checkstyle on files
current_out_dir = dir_path + '/current'
previous_out_dir = dir_path + '/previous'

# Location of Checkstyle .jar
jar = dir_path + "/checkstyle-8.11-all.jar"

def extract(currentFile, previousFile, previousExists):
    print(">>>>>>>>>>>>>>>>>>>>>CHECKSTYLE<<<<<<<<<<<<<<<<<<<<<<<")
    current_xml = current_out_dir + '/current.xml'
    previous_xml = previous_out_dir + '/previous.xml'
    # run checkstyle on specified file and output xml-results into /results
    call(["java", "-jar", jar, "-c", sun_checks, currentFile, "-f", "xml", "-o", current_xml])
    if previousExists:
        call(["java", "-jar", jar, "-c", sun_checks, previousFile, "-f", "xml", "-o", previous_xml])

    # parse xml
    res = list()
    delta = None
    previous_res = None
    current_res = parse(current_xml, current_out_dir)
    if previousExists:
        previous_res = parse(previous_xml, previous_out_dir)
        delta = diff(current_out_dir, previous_out_dir)

        res.append(delta)
        res.append(current_res)
        res.append(previous_res) 
    else:
        res.append(current_res)  
    deleteFolderContents(dir_path + '/current') 
    deleteFolderContents(dir_path + '/previous')

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