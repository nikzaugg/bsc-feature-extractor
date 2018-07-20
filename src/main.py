import pandas as pd
import numpy as np
import sys
import os
from code_metrics import extractor
from git import Repo
import subprocess
from subprocess import Popen, PIPE
from os import path


def main():
    """ Main entry point to compute features for the training-set """

    ########################
    # DATA CREATED BEFORE  #
    ########################
    # 1) load ChangeDistiller output for current project

    # 2) load tf-idf matrix of considered commit-messages

    # 3) load Change-Metrics of each considered file

    ###############################
    # 4) load preprocess-dataset  #
    ###############################
    preprocess_data = pd.read_csv('preprocess_dataset/dataset.csv')

    ############################
    # COMPUTE METRICS FOR FILE #
    ############################
    # list() of list() of features
    feature_rows = list()

    # for each file in preprocess-dataset
    for row in preprocess_data.itertuples():
        feature_row = list()
        code_metrics = dict()

        # list() code-metrics
        # list() checkstyle-metrics
        # list() pmd-metrics
        # list() change-metrics
        # list() tf-idf features
        # list() ck-metrics
        # list() scc-metrics
        # list() labels

        ####################################################################
        # 5) fetch patch of file & fetch patch of previous patchset/base   #
        ####################################################################
        fetch_url = row[1]
        project_name = row[2]
        revision_nr = row[5]
        ref = row[6]
        file_path = row[8]
        repo_dir = row[9]

        repo_current_loc = repo_dir + '/current-' + project_name + '/'
        repo_previous_loc = repo_dir + '/previous-' + project_name + '/'

        fname_current = repo_current_loc + file_path
        fname_previous = repo_previous_loc + file_path

        f_current_exists = False
        f_previous_exists = False

        # CHECKOUT CURRENT
        print("<=========================== CURRENT ==============================>")
        checkout_ref(repo_current_loc, ref, fetch_url)
        f_current_exists = os.path.isfile(fname_current)
        print("<=============FILE EXISTS============>", f_current_exists)

        # CHECKOUT PREVIOUS
        # https://stackoverflow.com/questions/692246/undo-working-copy-modifications-of-one-file-in-git
        patch_nr = ref.split("/")[-1]
        # If current patch is patch nr. 1
        if int(patch_nr) == 1:
            print("<=========================== PREVIOUS ==============================>")
            checkout_prev_file_version(repo_previous_loc, file_path, revision_nr)
            f_previous_exists = os.path.isfile(fname_previous)
            print("<=============FILE EXISTS============>", f_previous_exists)
        # If current patch is not patch nr. 1
        else:
            previous_ref = int(patch_nr) - 1
            new_ref = ref.split("/")[:-1]
            x = ''
            for s in new_ref:
                x = x+s+'/'
            x = x + str(previous_ref)
            print("<=========================== PREVIOUS ==============================>")
            checkout_ref(repo_previous_loc, x, fetch_url)
            f_previous_exists = os.path.isfile(fname_previous)
            print("<=============FILE EXISTS============>", f_previous_exists)
            
            
        #############################################
        # 6) compute Code-Metrics -> save features  #
        #############################################
        code_metrics = extractor.createLog(fname_current, fname_previous, f_previous_exists)

        # 7) compute checkstyle-metrics -> save features

        # 8) compute pmd-metrics -> save features

        # 9) lookup change-metrics -> save features

        # 10) lookup tf-idf row -> save features

        # 11) compute ck-metrics -> save features

        # 12) lookup ChangeDistiller types -> save features

        # 13) extract labels --> save

        # 14) add each feature list to features
        feature_row.append(code_metrics)
        feature_rows.append(feature_row)
    # 15) print each feature-row into a data-set
    print(len(feature_rows))
    print('> finished analyzing')


def checkout_ref(repoLoc, ref, fetchUrl):
    repository = path.dirname(repoLoc)

    git_command = ['git', 'fetch', fetchUrl, ref]
    git_query = subprocess.Popen(git_command, cwd=repository)
    git_query.communicate()

    git_command2 = ['git', 'checkout', 'FETCH_HEAD', '--force']
    git_query2 = subprocess.Popen(git_command2, cwd=repository)
    git_query2.communicate()

def checkout_prev_file_version(repoLoc, filePath, revisionNr):
    repository = path.dirname(repoLoc)

    git_command = ['git', 'checkout', revisionNr, '--force']
    git_query = subprocess.Popen(git_command, cwd=repository)
    git_query.communicate()

    git_command2 = ['git', 'checkout', 'HEAD^', filePath]
    git_query2 = subprocess.Popen(git_command2, cwd=repository)
    git_query2.communicate()

if __name__ == "__main__":
    main()
