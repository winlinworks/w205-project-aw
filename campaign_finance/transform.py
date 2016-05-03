import sys, os
import pandas as pd

from config import *


# [START filterCands]
def filterCandidates(year):
    head = SCHEMA_ALL['candidates']                 # header to read csv
    cols = SCHEMA_INCLUDE['candidates'].keys()      # columns to include in export
    dt = SCHEMA_INCLUDE['candidates']               # data types

    fn = CANDCOMM_FILES[year]['txt'][1]      # get file name
    df = pd.read_table(RAW_DIR + fn, sep='|', dtype=dt, header=None, names=head, index_col=0, usecols=cols)     # read csv into dataframe

    df = df[df['cand_pty_affiliation'].isin(INCLUDE_PTY)]   # filter included party affiliations
    fn = fn[:-4] + '.csv'       # change extension to csv
    df.to_csv(MASTER_DIR + fn, header=None, na_rep='NA')         # save csv to master data folder

    print('-- Processed and saved: %s' % fn)
# [END filterCands]


# [START filterComms]
def filterCommittees(year):
    head = SCHEMA_ALL['committees']                 # header to read csv
    cols = SCHEMA_INCLUDE['committees'].keys()      # columns to include in export
    dt = SCHEMA_INCLUDE['committees']               # data types

    fn = CANDCOMM_FILES[year]['txt'][0]      # get file name
    df = pd.read_table(RAW_DIR + fn, sep='|', dtype=dt, header=None, names=head, index_col=0, usecols=cols)     # read csv into dataframe

    # *** no filter for committee classifications

    fn = fn[:-4] + '.csv'       # change extension to csv
    df.to_csv(MASTER_DIR + fn, header=None, na_rep='NA')         # save csv to master data folder

    print('-- Processed and saved: %s' % fn)
# [END filterComms]


# [START filterIndivCons]
def filterIndivContribs(year):
    head = SCHEMA_ALL['indiv_contribs']                 # header to read csv
    cols = SCHEMA_INCLUDE['indiv_contribs'].keys()      # columns to include in export
    dt = SCHEMA_INCLUDE['indiv_contribs']               # data types

    fn = CONTRIB_FILES[year]['txt'][0]      # get file name
    df = pd.read_table(RAW_DIR + fn, sep='|', dtype=dt, header=None, names=head, index_col=15, usecols=cols)     # read csv into dataframe
    
    df = df[df['transaction_tp'].isin(INCLUDE_TRANS)]   # filter transaction types
    fn = fn[:-4] + '.csv'       # change extension to csv
    df.to_csv(MASTER_DIR + fn, header=None, na_rep=0)             # save csv to master data folder

    print('-- Processed and saved: %s' % fn)
# [END filterIndivCons]


# [START filterCommCons]
def filterCommContribs(year):
    head = SCHEMA_ALL['comm_contribs']                  # header to read csv
    cols = SCHEMA_INCLUDE['comm_contribs'].keys()       # columns to include in export
    dt = SCHEMA_INCLUDE['comm_contribs']                # data types

    fn = CONTRIB_FILES[year]['txt'][1]      # get file name
    df = pd.read_table(RAW_DIR + fn, sep='|', dtype=dt, header=None, names=head, index_col=14, usecols=cols)     # read csv into dataframe
    
    df = df[df['transaction_tp'].isin(INCLUDE_TRANS)]   # filter transaction types
    fn = fn[:-4] + '.csv'       # change extension to csv
    df.to_csv(MASTER_DIR + fn, header=None, na_rep='NA')             # save csv to master data folder

    print('-- Processed and saved: %s' % fn)
# [END filterCommCons]


# [START filterAll]
def filterAll():
    # for each election cycle
    for year in ELECT_YR:
        print('Filtering candidate and committee data for %s...' % year)

        filterCandidates(year)      # filter candidates
        filterCommittees(year)      # filter committees

        print('Filtering contribution and transfer data for %s...' % year)

        filterIndivContribs(year)   # filter individual contributions to candidates
        filterCommContribs(year)    # filter committee contributions to candidates
# [END filterAll]

if __name__ == '__main__':

    filterAll()

