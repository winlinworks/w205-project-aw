import sys
import os

import urllib
import ftplib
from ftplib import FTP

import zipfile

PROJ_DIR = os.getcwd()                  # main project directory
RAW_DIR = PROJ_DIR + '/data_raw'        # directory for raw data files
MASTER_DIR = PROJ_DIR + '/data_master'  # directory for transformed master data files

HOST = 'ftp.fec.gov'

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


##### getCandComms - downloads candidate and committee files and file headers from FEC site

def getCandComms():
    try:
        ftp = FTP(HOST)             # connect to host ftp.fec.gov
        ftp.login()

        os.chdir(RAW_DIR)           # move to raw data directory

        # download files for each year
        for y in ELECT_YR:
            ftp.cwd('/FEC/' + y)      # move to FTP directory matching year
            ftp.retrlines('LIST')     # list files

            # download files
            for fn in CANDCOMM_FILES[y]:
                f = open(fn, 'wb')
                ftp.retrbinary('RETR ' + fn, f.write)
                f.close()

    except ftplib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % fn
        os.unlink(fn)

    ftp.quit()
    os.chdir(PROJ_DIR)      # return to project directory


###### getContribs - downloads contribution files and file headers from FEC site

def getContribs():
    try:
        ftp = FTP(HOST)             # connect to host ftp.fec.gov
        ftp.login()

        os.chdir(RAW_DIR)           # move to raw data directory

        # download files for each year
        for y in ELECT_YR:
            ftp.cwd('/FEC/' + y)      # move to FTP directory matching year
            ftp.retrlines('LIST')     # list files

            # download files
            for fn in CONTRIB_FILES[y]:
                f = open(fn, 'wb')
                ftp.retrbinary('RETR ' + fn, f.write)
                f.close()

    except ftplib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % fn
        os.unlink(fn)

    ftp.quit()
    os.chdir(PROJ_DIR)      # return to project directory


###### getHeaders - downloads file headers from ftp.fec.gov

def getHeaders():
    try:
        ftp = FTP(HOST)             # connect to host ftp.fec.gov
        ftp.login()

        os.chdir(RAW_DIR)           # move to raw data directory

        # download candidate and committee file headers
        for fn in CANDCOMM_FILES['head']:
            url = 'http://www.fec.com/finance/disclosure/metadata/' + fn
            urllib.urlretrieve(url, fn)

        # download contribution file headers
        for fn in CONTRIB_FILES['head']:
            url = 'http://www.fec.com/finance/disclosure/metadata/' + fn
            urllib.urlretrieve(url, fn)

    except ftplib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % fn
        os.unlink(fn)

    ftp.quit()
    os.chdir(PROJ_DIR)      # return to project directory


###### unzipYear - unzips files to text files, renames them with year appended

def unzipYear(file_dict, year):

    # unzip file for given year
    for fn in file_dict[year]:
        f = open(fn, 'rb')
        zf = zipfile.ZipFile(f)
        zf.extractall()
        zf.close()

    # append year to text files
    for fn in file_dict['txt']:
        newfile = fn[:-4] + year[2:] + '.txt'
        os.rename(fn, newfile)


###### initFiles - calls functions to download, unzip, and rename files for all years

def initFiles():
    getCandComms()      # download candidate and committee files
    getContribs()       # download contribution files
    getHeaders()        # download file headers

    os.chdir(RAW_DIR)       # move to raw data directory
    
    # unzip and rename raw files for each year
    for y in ELECT_YR:
        unzipYear(CANDCOMM_FILES, y)    # candidate and committee files
        unzipYear(CONTRIB_FILES, y)     # contribution files

    # remove all zip files
    for fn in os.listdir(os.getcwd()):
        if fn.endswith('zip'):
            os.remove(fn)

    os.chdir(PROJ_DIR)      # return to project directory


##### updateCandComms - downloads candidate and committee files and file headers from FEC site

def updateCandComms(year):
    try:
        ftp = FTP(HOST)           # connect to host fec.ftp.gov
        ftp.login()

        os.chdir(RAW_DIR)         # move to raw data directory

        ftp.cwd('/FEC/' + year)      # move to FTP directory matching year
        ftp.retrlines('LIST')     # list files

        # download files
        for fn in CANDCOMM_FILES[year]:
            f = open(fn, 'wb')
            ftp.retrbinary('RETR ' + fn, f.write)
            f.close()

    except ftplib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % fn
        os.unlink(fn)

    ftp.quit()
    os.chdir(PROJ_DIR)      # return to project directory


###### updateContribs - downloads contribution files and file headers from FEC site

def updateContribs(year):
    try:
        ftp = FTP(HOST)             # connect to host ftp.fec.gov
        ftp.login()

        os.chdir(RAW_DIR)           # move to raw data directory

        ftp.cwd('/FEC/' + year)     # move to FTP directory matching year
        ftp.retrlines('LIST')       # list files

        # download files
        for fn in CONTRIB_FILES[year]:
            f = open(fn, 'wb')
            ftp.retrbinary('RETR ' + fn, f.write)
            f.close()

    except ftplib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % fn
        os.unlink(fn)

    ftp.quit()
    os.chdir(PROJ_DIR)      # return to project directory


###### updateFiles - calls functions to download, unzip, and rename files for a given year

def updateFiles(year):
    updateCandComms(year)   # download candidate and committee files
    updateContribs(year)    # download contribution files

    os.chdir(RAW_DIR)       # move to raw data directory
    
    unzipYear(CANDCOMM_FILES, year)    # candidate and committee files
    unzipYear(CONTRIB_FILES, year)     # contribution files

    # remove all zip files
    for fn in os.listdir(os.getcwd()):
        if fn.endswith('zip'):
            os.remove(fn)

    os.chdir(PROJ_DIR)      # return to project directory

###### MAIN

if __name__ == '__main__':

    # initFiles()
    
    # updateFiles('2016')
    