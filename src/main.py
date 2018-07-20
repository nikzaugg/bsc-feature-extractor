import pandas as pd
import numpy as np
import sys
import os
from code_metrics import extractor



def main():
    """ Main entry point to compute features for the training-set """

    ########################
    # DATA CREATED BEFORE  #
    ########################
    # 1) load ChangeDistiller output for current project

    # 2) load tf-idf matrix of considered commit-messages

    # 3) load Change-Metrics of each considered file

    # 4) load preprocess-dataset
    preprocess_data = pd.read_csv('preprocess_dataset/dataset.csv', skiprows=1)

    ############################
    # COMPUTE METRICS FOR FILE #
    ############################
    # list() of list() of features
    feature_rows = list()
    # for each file in preprocess-dataset
    for record in preprocess_data:
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

        # 5) fetch patch of file & fetch patch of previous patchset/base

        # 6) compute Code-Metrics -> save features
        code_metrics = extractor.createLog(record)
    
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
    print('> finished analyzing')

if __name__ == "__main__":
    main()
