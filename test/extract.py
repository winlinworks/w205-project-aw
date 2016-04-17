import sys
import os
import socket
import zipfile

import urllib
import ftplib
from ftplib import FTP


CURR_DIR = os.getcwd()              # parent directory where main apps are
DEST_DIR = CURR_DIR + '/data_raw/'  # directory where files will be stored
HOST = 'ftp.fec.gov'


# dictionary for election years and associated file names
FILE_DICT = {'2016': ['cm16.zip', 'cn16.zip', 'pas216.zip', 'indiv16.zip'],
            '2014': ['cm14.zip', 'cn14.zip', 'pas214.zip', 'indiv14.zip'],
            '2012': ['cm12.zip', 'cn12.zip', 'pas212.zip', 'indiv12.zip']}

UNZIP_FILES = ['cm.txt', 'cn.txt', 'itcont.txt', 'pas2.txt']

# downloads all raw zip files from ftp.fec.gov
def getFiles():
    try:
        os.chdir(DEST_DIR)          # change local working directory

        ftp = FTP('ftp.fec.gov')    # connect to host: ftp.fec.gov
        ftp.login()                 # user = anonymous, pass = anonymous

        # for each year
        for key in FILE_DICT:
            ftp.cwd('/FEC/' + key)      # move to matching FTP directory
            ftp.retrlines('LIST')       # list files

            filenames = FILE_DICT[key]  # get file names

            # for each file name, download file from FTP site
            for fn in filenames:
                f = open(fn, 'wb')
                ftp.retrbinary('RETR ' + fn, f.write)
                f.close()

    except ftplib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % fn
        os.unlink(fn)

    ftp.quit()
    os.chdir(CURR_DIR)

# unzips all raw zip files to text files, adds year suffix to text file name
def unzipFiles():
    os.chdir(DEST_DIR)

    # for each year
    for key in FILE_DICT:
        suffix = key[2:]        # suffix for year

        filenames = FILE_DICT[key]  # get file names

        # unzip each file
        for fn in filenames:
            f = open(fn, 'rb')
            zf = zipfile.ZipFile(f)
            zf.extractall()
            zf.close()

        # add year suffix to each text file
        for fn in os.listdir(DEST_DIR):         
            if fn in UNZIP_FILES:
                currfile = fn
                newfile = fn[:-4] + suffix + '.txt'
                os.rename(currfile, newfile)    # rename file

    os.chdir(CURR_DIR)


if __name__ == '__main__':
    # getFiles()
    unzipFiles()