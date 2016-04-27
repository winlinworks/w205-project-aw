import sys
import os


HOST = 'ftp.fec.gov'

MAIN_DIR = os.getcwd()                  # main project directory
RAW_DIR = MAIN_DIR + '/data_raw/'       # directory for raw data files
MASTER_DIR = MAIN_DIR + '/data_master/' # directory for transformed master data files

ELECT_YR = ['2012', '2014', '2016']


###### Globals for parsing files from FEC site

# dict for candidate and committee files
CANDCOMM_FILES = {
    'head': ['cm_header_file.csv', 'cn_header_file.csv'],
    'temp': ['cm.txt', 'cn.txt'],
    '2016': {
        'zip': ['cm16.zip', 'cn16.zip'],
        'txt': ['cm16.txt', 'cn16.txt']
    },
    '2014': {
        'zip': ['cm14.zip', 'cn14.zip'],
        'txt': ['cm14.txt', 'cn14.txt']
    },
    '2012': {
        'zip': ['cm12.zip', 'cn12.zip'],
        'txt': ['cm12.txt', 'cn12.txt']
    }
}

# dict for contribution files
CONTRIB_FILES = {
    'head': ['indiv_header_file.csv', 'pas2_header_file.csv', 'oth_header_file.csv'],
    'temp': ['itcont.txt', 'itpas2.txt', 'itoth.txt'],
    '2016': {
        'zip': ['indiv16.zip', 'pas216.zip', 'oth16.zip'],
        'txt': ['itcont16.txt', 'itpas216.txt', 'itoth16.txt']
    },
    '2014': {
        'zip': ['indiv14.zip', 'pas214.zip', 'oth14.zip'],
        'txt': ['itcont14.txt', 'itpas214.txt', 'itoth14.txt']
    },
    '2012': {
        'zip': ['indiv12.zip', 'pas212.zip', 'oth12.zip'],
        'txt': ['itcont12.txt', 'itpas212.txt', 'itoth12.txt']
    }
}

# code columns to normalize (?)
CODES = ['AMNDT_IND', 'CAND_ICI', 'CAND_STATUS', 'CMTE_DSGN', 'CMTE_FILING_FREQ', 'CMTE_TP', 'ENTITY_TP', 'ORG_TP', 'OFFICE', 'RPT_TP', 'TRANSACTION_PGI', 'TRANSACTION_TP']


# columns to include
HEADERS = {
    'cm': {
        'head': ['CMTE_ID', 'CMTE_NM', 'TRES_NM', 'CMTE_ST1', 'CMTE_ST2', 'CMTE_CITY', 'CMTE_ST', 'CMTE_ZIP', 'CMTE_DSGN', 'CMTE_TP', 'CMTE_PTY_AFFILIATION', 'CMTE_FILING_FREQ', 'ORG_TP', 'CONNECTED_ORG_NM', 'CAND_ID'],
        'keep': ['CMTE_ID', 'CMTE_NM', 'CMTE_DSGN', 'CMTE_TP', 'CMTE_PTY_AFFILIATION', 'ORG_TP', 'CONNECTED_ORG_NM', 'CAND_ID']
    },
    'cn': {
        'head': ['CAND_ID', 'CAND_NAME', 'CAND_PTY_AFFILIATION', 'CAND_ELECTION_YR', 'CAND_OFFICE_ST', 'CAND_OFFICE', 'CAND_OFFICE_DISTRICT', 'CAND_ICI', 'CAND_STATUS', 'CAND_PCC', 'CAND_ST1','CAND_ST2', 'CAND_CITY', 'CAND_ST', 'CAND_ZIP'],
        'keep': ['CAND_ID', 'CAND_NAME', 'CAND_PTY_AFFILIATION', 'CAND_ELECTION_YR', 'CAND_OFFICE_ST', 'CAND_OFFICE', 'CAND_OFFICE_DISTRICT', 'CAND_ICI', 'CAND_STATUS', 'CAND_PCC']
    },
    'itcont': {
        'head': ['CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'IMAGE_NUM', 'TRANSACTION_TP', 'ENTITY_TP', 'NAME', 'CITY', 'STATE', 'ZIP_CODE', 'EMPLOYER', 'OCCUPATION', 'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID', 'TRAN_ID', 'FILE_NUM', 'MEMO_CD', 'MEMO_TEXT', 'SUB_ID'],
        'keep': ['CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'TRANSACTION_TP', 'ENTITY_TP','NAME', 'CITY', 'STATE', 'ZIP_CODE', 'EMPLOYER', 'OCCUPATION', 'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID', 'MEMO_CD']
    },
    'itoth': {
        'head': ['CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'IMAGE_NUM', 'TRANSACTION_TP', 'ENTITY_TP', 'NAME', 'CITY', 'STATE', 'ZIP_CODE', 'EMPLOYER', 'OCCUPATION', 'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID', 'TRAN_ID', 'FILE_NUM', 'MEMO_CD', 'MEMO_TEXT', 'SUB_ID'],
        'keep': ['CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'TRANSACTION_TP', 'ENTITY_TP','NAME', 'CITY', 'STATE', 'ZIP_CODE', 'EMPLOYER', 'OCCUPATION', 'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID', 'MEMO_CD']
    },
    'itpas2': {
        'head': ['CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'IMAGE_NUM', 'TRANSACTION_TP', 'ENTITY_TP', 'NAME', 'CITY', 'STATE', 'ZIP_CODE', 'EMPLOYER', 'OCCUPATION', 'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID', 'CAND_ID', 'TRAN_ID', 'FILE_NUM', 'MEMO_CD', 'MEMO_TEXT', 'SUB_ID'],
        'keep': ['CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'TRANSACTION_TP', 'ENTITY_TP','NAME', 'CITY', 'STATE', 'ZIP_CODE', 'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID', 'CAND_ID', 'MEMO_CD']
    }
}


INCLUDE_PTY = ['DEM', 'REP', 'IND']                             # political parties to include
INCLUDE_TRANS = ['15', '15E', '15C', '24K', '24E', '24A']       # transaction types to include


###### BigQuery info

PROJECT_ID = 'w205-project-1272'

DATASET_ID = 'test_data2'

TABLE_ID = ['cm', 'cn', 'itcont', 'itpas2', 'itoth']

# TABLE_ID = {'cm': ['cm12', 'cm14', 'cm16'],
#             'cn': ['cn12', 'cn14', 'cn16'],
#             'itcont': ['itcont12', 'itcont14', 'itcont16'],
#             'itpas2': ['itpas212', 'itpas214', 'itpas216']}