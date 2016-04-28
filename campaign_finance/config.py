import sys
import os

from collections import OrderedDict


MAIN_DIR = os.getcwd()                  # main project directory
RAW_DIR = MAIN_DIR + '/data_raw/'       # directory for raw data files
MASTER_DIR = MAIN_DIR + '/data_master/' # directory for transformed master data files

# FEC download page: http://www.fec.gov/finance/disclosure/ftpdet.shtml
FTP_HOST = 'ftp.fec.gov'


# [START BigQuery config info]

PROJECT_ID = 'w205-project-1272'

DATASET_ID = 'test_data'

TABLE_ID = {
    'committees': ['cm12', 'cm14', 'cm16'],
    'candidates': ['cn12', 'cn14', 'cn16'],
    'indiv_contribs': ['itcont12', 'itcont14', 'itcont16'],
    'comm_contribs': ['itpas212', 'itpas214', 'itpas216'],
    'comm_transfers': ['itpas212', 'itpas214', 'itpas216']
}
# [END BigQuery config info]


# [START globals]

# election cycles
ELECT_YR = ['2012', '2014', '2016']

# political parties to include: Democrats, Republicans, Independents
INCLUDE_PTY = ['DEM', 'REP', 'IND']     

# transaction types to include
INCLUDE_TRANS = [           
    '10', '11', '12', '13',         
    '15', '15C', '15E',
    '15I', '15T', '15Z',                # contributions from committees, individuals
    '18G', '18H', '18K',
    '18L', '18U', '19',                 # contributions from various other parties
    '24A', '24C', '24E',                # independent expenditures for/against
    '24F', '24G', '24H',
    '24I', '24K',                       # contributions/transfers for various 3rd parties
    '24N', '24P', '24T','24U', '24Z',
    '30', '30T', '30K', '30G',          # Convention Account receipts
    '31', '31T', '31K', '31G',          # Headquarters Account receipts
    '32', '32T', '32K', '32G',          # Recount Account receipts
]
# [END globals]


# [START file metadata]

