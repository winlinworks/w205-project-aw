import sys
import os
import pandas as pd

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials

from config import *


# [START filterAll]
def filterAll():
    # for each election cycle
    for year in ELECT_YR:
        filterCandidates(year)      # filter candidates
        filterCommittees(year)      # filter committees

        filterIndivContribs(year)   # filter individual contributions to candidates
        filterCommContribs(year)    # filter committee contributions to candidates
# [END filterAll]


# [START filterCands]
def filterCandidates(year):
    head = SCHEMA_ALL['candidates']                 # header to read csv
    cols = SCHEMA_INCLUDE['candidates'].keys()      # columns to include in export
    dt = SCHEMA_INCLUDE['candidates']               # data types

    fn = CANDCOMM_FILES[year]['txt'][1]             # get file name
    df = pd.read_table(RAW_DIR + fn, sep='|', dtype=dt, header=None, names=head, index_col=0, usecols=cols)     # read csv into dataframe

    df = df[df['CAND_PTY_AFFILIATION'].isin(INCLUDE_PTY)]   # filter included party affiliations
    df.to_csv(MASTER_DIR + fn, header=True)         # save csv to master data folder
# [END filterCands]


# [START filterComms]
def filterCommittees(year):
    head = SCHEMA_ALL['committees']                 # header to read csv
    cols = SCHEMA_INCLUDE['committees'].keys()      # columns to include in export
    dt = SCHEMA_INCLUDE['committees']               # data types

    fn = CANDCOMM_FILES[year]['txt'][0]             # get file name
    df = pd.read_table(RAW_DIR + fn, sep='|', dtype=dt, header=None, names=head, index_col=0, usecols=cols)     # read csv into dataframe

    # *** no filter for committee classifications
    
    df.to_csv(MASTER_DIR + fn, header=True)         # save csv to master data folder
# [END filterComms]


# [START filterIndivCons]
def filterIndivContribs(year):
    head = SCHEMA_ALL['indiv_contribs']                 # header to read csv
    cols = SCHEMA_INCLUDE['indiv_contribs'].keys()      # columns to include in export
    dt = SCHEMA_INCLUDE['indiv_contribs']               # data types

    fn = CONTRIB_FILES[year]['txt'][0]                  # get file name
    df = pd.read_table(RAW_DIR + fn, sep='|', dtype=dt, header=None, names=head, index_col=0, usecols=cols)     # read csv into dataframe
    
    df = df[df['TRANSACTION_TP'].isin(INCLUDE_TRANS)]   # filter transaction types
    df.to_csv(MASTER_DIR + fn, header=True)             # save csv to master data folder
# [END filterIndivCons]


# [START filterCommCons]
def filterCommContribs(year):
    head = SCHEMA_ALL['comm_contribs']                  # header to read csv
    cols = SCHEMA_INCLUDE['comm_contribs'].keys()       # columns to include in export
    dt = SCHEMA_INCLUDE['comm_contribs']                # data types

    fn = CONTRIB_FILES[year]['txt'][1]                  # get file name
    df = pd.read_table(RAW_DIR + fn, sep='|', dtype=dt, header=None, names=head, index_col=0, usecols=cols)     # read csv into dataframe
    
    df = df[df['TRANSACTION_TP'].isin(INCLUDE_TRANS)]   # filter transaction types
    df.to_csv(MASTER_DIR + fn, header=True)             # save csv to master data folder
# [END filterCommCons]


if __name__ == '__main__':
    filterAll()

