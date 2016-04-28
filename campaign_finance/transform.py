import sys
import os
import pandas as pd

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials

from settings import *



def filterAll():
    for year in ELECT_YR:
        filterCandidates(year)
        filterCommittees(year)
        filterIndivContribs(year)
        filterCommContribs(year)

###### FILTERING

###### filterCands

def filterCandidates(year):
    head = HEADERS['candidate']['all']       # read header file
    cols = HEADERS['candidate']['include']   # set col names to keep

    fn = CANDCOMM_FILES[year]['txt'][1]     # get candidate text file name
    df = pd.read_table(RAW_DIR + fn, sep='|', header=None, names=head, index_col=0, usecols=cols)  # read csv into dataframe
    df = df[df['CAND_PTY_AFFILIATION'].isin(INCLUDE_PTY)]   # filter included party affiliations

    df.to_csv(MASTER_DIR + fn, header=True)  # save csv to master data folder


###### filterComms

def filterCommittees(year):
    head = HEADERS['committee']['all']       # read header file
    cols = HEADERS['committee']['include']   # set col names to keep

    fn = CANDCOMM_FILES[year]['txt'][0]    # get committee text file name
    df = pd.read_table(RAW_DIR + fn, sep='|', header=None, names=head, index_col=0, usecols=cols)  # read csv into dataframe

    df.to_csv(MASTER_DIR + fn, header=True)  # save csv to master data folder


###### filterIndivContribs

def filterIndivContribs(year):
    head = HEADERS['indiv_contrib']['all']       # read header file
    cols = HEADERS['indiv_contrib']['include']   # set col names to keep

    fn = CONTRIB_FILES[year]['txt'][0]    # get committee text file name
    df = pd.read_table(RAW_DIR + fn, sep='|', header=None, names=head, index_col=0, usecols=cols)  # read csv into dataframe
    df = df[df['TRANSACTION_TP'].isin(INCLUDE_TRANS)]   # filter transaction types

    df.to_csv(MASTER_DIR + fn, header=True)  # save csv to master data folder


###### filterCommContribs

def filterCommContribs(year):
    head = HEADERS['comm_contrib']['all']       # read header file
    cols = HEADERS['comm_contrib']['include']   # set col names to keep

    fn = CONTRIB_FILES[year]['txt'][1]    # get committee text file name
    df = pd.read_table(RAW_DIR + fn, sep='|', header=None, names=head, index_col=0, usecols=cols)  # read csv into dataframe
    df = df[df['TRANSACTION_TP'].isin(INCLUDE_TRANS)]   # filter transaction types

    # filter contribs to relevant transaction types
    df.to_csv(MASTER_DIR + fn, header=True)  # save csv to master data folder


###### transform
#   - convert TRANSACTION_DT string to "mm-dd-yyyy" date format
#   - standardize EMPLOYER string
#   - group EMPLOYER into new col INDUSTRY


###### main

if __name__ == '__main__':
    filterAll()


