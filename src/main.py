import pandas as pd
import numpy as np


def main():
    """ Main entry point to compute features """


    ########################
    # DATA CREATED BEFORE  #
    ########################
    # 1) load ChangeDistiller output for current project

    # 2) load tf-idf matrix of considered commit-messages

    # 3) load Change-Metrics of each considered file

    # 4) load preprocess-dataset

    ############################
    # COMPUTE METRICS FOR FILE #
    ############################
    # for each file in preprocess-dataset
        # list() of list() of features
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

        # 7) compute checkstyle-metrics -> save features

        # 8) compute pmd-metrics -> save features

        # 9) lookup change-metrics -> save features

        # 10) lookup tf-idf row -> save features

        # 11) compute ck-metrics -> save features

        # 12) lookup ChangeDistiller types -> save features

        # 13) extract labels --> save

        # 14) add each feature list to features

    # 15) print each feature-row into a data-set

    pass


if __name__ == 'main':
    main()
