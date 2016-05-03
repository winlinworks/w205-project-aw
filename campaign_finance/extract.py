import sys, os
import zipfile
import urllib
import ftplib
from ftplib import *

from config import *


# [START get_file]
def get_file(zip_type, year):

    try:
        ftp = FTP(FTP_HOST)             # connect to host: fec.ftp.gov
        ftp.login()
        ftp.cwd('/FEC/' + year)         # move to FTP directory matching year
        # ftp.retrlines('LIST')         # list all files

        # download files
        file = zip_type + year[2:] + '.zip'
        f = open(RAW_DIR + file, 'wb')
        ftp.retrbinary('RETR ' + file, f.write)
        f.close()

        print('-- Downloaded: %s' % file)

    except ftplib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % file
        os.unlink(RAW_DIR + file)

    ftp.quit()
# [END get_file]



# [START unzip_file]
def unzip_file(zip_type, txt_type, year):

    # unzip files to text files
    file = zip_type + year[2:] + '.zip'
    f = open(RAW_DIR + file, 'rb')
    zf = zipfile.ZipFile(f)
    zf.extractall(RAW_DIR)
    zf.close()

    print('-- Unzipped: %s' % file)

    # rename text files with year appended
    # must do before unzipping files for other years
    oldfile = txt_type + '.txt'
    newfile = txt_type + year[2:] + '.txt'
    os.rename(RAW_DIR + oldfile, RAW_DIR + newfile)

    print('-- Renamed: %s -> %s') % (oldfile, newfile)
# [END unzip_file]


# [START extract_all]
def extract_all():

    print('Welcome to Campaign Finance Explorer...\n')

    # for each election cycle, unzip and rename raw files
    for year in ELECTION_YEARS:
        print('Downloading candidate, committee, and contribution/transfer files for %s...' % year)

        for zip_type, txt_type in FILE_TYPES.items():
            get_file(zip_type, year)       # download file
            unzip_file(zip_type, txt_type, year)    # unzip file

    # remove zip files from raw data directory
    print('Cleaning up folder...')

    for file in os.listdir(RAW_DIR):
        if file.endswith('zip'):
            os.remove(RAW_DIR + file)

            print('-- Removed: %s' % file)
# [END extract]


if __name__ == '__main__':

    extract_all()
    # extract_cand_comm()
    # extract_contrib_trans()

