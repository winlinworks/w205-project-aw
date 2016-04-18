import sys, os
import pandas as pd

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials


CURR_DIR = os.getcwd()              # parent directory where main apps are
RAW_DIR = CURR_DIR + '/data_raw/'  # directory where files will be stored
NEW_DIR = CURR_DIR + '/data_new/'  # directory where files will be stored

FILE_STEMS = ['cm', 'cn', 'itcont', 'itpas2']

CODE_FIELDS = ['amndt_ind', 'cand_ici', 'cand_status', 'cmte_dsgn', 'cmte_filing_freq', 'cmte_tp', 'entity_tp', 'org_tp', 'office', 'rpt_tp', 'transaction_pgi', 'transaction_tp']
CODE_DICT = {''}


# APPROACH

# Method 1: normalize/join data locally, then load to BQ
# - Use pandas for more intuitive workflow
# - Filter future data before loading to reduce size of loads
# - Can merge on 2 cols/indices

# Method 2: load all raw/denormalized data to BQ, then normalize/join data in BQ


# IMPLEMENTATION

# With dataframs df1, df2
# - Merge: pd.merge(df1, df2, on='field', how='left')
# - Join: df1.set_index('field', inplace=True); df1.join(df2)

# Candidate Master (cmXX.txt)
# 1. normalize cols: CAND_OFFICE, CAND_ICI, CAND_STATUS, CAND_PTY_AFFILIATION
# 2. delete cols: CAND_ST1, CAND_ST2, CAND_CITY, CAND_ST, CAND_ZIP
# 3. filter rows: CAND_OFFICE = P, CAND_PTY_AFFILIATION = {DEM, REP, IND}

def getCodes():
    for fn in os.listdir(DEST_DIR):
        if fn.startswith('cd_'):
            codename = fn[2:-4]


def transformCandidates():
    # read csv into dataframe, set headers, set index
    df = pd.read_csv(filename, names=getHeaders(), index_col=0)

    codes = getCodes()      # get dictionary of codes
    pd.merge(df, currcode, on# merge dataframe with codes

    # create new dataframe with selected cols

    # filter rows to relevant elected offices and parties

    # save csv to new data directory
    df.to_csv(newfilename, header = False)
    return


# Committee Master (cnXX.txt)
# 1. normalize cols: CMTE_DSGN, CMTE_TP, CMTE_PTY_AFFILIATION, ORG_TP
# 2. delete cols: TRES_NM, CMTE_ST1, CMTE_ST2, CMTE_CITY, CMTE_ST, CMTE_ZIP, CMTE_FILING_FREQ, CONNECTED_ORG_NM
# 3. filter rows: CMTE_ID = CAND_PCC from above
def transformCommittees():
    # read csv into dataframe

    # create new dataframe with selected cols

    # filter rows to relevant candidates

    return


# Contributions by Individuals (itcontXX.txt)
# Contributions by Committees (itpas2XX.txt)
# 1. normalize cols: RPT_TP, TRANSACTION_TP, ENTITY_TP
# 2. delete cols: IMAGE_NUM, TRAN_ID, FILE_NUM, MEMO_TEXT, SUB_ID
# 3. filter rows: contains CMTE_ID from above, TRANSACTION_TP = {15, 15E, 15C, 24K, 24E, 24A}
# 4. transform values:
#   - convert TRANSACTION_DT string to "mm-dd-yyyy" date format
#   - standardize EMPLOYER string
#   - group EMPLOYER into new col INDUSTRY

def transformContribs():
    # read csv into dataframe

    # create new dataframe with selected cols

    # filter contribs to relevant transaction types
    return

# 1. normalize cols: RPT_TP, TRANSACTION_TP, ENTITY_TP
# 2. delete cols: IMAGE_NUM, TRAN_ID, FILE_NUM, MEMO_TEXT, SUB_ID
# 3. filter rows: contains CMTE_ID from above
# 4. transform values:
#   - convert TRANSACTION_DT string to "mm-dd-yyyy" date format
#   - standardize EMPLOYER string
#   - group EMPLOYER into new col INDUSTRY
