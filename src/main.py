import sys
import os
import subprocess

import pandas as pd
import numpy as np

from code_metrics import extractor as metrics_code
from checkstyle_metrics import extractor as metrics_checkstyle
from pmd_metrics import extractor as metrics_pmd
from ck_metrics import extractor as metrics_ck
from change_metrics import extractor as metrics_change
from nlp_metrics import extractor as metrics_nlp
from scc_metrics import extractor as metrics_scc

import dataSetWriter as writer


def main():
    """ Main entry point to compute features for the training-set """

    CODE_METRICS = True
    CHECKSTYLE_METRICS = True
    PMD_METRICS = True
    CK_METRICS = True
    CHANGE_METRICS = True
    NLP_METRICS = True
    SCC_METRICS = True

    #######################################################
    # 1) load tf-idf matrix of considered commit-messages #
    #######################################################
    nlp_data = metrics_nlp.generate()

    ##################################################
    # 2) load Change-Metrics of each considered file #
    ##################################################
    changeData = metrics_change.loadData('acceleo')

    ##############################
    # 3) load preprocess-dataset #
    ##############################
    preprocess_data = pd.read_csv('preprocess_dataset/dataset_big.csv')

    ############################
    # COMPUTE METRICS FOR FILE #
    ############################
    feature_rows = list()

    code_metrics_features = list()
    checkstyle_metrics_features = list()
    pmd_metrics_features = list()
    ck_metrics_features = list()
    change_metrics_features = list()
    nlp_metrics_features = list()
    scc_metrics_features = list()
    labels = list()

    # for each file in preprocess-dataset
    for row in preprocess_data.itertuples():
        ##################################################################
        # 4) fetch patch of file & fetch patch of previous patchset/base #
        ##################################################################
        fetch_url = row[1]
        project_name = row[2]
        change_id = row[4]
        revision_nr = row[5]
        ref = row[7]
        file_path = row[9]
        repo_dir = row[10]

        REPO_CURRENT_LOC = repo_dir + '/current-' + project_name + '/'
        REPO_PREVIOUS_LOC = repo_dir + '/previous-' + project_name + '/'

        FILE_CURRENT = REPO_CURRENT_LOC + file_path
        FILE_PREVIOUS = REPO_PREVIOUS_LOC + file_path

        CURRENT_FILE_EXISTS = False
        PREVIOUS_FILE_EXISTS = False

        # CHECKOUT CURRENT VERSION OF FILE
        print("<=========================== CURRENT ==============================>")
        checkout_ref(REPO_CURRENT_LOC, ref, fetch_url)
        CURRENT_FILE_EXISTS = os.path.isfile(FILE_CURRENT)
        print("FILE EXISTS =>", CURRENT_FILE_EXISTS)

        # CHECKOUT PREVIOUS VERSION OF FILE
        patch_nr = ref.split("/")[-1]
        # If current patch is patch nr. 1
        if int(patch_nr) == 1:
            print("<=========================== PREVIOUS ==============================>")
            checkout_prev_file_version(
                REPO_PREVIOUS_LOC, file_path, revision_nr)
            PREVIOUS_FILE_EXISTS = os.path.isfile(FILE_PREVIOUS)
            print("FILE EXISTS =>", PREVIOUS_FILE_EXISTS)
            print("\n")
        # If current patch is not patch nr. 1
        else:
            previous_ref = int(patch_nr) - 1
            new_ref = ref.split("/")[:-1]
            x = ''
            for s in new_ref:
                x = x+s+'/'
            x = x + str(previous_ref)
            print("<=========================== PREVIOUS ==============================>")
            checkout_ref(REPO_PREVIOUS_LOC, x, fetch_url)
            PREVIOUS_FILE_EXISTS = os.path.isfile(FILE_PREVIOUS)
            print("FILE EXISTS =>", PREVIOUS_FILE_EXISTS)
            print("\n")

        ############################################
        # 5) compute Code-Metrics -> save features #
        ############################################
        if CODE_METRICS:
            code_metrics = metrics_code.extract(
                FILE_CURRENT, FILE_PREVIOUS, PREVIOUS_FILE_EXISTS)
            code_metrics[0]['fileName'] = file_path
            code_metrics[0]['changeId'] = change_id
            code_metrics[0]['patchId'] = revision_nr
            code_metrics[0]['patchRef'] = ref
            code_metrics_features.append(code_metrics[0])

        ##################################################
        # 6) compute checkstyle-metrics -> save features #
        ##################################################
        if CHECKSTYLE_METRICS:
            checkstyle_metrics = metrics_checkstyle.extract(
                FILE_CURRENT, FILE_PREVIOUS, PREVIOUS_FILE_EXISTS)
            checkstyle_metrics[0]['fileName'] = file_path
            checkstyle_metrics[0]['changeId'] = change_id
            checkstyle_metrics[0]['patchId'] = revision_nr
            checkstyle_metrics[0]['patchRef'] = ref
            checkstyle_metrics_features.append(checkstyle_metrics[0])

        ###########################################
        # 7) compute pmd-metrics -> save features #
        ###########################################
        if PMD_METRICS:
            pmd_metrics = metrics_pmd.extract(
                FILE_CURRENT, FILE_PREVIOUS, PREVIOUS_FILE_EXISTS)
            pmd_metrics[0]['fileName'] = file_path
            pmd_metrics[0]['changeId'] = change_id
            pmd_metrics[0]['patchId'] = revision_nr
            pmd_metrics[0]['patchRef'] = ref
            pmd_metrics_features.append(pmd_metrics[0])

        ###########################################
        # 8) compute ck-metrics -> save features #
        ###########################################
        if CK_METRICS:
            ck_metrics = metrics_ck.extract(
                FILE_CURRENT, FILE_PREVIOUS, PREVIOUS_FILE_EXISTS)
            ck_metrics[0]['fileName'] = file_path
            ck_metrics[0]['changeId'] = change_id
            ck_metrics[0]['patchId'] = revision_nr
            ck_metrics[0]['patchRef'] = ref
            ck_metrics_features.append(ck_metrics[0])

        #############################################
        # 9) lookup change-metrics -> save features #
        #############################################
        if CHANGE_METRICS:
            change_metrics = metrics_change.extract(changeData, row)
            change_metrics['fileName'] = file_path
            change_metrics['changeId'] = change_id
            change_metrics['patchId'] = revision_nr
            change_metrics['patchRef'] = ref
            change_metrics_features.append(change_metrics)

        ##########################################
        # 10) lookup tf-idf row -> save features #
        ##########################################
        if NLP_METRICS:
            nlp_metrics = metrics_nlp.extract(nlp_data, row)
            nlp_metrics['fileName'] = file_path
            nlp_metrics['changeId'] = change_id
            nlp_metrics['patchId'] = revision_nr
            nlp_metrics['patchRef'] = ref
            nlp_metrics_features.append(nlp_metrics)

        #####################################################
        # 11) lookup ChangeDistiller types -> save features #
        #####################################################
        if SCC_METRICS:
            scc_metrics = metrics_scc.extract(
                FILE_CURRENT, FILE_PREVIOUS, PREVIOUS_FILE_EXISTS)
            scc_metrics[0]['fileName'] = file_path
            scc_metrics[0]['changeId'] = change_id
            scc_metrics[0]['patchId'] = revision_nr
            scc_metrics[0]['patchRef'] = ref
            scc_metrics_features.append(scc_metrics[0])

        ###############################
        # 12) extract labels --> save #
        ###############################
        lbls = dict()
        ls = row[15].split(';')
        lbls['fileName'] = file_path
        lbls['changeId'] = change_id
        lbls['patchId'] = revision_nr
        lbls['patchRef'] = ref
        lbls['labels'] = ls

        labels.append(lbls)

    ##############################################
    # 13) print each feature-row into a data-set #
    ##############################################

    print(" ")
    if CODE_METRICS:
        writer.writeFeatureRows(code_metrics_features, "code_metrics_diff.csv")
    if CHECKSTYLE_METRICS:
        writer.writeFeatureRows(
            checkstyle_metrics_features, "checkstyle_metrics_diff.csv")
    if PMD_METRICS:
        writer.writeFeatureRows(pmd_metrics_features, "pmd_metrics_diff.csv")
    if CK_METRICS:
        writer.writeFeatureRows(ck_metrics_features, "ck_metrics_diff.csv")
    if CHANGE_METRICS:
        writer.writeFeatureRows(change_metrics_features, "change_metrics.csv")
    if NLP_METRICS:
        writer.writeFeatureRows(nlp_metrics_features, "nlp_metrics.csv")
    if SCC_METRICS:
        writer.writeFeatureRows(scc_metrics_features, "scc_metrics.csv")
    writer.writeFeatureRows(labels, "labels.csv")

    print('> finished analyzing')


def checkout_ref(repoLoc, ref, fetchUrl):
    """ checkout a ref (refs/*/changes/*) of a given repository """
    repository = os.path.dirname(repoLoc)

    git_command = ['git', 'fetch', fetchUrl, ref]
    git_query = subprocess.Popen(git_command, cwd=repository)
    git_query.communicate()

    git_command2 = ['git', 'checkout', 'FETCH_HEAD', '--force']
    git_query2 = subprocess.Popen(git_command2, cwd=repository)
    git_query2.communicate()


def checkout_prev_file_version(repoLoc, filePath, revisionNr):
    """ checkout the previous commit where the given file was last modified of a given repository """
    repository = os.path.dirname(repoLoc)

    git_command = ['git', 'checkout', revisionNr, '--force']
    git_query = subprocess.Popen(git_command, cwd=repository)
    git_query.communicate()

    git_command2 = ['git', 'checkout', 'HEAD^', filePath]
    git_query2 = subprocess.Popen(git_command2, cwd=repository)
    git_query2.communicate()


if __name__ == "__main__":
    main()
