import sys
import os

import urllib
import ftplib
from ftplib import FTP

import zipfile

from settings import *


###### initFiles - calls functions to download, unzip, and rename files for all years

def updateFiles():
    print('Welcome to Campaign Finance Explorer...\n')

    # unzip and rename raw files for each year
    for year in ELECT_YR:
        print('Downloading candidate and committee files for %s...' % year)

        getFiles(CANDCOMM_FILES, year)      # download candidate and committee files
        unzipFiles(CANDCOMM_FILES, year)    # candidate and committee files

        print('Downloading contribution and transfer files for %s...' % year)

        getFiles(CONTRIB_FILES, year)       # download contribution files    
        unzipFiles(CONTRIB_FILES, year)     # contribution files

    # remove zip files from raw data directory
    print('Cleaning up files...')

    for fn in os.listdir(RAW_DIR):
        if fn.endswith('zip'):
            os.remove(RAW_DIR + fn)

            print('-- Removed: %s' % fn)


###### getFiles - downloads candidate and committee files and file headers from FEC site

def getFiles(file_dict, year):
    try:
        ftp = FTP(HOST)           # connect to host fec.ftp.gov
        ftp.login()

        ftp.cwd('/FEC/' + year)      # move to FTP directory matching year
        # ftp.retrlines('LIST')     # list files

        # download files
        for fn in file_dict[year]['zip']:
            f = open(RAW_DIR + fn, 'wb')
            ftp.retrbinary('RETR ' + fn, f.write)
            f.close()

            print('-- Downloaded: %s' % fn)

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

        print('-- Unzipped: %s' % fn)

    # append year to text files
    for fn in file_dict['temp']:
        newfile = fn[:-4] + year[2:] + '.txt'
        os.rename(RAW_DIR + fn, RAW_DIR + newfile)

        print('-- Renamed: %s -> %s') % (fn, newfile)



###### main 

if __name__ == '__main__':
    updateFiles()
    