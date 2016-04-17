import sys, os
import pandas as pd


CURR_DIR = os.getcwd()              # parent directory where main apps are
DEST_DIR = CURR_DIR + '/data_raw/'  # directory where files will be stored

FILE_STEMS = ['cm', 'cn', 'itcont', 'itpas2']


# Candidate Master (cmXX.txt)
# 1. normalize cols: CAND_OFFICE, CAND_ICI, CAND_STATUS, CAND_PTY_AFFILIATION
# 2. delete cols: CAND_ST1, CAND_ST2, CAND_CITY, CAND_ST, CAND_ZIP
# 3. filter rows: CAND_OFFICE = P, CAND_PTY_AFFILIATION = {DEM, REP, IND}

def transformCandidates():
    # read csv into dataframe

    # create new dataframe with selected cols

    # filter rows to relevant elected offices and parties
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
# 3. filter rows: contains CMTE_ID from above, TRANSACTION_TP = {15, 15E, 15C}
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
