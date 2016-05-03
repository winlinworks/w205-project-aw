import sys
import os

from collections import OrderedDict


MAIN_DIR = os.getcwd()                  # main project directory
RAW_DIR = MAIN_DIR + '/data_raw/'       # directory for raw data files
MASTER_DIR = MAIN_DIR + '/data_master/' # directory for transformed master data files

# FEC download page: http://www.fec.gov/finance/disclosure/ftpdet.shtml
FTP_HOST = 'ftp.fec.gov'


# BigQuery config info

PROJ_ID = 'campaign-finance-1295'
# DATA_ID = 'demo205'
# STORE_ID = 'demo205'

DATA_ID = 'test205'
STORE_ID = 'test205'

# TABLE_ID = {
#     'committees': ['cm12', 'cm14', 'cm16'],
#     'candidates': ['cn12', 'cn14', 'cn16'],
#     'indiv_contribs': ['itcont12', 'itcont14', 'itcont16'],
#     'comm_contribs': ['itpas212', 'itpas214', 'itpas216'],
#     'comm_transfers': ['itpas212', 'itpas214', 'itpas216']
# }



# election cycles
ELECTION_YEARS = ['2012', '2014', '2016']

FILE_TYPES = {
    'cm': 'cm',
    'cn': 'cn',
    'indiv': 'itcont',
    'pas2': 'itpas2',
    'oth': 'itoth'
}

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


# schema for raw data
SCHEMA_RAW = {
    'cn': OrderedDict((
        ('cand_id', str),
        ('cand_name', str),
        ('cand_pty_affiliation', str),
        ('cand_election_yr', str),
        ('cand_office_st', str),
        ('cand_office', str),
        ('cand_office_district', str),
        ('cand_ici', str),
        ('cand_status', str),
        ('cand_pcc', str),
        ('cand_st1', str),
        ('cand_st2', str),
        ('cand_city', str),
        ('cand_st', str),
        ('cand_zip', str)
    )),
    'cm': OrderedDict((
        ('cmte_id', str),
        ('cmte_nm', str),
        ('tres_nm', str),
        ('cmte_st1', str),
        ('cmte_st2', str),
        ('cmte_city', str),
        ('cmte_st', str),
        ('cmte_zip', str),
        ('cmte_dsgn', str),
        ('cmte_tp', str),
        ('cmte_pty_affiliation', str),
        ('cmte_filing_freq', str),
        ('org_tp', str),
        ('connected_org_nm', str),
        ('cand_id', str)
    )),
    'itcont': OrderedDict((
        ('cmte_id', str),
        ('amndt_ind', str),
        ('rpt_tp', str),
        ('transaction_pgi', str),
        ('image_num', str),
        ('transaction_tp', str),
        ('entity_tp', str),
        ('name', str),
        ('city', str),
        ('state', str),
        ('zip_code', str),
        ('employer', str),
        ('occupation', str),
        ('transaction_dt', str),
        ('transaction_amt', int),
        ('other_id', str),
        ('tran_id', str),
        ('file_num', str),
        ('memo_cd', str),
        ('memo_text', str),
        ('sub_id', str)
    )),
    'itpas2': OrderedDict((
        ('cmte_id', str),
        ('amndt_ind', str),
        ('rpt_tp', str),
        ('transaction_pgi', str),
        ('image_num', str),
        ('transaction_tp', str),
        ('entity_tp', str),
        ('name', str),
        ('city', str),
        ('state', str),
        ('zip_code', str),
        ('employer', str),
        ('occupation', str),
        ('transaction_dt', str),
        ('transaction_amt', int),
        ('other_id', str),
        ('cand_id', str),
        ('tran_id', str),
        ('file_num', str),
        ('memo_cd', str),
        ('memo_text', str),
        ('sub_id', str)
    )),
    'itoth': OrderedDict((
        ('cmte_id', str),
        ('amndt_ind', str),
        ('rpt_tp', str),
        ('transaction_pgi', str),
        ('image_num', str),
        ('transaction_tp', str),
        ('entity_tp', str),
        ('name', str),
        ('city', str),
        ('state', str),
        ('zip_code', str),
        ('employer', str),
        ('occupation', str),
        ('transaction_dt', str),
        ('transaction_amt', int),
        ('other_id', str),
        ('tran_id', str),
        ('file_num', str),
        ('memo_cd', str),
        ('memo_text', str),
        ('sub_id', str)
    ))
}


# schema for transformed data
SCHEMA_NEW = {
    'cn': OrderedDict((
        ('cand_id', str),
        ('cand_name', str),
        ('cand_pty_affiliation', str),
        ('cand_election_yr', int),
        ('cand_office_st', str),
        ('cand_office', str),
        ('cand_office_district', str),
        ('cand_ici', str),
        ('cand_status', str),
        ('cand_pcc', str)
    )),
    'cm': OrderedDict((
        ('cmte_id', str),
        ('cmte_nm', str),
        ('cmte_dsgn', str),
        ('cmte_tp', str),
        ('cmte_pty_affiliation', str),
        ('org_tp', str),
        ('connected_org_nm', str),
        ('cand_id', str)
    )),
    'itcont': OrderedDict((
        ('cmte_id', str),
        ('amndt_ind', str),
        ('rpt_tp', str),
        ('transaction_pgi', str),
        ('transaction_tp', str),
        ('entity_tp', str),
        ('name', str),
        ('city', str),
        ('state', str),
        ('zip_code', str),
        ('employer', str),
        ('occupation', str),
        ('transaction_dt', str),
        ('transaction_amt', int),
        ('other_id', str),
        ('tran_id', str),
        ('memo_cd', str)
    )),
    'itpas2': OrderedDict((
        ('cmte_id', str),
        ('amndt_ind', str),
        ('rpt_tp', str),
        ('transaction_pgi', str),
        ('transaction_tp', str),
        ('entity_tp', str),
        ('name', str),
        ('city', str),
        ('state', str),
        ('zip_code', str),
        ('employer', str),
        ('occupation', str),
        ('transaction_dt', str),
        ('transaction_amt', int),
        ('other_id', str),
        ('cand_id', str),
        ('tran_id', str),
        ('memo_cd', str)
    )),
    'itoth': OrderedDict((
        ('cmte_id', str),
        ('amndt_ind', str),
        ('rpt_tp', str),
        ('transaction_pgi', str),
        ('transaction_tp', str),
        ('entity_tp', str),
        ('name', str),
        ('city', str),
        ('state', str),
        ('zip_code', str),
        ('employer', str),
        ('occupation', str),
        ('transaction_dt', str),
        ('transaction_amt', int),
        ('other_id', str),
        ('tran_id', str),
        ('memo_cd', str)
    ))
}

# dict for classification codes and descriptions (WIP)
# (k, v) = (code, description)
CLASS_CODES = {
    'amndt_ind': {},
    'cand_ici': {},
    'cand_status': {},
    'cmte_dsgn': {},
    'cmte_filing_freq': {},
    'cmte_tp': {},
    'entity_tp': {},
    'office': {},
    'org_tp': {},
    'pty_affiliation': {},
    'rpt_tp': {},
    'transaction_pgi': {},
    'transaction_tp': {}
}
