subliimport sys, os
import zipfile

import urllib
import ftplib
from ftplib import FTP

# directory structure
# ./data_raw - folder for raw data files
# ./data_new - folder for transformed data files

    pass
PROJ_DIR = os.getcwd()              # parent directory where main apps are
RAW_DIR = PROJ_DIR + '/data_raw/'  # directory where files will be stored
HOST = 'ftp.fec.gov'


# dictionary for election years and downloaded file names
FILE_DICT = {
            '2016': ['cm16.zip', 'cn16.zip', 'pas216.zip', 'indiv16.zip'],
            '2014': ['cm14.zip', 'cn14.zip', 'pas214.zip', 'indiv14.zip'],
            '2012': ['cm12.zip', 'cn12.zip', 'pas212.zip', 'indiv12.zip']
            }

# file names for header files, same across all years
HEADER_FILES = ['cm_header_file.csv', 'cn_header_file.csv', 'pas2_header_file.csv', 'indiv_header_file.csv']

# file names for unzipped text files, same across all years
UNZIP_FILES = ['cm.txt', 'cn.txt', 'itcont.txt', 'pas2.txt']


# downloads raw data for contributions, candidates, and committees from ftp.fec.gov
def getFiles():
    try:
        ftp = FTP('ftp.fec.gov')    # connect to host: ftp.fec.gov
        ftp.login()                 # user = anonymous, pass = anonymous

        os.chdir(RAW_DIR)           # move to raw data directory

        # download files for each year
        for k, v in FILE_DICT.iteritems():
            ftp.cwd('/FEC/' + k)      # move to FTP directory matching year
            ftp.retrlines('LIST')     # list files

            # download files
            for fn in v:
                f = open(fn, 'wb')
                ftp.retrbinary('RETR ' + fn, f.write)
                f.close()

        # download header files
        for fn in HEADER_FILES:
            url = 'http://www.fec.com/finance/disclosure/metadata/' + fn
            urllib.urlretrieve(url, fn)

    except ftplib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % fn
        os.unlink(fn)

    ftp.quit()
    os.chdir(PROJ_DIR)      # return to project directory


# unzips all raw zip files to text files, adds year suffix to text file name
def unzipFiles():
    os.chdir(RAW_DIR)       # move to raw data directory

    # for each year
    for k, v in FILE_DICT.iteritems():
        suffix = k[2:]      # suffix for year

        # unzip each file
        for fn in v:
            f = open(fn, 'rb')
            zf = zipfile.ZipFile(f)
            zf.extractall()
            zf.close()

        # add year suffix to each text file
        for fn in os.listdir(RAW_DIR):         
            if fn in UNZIP_FILES:
                currfile = fn
                newfile = fn[:-4] + suffix + '.txt'
                os.rename(currfile, newfile)    # rename file

    os.chdir(PROJ_DIR)      # return to project directory


if __name__ == '__main__':
    getFiles()
    unzipFiles()