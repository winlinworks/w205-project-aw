import sys
import os


HOST = 'ftp.fec.gov'

MAIN_DIR = os.getcwd()                  # main project directory
RAW_DIR = MAIN_DIR + '/data_raw/'       # directory for raw data files
MASTER_DIR = MAIN_DIR + '/data_master/' # directory for transformed master data files



INCLUDE_PTY = ['DEM', 'REP', 'IND']     # include Democrats, Republicans, Independents

INCLUDE_TRANS = [           # transaction types to include
    '10', '11', '12', '13',         
    '15', '15C', '15E', '15I', '15T', '15Z',    # contributions from committees, individuals
    '18G', '18H', '18K', '18L', '18U', '19',    # contributions from various other parties
    '24A', '24C', '24E',                # independent expenditures for/against
    '24F', '24G', '24H', '24I', '24K',  # contributions/transfers between various 3rd parties
    '24N', '24P', '24T', '24U', '24Z',
    '30', '30T', '30K', '30G',          # Convention Account receipts
    '31', '31T', '31K', '31G',          # Headquarters Account receipts
    '32', '32T', '32K', '32G',          # Recount Account receipts
]


###### BigQuery info

PROJECT_ID = 'w205-project-1272'
DATASET_ID = 'test_data'
TABLE_ID = ['committee', 'candidate', 'indiv_contrib', 'comm_contrib', 'comm_transfers']

# TABLE_ID = {'cm': ['cm12', 'cm14', 'cm16'],
#             'cn': ['cn12', 'cn14', 'cn16'],
#             'itcont': ['itcont12', 'itcont14', 'itcont16'],
#             'itpas2': ['itpas212', 'itpas214', 'itpas216']}

ELECT_YR = ['2012', '2014', '2016']





###### FEC file names - more info at http://www.fec.gov/finance/disclosure/ftpdet.shtml

# dict for candidate and committee files; updated daily
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

# dict for contribution files; updated weekly, so separate from candidate/committee files
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


# columns to include
HEADERS = {
    'candidate': {      # for cnXX.txt files
        'all': [
            'CAND_ID', 'CAND_NAME', 'CAND_PTY_AFFILIATION', 'CAND_ELECTION_YR',
            'CAND_OFFICE_ST', 'CAND_OFFICE', 'CAND_OFFICE_DISTRICT', 'CAND_ICI',
            'CAND_STATUS', 'CAND_PCC', 'CAND_ST1','CAND_ST2', 'CAND_CITY',
            'CAND_ST', 'CAND_ZIP'
        ],
        'include': [    # remove CAND_ST1, CAND_ST2, CAND_CITY, CAND_ST, CAND_ZIP
            'CAND_ID', 'CAND_NAME', 'CAND_PTY_AFFILIATION', 'CAND_ELECTION_YR',
            'CAND_OFFICE_ST', 'CAND_OFFICE', 'CAND_OFFICE_DISTRICT', 'CAND_ICI',
            'CAND_STATUS', 'CAND_PCC'
        ]
    },
    'committee': {      # for cmXX.txt files
        'all': [
            'CMTE_ID', 'CMTE_NM', 'TRES_NM', 'CMTE_ST1', 'CMTE_ST2', 'CMTE_CITY',
            'CMTE_ST', 'CMTE_ZIP', 'CMTE_DSGN', 'CMTE_TP', 'CMTE_PTY_AFFILIATION',
            'CMTE_FILING_FREQ', 'ORG_TP', 'CONNECTED_ORG_NM', 'CAND_ID'
        ],
        'include': [    # remove TRES_NM, CMTE_ST1, CMTE_ST2, CMTE_CITY, CMTE_ST, CMTE_ZIP, CMTE_FILING_FREQ
            'CMTE_ID', 'CMTE_NM', 'CMTE_DSGN', 'CMTE_TP', 'CMTE_PTY_AFFILIATION',
            'ORG_TP', 'CONNECTED_ORG_NM', 'CAND_ID'
        ]
    },
    'indiv_contrib': {  # for itcontXX.txt files
        'all': [
            'CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'IMAGE_NUM',
            'TRANSACTION_TP', 'ENTITY_TP', 'NAME', 'CITY', 'STATE', 'ZIP_CODE',
            'EMPLOYER', 'OCCUPATION', 'TRANSACTION_DT', 'TRANSACTION_AMT',
            'OTHER_ID', 'TRAN_ID', 'FILE_NUM', 'MEMO_CD', 'MEMO_TEXT', 'SUB_ID'
        ],
        'include': [
            'CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'TRANSACTION_TP',
            'ENTITY_TP','NAME', 'CITY', 'STATE', 'ZIP_CODE', 'EMPLOYER', 'OCCUPATION',
            'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID', 'MEMO_CD'
        ]
    },
    'comm_contrib': {   # for itpas2XX.txt files
        'all': [
            'CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'IMAGE_NUM',
            'TRANSACTION_TP', 'ENTITY_TP', 'NAME', 'CITY', 'STATE', 'ZIP_CODE',
            'EMPLOYER', 'OCCUPATION', 'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID',
            'CAND_ID', 'TRAN_ID', 'FILE_NUM', 'MEMO_CD', 'MEMO_TEXT', 'SUB_ID'
        ],
        'include': [    # remove IMAGE_NUM, TRAN_ID, FILE_NUM, MEMO_TEXT, SUB_ID
            'CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'TRANSACTION_TP',
            'ENTITY_TP','NAME', 'CITY', 'STATE', 'ZIP_CODE', 'TRANSACTION_DT',
            'TRANSACTION_AMT', 'OTHER_ID', 'CAND_ID', 'MEMO_CD'
        ]
    },
    'comm_transfers': {     # for itothXX.txt files
        'all': [
            'CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'IMAGE_NUM',
            'TRANSACTION_TP', 'ENTITY_TP', 'NAME', 'CITY', 'STATE', 'ZIP_CODE',
            'EMPLOYER', 'OCCUPATION', 'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID',
            'TRAN_ID', 'FILE_NUM', 'MEMO_CD', 'MEMO_TEXT', 'SUB_ID'
        ],
        'include': [
            'CMTE_ID', 'AMNDT_IND', 'RPT_TP', 'TRANSACTION_PGI', 'TRANSACTION_TP',
            'ENTITY_TP','NAME', 'CITY', 'STATE', 'ZIP_CODE', 'EMPLOYER', 'OCCUPATION',
            'TRANSACTION_DT', 'TRANSACTION_AMT', 'OTHER_ID', 'MEMO_CD'
        ]
    },
}

###### WORK IN PROGRESS

# dict for classification codes and descriptions (WIP); (k, v) = (code, description)
CLASS_CODES = {
    'AMNDT_IND': {},
    'CAND_ICI': {},
    'CAND_STATUS': {},
    'CMTE_DSGN': {},
    'CMTE_FILING_FREQ': {},
    'CMTE_TP': {},
    'ENTITY_TP': {},
    'ORG_TP': {},
    'OFFICE': {},
    'RPT_TP': {},
    'TRANSACTION_PGI': {},
    'TRANSACTION_TP': {}
}
