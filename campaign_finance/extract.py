import sys
import os

import urllib
import ftplib
from ftplib import FTP

import zipfile

from settings import *


###### initFiles - calls functions to download, unzip, and rename files for all years

def initFiles():
    print('Setting up Campaign Finance Explorer...')
    # unzip and rename raw files for each year
    for y in ELECT_YR:
        getCandComms(y)                 # download candidate and committee files
        getContribs(y)                  # download contribution files
        unzipFiles(CANDCOMM_FILES, y)    # candidate and committee files
        unzipFiles(CONTRIB_FILES, y)     # contribution files

    # remove all zip files from raw data directory
    for fn in os.listdir(RAW_DIR):
        if fn.endswith('zip'):
            os.remove(RAW_DIR + fn)

            print('Removed: %s' % fn)


###### updateFiles - calls functions to download, unzip, and rename files for a given year

def updateFiles(year):
    updateCandComms(year)   # download candidate and committee files
    updateContribs(year)    # download contribution files
    
    unzipYear(CANDCOMM_FILES, year)    # candidate and committee files
    unzipYear(CONTRIB_FILES, year)     # contribution files

    # remove all zip files from raw data directory
    for fn in os.listdir(RAW_DIR):
        if fn.endswith('zip'):
            os.remove(fn)

            print('Removed: %s' % fn)


##### updateCandComms - downloads candidate and committee files and file headers from FEC site

def getCandComms(year):
    try:
        ftp = FTP(HOST)           # connect to host fec.ftp.gov
        ftp.login()

        ftp.cwd('/FEC/' + year)      # move to FTP directory matching year
        # ftp.retrlines('LIST')     # list files

        # download files
        for fn in CANDCOMM_FILES[year]['zip']:
            f = open(RAW_DIR + fn, 'wb')
            ftp.retrbinary('RETR ' + fn, f.write)
            f.close()

            print('Download complete: %s' % fn)

    except ftplib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % fn
        os.unlink(fn)

    ftp.quit()


###### updateContribs - downloads contribution files and file headers from FEC site

def getContribs(year):
    try:
        ftp = FTP(HOST)             # connect to host ftp.fec.gov
        ftp.login()

        ftp.cwd('/FEC/' + year)     # move to FTP directory matching year
        # ftp.retrlines('LIST')       # list files

        # download files
        for fn in CONTRIB_FILES[year]['zip']:
            print('Download started: %s' % fn)

            f = open(RAW_DIR + fn, 'wb')
            ftp.retrbinary('RETR ' + fn, f.write)
            f.close()

            print('Download complete: %s' % fn)

    except ftplib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % fn
        os.unlink(fn)

    ftp.quit()


###### unzipYear - unzips files to text files, renames them with year appended

def unzipFiles(file_dict, year):

    # unzip file for given year
    for fn in file_dict[year]['zip']:
        f = open(RAW_DIR + fn, 'rb')
        zf = zipfile.ZipFile(f)
        zf.extractall(RAW_DIR)
        zf.close()

        print('Unzipped: %s' % fn)

    # append year to text files
    for fn in file_dict['temp']:
        newfile = fn[:-4] + year[2:] + '.txt'
        os.rename(RAW_DIR + fn, RAW_DIR + newfile)

        print('Renamed: %s to %s') % (fn, newfile)


###### MAIN

if __name__ == '__main__':
    initFiles()
    