import sys, os
import pandas as pd

from config import *


# [START reduce_cols]
def reduce_cols(txt_type, year):
    schema_raw = SCHEMA_RAW[txt_type]   # header to read csv
    schema_new = SCHEMA_NEW[txt_type]   # data types

    rawfile = txt_type + year[2:] + '.txt'      # get file name
    df = pd.read_table(RAW_DIR + rawfile, sep='|', header=None, index_col=0, names=schema_raw, dtype=schema_new, usecols=schema_new.keys())     # read csv into dataframe

    newfile = rawfile[:-4] + '.csv'       # change extension to csv
    df.to_csv(MASTER_DIR + newfile, header=None)         # save csv to master data folder

    print('-- Reduced columns: %s -> %s' % (rawfile, newfile))
# [END reduce_cols]


# [START filter_cands]
def filter_cands(year):
    schema_new = SCHEMA_NEW['cn']   # data types
    file = 'cn%s.csv' % year[2:]
    df = pd.read_csv(MASTER_DIR + file, header=None, index_col=0, names=schema_new, dtype=schema_new)     # read csv into dataframe
    x = len(df)

    df = df[df['cand_pty_affiliation'].isin(INCLUDE_PTY)]   # filter included party affiliations
    y = len(df)

    df.to_csv(MASTER_DIR + file, header=None)  # save csv to master data folder

    print('-- Filtered candidates: %s (%i -> %i rows)' % (file, x, y))
# [END filter_cands]


# [START filter_indiv_contribs]
def filter_indiv_contribs(year):
    schema_new = SCHEMA_NEW['itcont']   # data types
    file = 'itcont%s.csv' % year[2:]
    df = pd.read_csv(MASTER_DIR + file, header=None, index_col=0, names=schema_new, dtype=schema_new)     # read csv into dataframe
    x = len(df)

    # df = df[df['transaction_tp'].isin(INCLUDE_TRANS)]   # filter transaction types
    y = len(df)

    df.to_csv(MASTER_DIR + file, header=None)  # save csv to master data folder

    print('-- Filtered individual contributions: %s (%i -> %i rows)' % (file, x, y))
# [END filter_indiv_contribs]


# [START filter_comm_contribs]
def filter_comm_contribs(year):
    schema_new = SCHEMA_NEW['itpas2']   # data types
    file = 'itpas2%s.csv' % year[2:]
    df = pd.read_csv(MASTER_DIR + file, header=None, index_col=0, names=schema_new, dtype=schema_new)     # read csv into dataframe
    x = len(df)

    df = df[df['transaction_tp'].isin(INCLUDE_TRANS)]   # filter transaction types
    y = len(df)

    df.to_csv(MASTER_DIR + file, header=None)  # save csv to master data folder

    print('-- Filtered committee contributions: %s (%i -> %i rows)' % (file, x, y))
# [END filter_comm_contribs]


# [START filter_comm_transfers]
def filter_comm_transfers(year):
    schema_new = SCHEMA_NEW['itoth']   # data types
    file = 'itoth%s.csv' % year[2:]
    df = pd.read_csv(MASTER_DIR + file, header=None, index_col=0, names=schema_new, dtype=schema_new)     # read csv into dataframe
    x = len(df)

    df = df[df['transaction_tp'].isin(INCLUDE_TRANS)]   # filter transaction types
    y = len(df)

    df.to_csv(MASTER_DIR + file, header=None)  # save csv to master data folder

    print('-- Filtered committee transfers: %s (%i -> %i rows)' % (file, x, y))
# [END filter_comm_transfers]


# [START transform]
def transform():
    # for each election cycle
    for year in ELECTION_YEARS:
        print('Reducing columns for candidate, committee, and contribution/transfer data for %s...' % year)

        # reduce cols for all file types
        for zip_type, txt_type in FILE_TYPES.items():
            reduce_cols(txt_type, year)

        print('Filtering contribution and transfer data for %s...' % year)

        # filter rows for each file type
        filter_cands(year)
        filter_indiv_contribs(year)
        filter_comm_contribs(year)
        filter_comm_transfers(year)
# [END transform]

if __name__ == '__main__':

    transform()

