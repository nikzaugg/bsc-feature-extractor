import shutil
import os
import sys
import subprocess
from .featureAggregator import aggregate

dir_path = os.path.dirname(os.path.realpath(__file__))

def extract(currentFile, previousFile, previousExists):
    filePath_current = currentFile
    filePath_previous = previousFile

    # copy the two files
    shutil.copy(filePath_current, dir_path + '/current')
    if previousExists:
        shutil.copy(filePath_previous, dir_path + '/previous')

    jar = dir_path + '/ucc-j.jar'

    # create a code-metric report for each file
    subprocess.call(["java", "-jar", jar, "-dir", dir_path + "/current", "-outdir", dir_path + "/current-result", "-unified"])
    if previousExists:
        subprocess.call(["java", "-jar", jar, "-dir", dir_path + "/previous", "-outdir", dir_path + "/previous-result", "-unified"])

    features = aggregate(previousExists)

    deleteFolderContents(dir_path + '/current') 
    deleteFolderContents(dir_path + '/previous')
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