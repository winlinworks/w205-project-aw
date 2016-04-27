import sys
import os
import pandas as pd

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials

from settings import *

# APPROACH

# Method 1: normalize/join data locally, then load to BQ
# - Use pandas for more intuitive workflow
# - Filter future data before loading to reduce size of loads
# - Can merge on 2 cols/indices

# Method 2: load all raw/denormalized data to BQ, then normalize/join data in BQ


# IMPLEMENTATION

# With dataframes df1, df2
# - Merge: pd.merge(df1, df2, on='field', how='left')
# - Join: df1.set_index('field', inplace=True); df1.join(df2)

# Candidate Master (cmXX.txt)
# 1. filter out cols: CAND_ST1, CAND_ST2, CAND_CITY, CAND_ST, CAND_ZIP
# 2. filter rows (?):
#   - CAND_OFFICE = P
#   - CAND_PTY_AFFILIATION = DEM, REP, IND
# 3. normalize cols: CAND_OFFICE, CAND_ICI, CAND_STATUS, CAND_PTY_AFFILIATION


def filterCands():

    os.chdir(RAW_DIR)        # change to raw data folder

    fn = CANDCOMM_FILES['head'][1]  # get header file name
    colnames = pd.read_csv(fn)      # read header file
    cols = range(0,10)              # set col array

    fn = 'cn16.txt'
    df = pd.read_table(fn, sep='|', header=None, names=colnames, index_col=0, usecols=cols)  # read csv into dataframe, set headers, set index

    os.chdir(MASTER_DIR)        # change to raw data folder

    df.to_csv(fn, header=True)  # save csv to new data directory


# Committee Master (cnXX.txt)
# 1. filter cols: TRES_NM, CMTE_ST1, CMTE_ST2, CMTE_CITY, CMTE_ST, CMTE_ZIP, CMTE_FILING_FREQ, CONNECTED_ORG_NM
# 2. normalize cols: CMTE_DSGN, CMTE_TP, CMTE_PTY_AFFILIATION, ORG_TP
# 3. filter rows (?): CMTE_ID = CAND_PCC from above
def transformComms():
    print 'Hello'
    # read csv into dataframe

    # create new dataframe with selected cols

    # filter rows to relevant candidates



# Contributions by Individuals (itcontXX.txt)
# Contributions to Candidates from Committees (itpas2XX.txt)
# 1. normalize cols: RPT_TP, TRANSACTION_TP, ENTITY_TP
# 2. filter cols: IMAGE_NUM, TRAN_ID, FILE_NUM, MEMO_TEXT, SUB_ID
# 3. filter rows (?):
#   - contains CMTE_ID from above
#   - TRANSACTION_TP = 15, 15E, 15C, 24K, 24E, 24A
# 4. transform values:
#   - convert TRANSACTION_DT string to "mm-dd-yyyy" date format
#   - standardize EMPLOYER string
#   - group EMPLOYER into new col INDUSTRY

def transformContribs():
    print 'Hello'
    # read csv into dataframe

    # create new dataframe with selected cols

    # filter contribs to relevant transaction types



if __name__ == '__main__':
    transformCands()