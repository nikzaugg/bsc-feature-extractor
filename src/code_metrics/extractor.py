import shutil
import os
import sys
import subprocess
from .featureAggregator import aggregate

dir_path = os.path.dirname(os.path.realpath(__file__))

# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)
# os.chdir(dname)

def createLog(record):
    # create path to the two files
    filePath_current = dir_path + '/current-repo/class.java'
    filePath_previous = dir_path + '/previous-repo/class.java'

    # copy the two files
    shutil.copy(filePath_current, dir_path + '/current')
    shutil.copy(filePath_previous, dir_path + '/previous')

    jar = dir_path + '/ucc-j.jar'

    # create a code-metric report for each file
    subprocess.call(["java", "-jar", jar, "-dir", dir_path + "/current", "-outdir", dir_path + "/current-result", "-unified"])
    subprocess.call(["java", "-jar", jar, "-dir", dir_path + "/previous", "-outdir", dir_path + "/previous-result", "-unified"])

    features = aggregate()

    deleteFolderContents(dir_path + '/current-result') 
    deleteFolderContents(dir_path + '/previous-result')

    return features

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