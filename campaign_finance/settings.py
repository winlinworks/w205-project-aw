import sys
import os


HOST = 'ftp.fec.gov'

PROJ_DIR = os.getcwd()                  # main project directory
RAW_DIR = PROJ_DIR + '/data_raw'        # directory for raw data files
MASTER_DIR = PROJ_DIR + '/data_master'  # directory for transformed master data files

ELECT_YR = ['2012', '2014', '2016']

# dict for candidate and committee files

CANDCOMM_FILES = {
    'head': ['cm_header_file.csv', 'cn_header_file.csv'],
    'txt': ['cm.txt', 'cn.txt'],
    '2016': ['cm16.zip', 'cn16.zip'],
    '2014': ['cm14.zip', 'cn14.zip'],
    '2012': ['cm12.zip', 'cn12.zip']
}


# dict for contribution files

CONTRIB_FILES = {
    'head': ['indiv_header_file.csv', 'pas2_header_file.csv', 'oth_header_file.csv'],
    'txt': ['itcont.txt', 'itpas2.txt', 'itoth.txt'],
    '2016': ['indiv16.zip', 'pas216.zip', 'oth16.zip'],
    '2014': ['indiv14.zip', 'pas214.zip', 'oth14.zip'],
    '2012': ['indiv12.zip', 'pas212.zip', 'oth12.zip'],
}

CODE_FIELDS = [
    'amndt_ind',
    'cand_ici',
    'cand_status',
    'cmte_dsgn',
    'cmte_filing_freq',
    'cmte_tp',
    'entity_tp',
    'org_tp',
    'office',
    'rpt_tp',
    'transaction_pgi',
    'transaction_tp'
]