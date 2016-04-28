import sys
import os
import zipfile
import urllib
import ftplib
from ftplib import *
from config import *


# [START updateFiles]
def updateFiles():
    print('Welcome to Campaign Finance Explorer...\n')

    # for each election cycle, unzip and rename raw files
    for year in ELECT_YR:
        print('Downloading candidate and committee files for %s...' % year)

        getFiles(CANDCOMM_FILES, year)      # download candidate and committee files
        unzipFiles(CANDCOMM_FILES, year)    # candidate and committee files

        print('Downloading contribution and transfer files for %s...' % year)

        getFiles(CONTRIB_FILES, year)       # download contribution files    
        unzipFiles(CONTRIB_FILES, year)     # contribution files

    getHeaders()    # download file headers

    # remove zip files from raw data directory
    print('Cleaning up folder...')

    for fn in os.listdir(RAW_DIR):
        if fn.endswith('zip'):
            os.remove(RAW_DIR + fn)

            print('-- Removed: %s' % fn)
# [END updateFiles]


# [START getFiles]
def getFiles(file_dict, year):
    try:
        ftp = FTP(FTP_HOST)             # connect to host: fec.ftp.gov
        ftp.login()
        ftp.cwd('/FEC/' + year)         # move to FTP directory matching year
        # ftp.retrlines('LIST')         # list all files

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
# [END getFiles]


# [START getHeaders]
def getHeaders():
    try:
        site_url = 'http://www.fec.gov/finance/disclosure/metadata/'

        # download candidate and committee file headers
        for fn in CANDCOMM_FILES['head']:
            file_url =  site_url + fn
            urllib.urlretrieve(file_url, RAW_DIR + fn)

            print('-- Downloaded: %s' % fn)

        # download contribution file headers
        for fn in CONTRIB_FILES['head']:
            file_url =  site_url + fn
            urllib.urlretrieve(file_url, RAW_DIR + fn)

            print('-- Downloaded: %s' % fn)

    except urllib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % fn
        os.unlink(fn)
# [END getHeaders]


# [START unzipYear]
def unzipFiles(file_dict, year):

    # unzip files to text files
    for fn in file_dict[year]['zip']:
        f = open(RAW_DIR + fn, 'rb')
        zf = zipfile.ZipFile(f)
        zf.extractall(RAW_DIR)
        zf.close()

        print('-- Unzipped: %s' % fn)

    # rename text files with year appended
    for fn in file_dict['temp']:
        newfile = fn[:-4] + year[2:] + '.txt'
        os.rename(RAW_DIR + fn, RAW_DIR + newfile)

        print('-- Renamed: %s -> %s') % (fn, newfile)
# [END unzipYear]


if __name__ == '__main__':
    updateFiles()