# dict for candidate and committee file names
# updated daily
CANDCOMM_FILES = {
    # header files
    'head': ['cm_header_file.csv', 'cn_header_file.csv'],

    # unzipped txt files
    'temp': ['cm.txt', 'cn.txt'],

    # zip files and renamed txt files
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

# dict for contribution file names
# updated weekly -> handle separately from candidate/committeee files
CONTRIB_FILES = {
    # header files
    'head': ['indiv_header_file.csv', 'pas2_header_file.csv', 'oth_header_file.csv'],
    
    # unzipped txt files
    'temp': ['itcont.txt', 'itpas2.txt', 'itoth.txt'],

    # zip files and renamed txt files by election cycle
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

# schema with columns to include
SCHEMA_INCLUDE = {
    'candidates': OrderedDict((
        ('CAND_ID', str),
        ('CAND_NAME', str),
        ('CAND_PTY_AFFILIATION', str),
        ('CAND_ELECTION_YR', str),
        ('CAND_OFFICE_ST', str),
        ('CAND_OFFICE', str),
        ('CAND_OFFICE_DISTRICT', str),
        ('CAND_ICI', str),
        ('CAND_STATUS', str),
        ('CAND_PCC', str)
    )),
    'committees': OrderedDict((
        ('CMTE_ID', str),
        ('CMTE_NM', str),
        ('CMTE_DSGN', str),
        ('CMTE_TP', str),
        ('CMTE_PTY_AFFILIATION', str),
        ('ORG_TP', str),
        ('CONNECTED_ORG_NM', str),
        ('CAND_ID', str)
    )),
    'indiv_contribs': OrderedDict((
        ('CMTE_ID', str),
        ('AMNDT_IND', str),
        ('RPT_TP', str),
        ('TRANSACTION_PGI', str),
        ('TRANSACTION_TP', str),
        ('ENTITY_TP', str),
        ('NAME', str),
        ('CITY', str),
        ('STATE', str),
        ('ZIP_CODE', str),
        ('EMPLOYER', str),
        ('OCCUPATION', str),
        ('TRANSACTION_DT', str),
        ('TRANSACTION_AMT', float),
        ('OTHER_ID', str),
        ('MEMO_CD', str)
    )),
    'comm_contribs': OrderedDict((
        ('CMTE_ID', str),
        ('AMNDT_IND', str),
        ('RPT_TP', str),
        ('TRANSACTION_PGI', str),
        ('TRANSACTION_TP', str),
        ('ENTITY_TP', str),
        ('NAME', str),
        ('CITY', str),
        ('STATE', str),
        ('ZIP_CODE', str),
        ('TRANSACTION_DT', str),
        ('TRANSACTION_AMT', float),
        ('OTHER_ID', str),
        ('CAND_ID', str),
        ('MEMO_CD', str)
    )),
    'comm_transfers': OrderedDict((
        ('CMTE_ID', str),
        ('AMNDT_IND', str),
        ('RPT_TP', str),
        ('TRANSACTION_PGI', str),
        ('TRANSACTION_TP', str),
        ('ENTITY_TP', str),
        ('NAME', str),
        ('CITY', str),
        ('STATE', str),
        ('ZIP_CODE', str),
        ('EMPLOYER', str),
        ('OCCUPATION', str),
        ('TRANSACTION_DT', str),
        ('TRANSACTION_AMT', float),
        ('OTHER_ID', str),
        ('MEMO_CD', str)
    ))
}

# schema with all columns from raw data
SCHEMA_ALL = {
    'candidates': OrderedDict((
        ('CAND_ID', str),
        ('CAND_NAME', str),
        ('CAND_PTY_AFFILIATION', str),
        ('CAND_ELECTION_YR', str),
        ('CAND_OFFICE_ST', str),
        ('CAND_OFFICE', str),
        ('CAND_OFFICE_DIstr)ICT', str),
        ('CAND_ICI', str),
        ('CAND_STATUS', str),
        ('CAND_PCC', str),
        ('CAND_ST1', str),
        ('CAND_ST2', str),
        ('CAND_CITY', str),
        ('CAND_ST', str),
        ('CAND_ZIP', str)
    )),
    'committees': OrderedDict((
        ('CMTE_ID', str),
        ('CMTE_NM', str),
        ('TRES_NM', str),
        ('CMTE_ST1', str),
        ('CMTE_ST2', str),
        ('CMTE_CITY', str),
        ('CMTE_ST', str),
        ('CMTE_ZIP', str),
        ('CMTE_DSGN', str),
        ('CMTE_TP', str),
        ('CMTE_PTY_AFFILIATION', str),
        ('CMTE_FILING_FREQ', str),
        ('ORG_TP', str),
        ('CONNECTED_ORG_NM', str),
        ('CAND_ID', str)
    )),
    'indiv_contribs': OrderedDict((
        ('CMTE_ID', str),
        ('AMNDT_IND', str),
        ('RPT_TP', str),
        ('TRANSACTION_PGI', str),
        ('IMAGE_NUM', str),
        ('TRANSACTION_TP', str),
        ('ENTITY_TP', str),
        ('NAME', str),
        ('CITY', str),
        ('STATE', str),
        ('ZIP_CODE', str),
        ('EMPLOYER', str),
        ('OCCUPATION', str),
        ('TRANSACTION_DT', str),
        ('TRANSACTION_AMT', float),
        ('OTHER_ID', str),
        ('TRAN_ID', str),
        ('FILE_NUM', str),
        ('MEMO_CD', str),
        ('MEMO_TEXT', str),
        ('SUB_ID', str)
    )),
    'comm_contribs': OrderedDict((
        ('CMTE_ID', str),
        ('AMNDT_IND', str),
        ('RPT_TP', str),
        ('TRANSACTION_PGI', str),
        ('IMAGE_NUM', str),
        ('TRANSACTION_TP', str),
        ('ENTITY_TP', str),
        ('NAME', str),
        ('CITY', str),
        ('STATE', str),
        ('ZIP_CODE', str),
        ('EMPLOYER', str),
        ('OCCUPATION', str),
        ('TRANSACTION_DT', str),
        ('TRANSACTION_AMT', float),
        ('OTHER_ID', str),
        ('CAND_ID', str),
        ('TRAN_ID', str),
        ('FILE_NUM', str),
        ('MEMO_CD', str),
        ('MEMO_TEXT', str),
        ('SUB_ID', str)
    )),
    'comm_transfers': OrderedDict((
        ('CMTE_ID', str),
        ('AMNDT_IND', str),
        ('RPT_TP', str),
        ('TRANSACTION_PGI', str),
        ('IMAGE_NUM', str),
        ('TRANSACTION_TP', str),
        ('ENTITY_TP', str),
        ('NAME', str),
        ('CITY', str),
        ('STATE', str),
        ('ZIP_CODE', str),
        ('EMPLOYER', str),
        ('OCCUPATION', str),
        ('TRANSACTION_DT', str),
        ('TRANSACTION_AMT', float),
        ('OTHER_ID', str),
        ('TRAN_ID', str),
        ('FILE_NUM', str),
        ('MEMO_CD', str),
        ('MEMO_TEXT', str),
        ('SUB_ID', str)
    ))
}
# [END file metadata]
