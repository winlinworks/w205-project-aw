
###### getHeaders - downloads file headers from ftp.fec.gov

def getHeaders():
    try:
        # download candidate and committee file headers
        for fn in CANDCOMM_FILES['head']:
            url = 'http://www.fec.gov/finance/disclosure/metadata/' + fn
            urllib.urlretrieve(url, RAW_DIR + fn)

        # download contribution file headers
        for fn in CONTRIB_FILES['head']:
            url = 'http://www.fec.gov/finance/disclosure/metadata/' + fn
            urllib.urlretrieve(url, RAW_DIR + fn)

    except urllib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % fn
        os.unlink(fn)


    ###### updateFiles - calls functions to download, unzip, and rename files for a given year

def updateFiles(year):
    getFiles(CANDCOMM_FILES, year)   # download candidate and committee files
    getFiles(CONTRIB_FILES, year)    # download contribution files
    
    unzipFiles(CANDCOMM_FILES, year)    # candidate and committee files
    unzipFiles(CONTRIB_FILES, year)     # contribution files

    # remove all zip files from raw data directory
    for fn in os.listdir(RAW_DIR):
        if fn.endswith('zip'):
            os.remove(fn)

            print('Removed: %s' % fn)