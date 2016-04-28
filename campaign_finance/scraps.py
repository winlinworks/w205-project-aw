


###### EXTRACT.PY


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





###### TRANSFORM.PY


"""

format issues
- date formate is mmddyyyy
- zip codes and dates are being read and saved as floats?

APPROACH

Method 1: normalize/join data locally, then load to BQ
- Use pandas for more intuitive workflow
- Filter future data before loading to reduce size of loads
- Can merge on 2 cols/indices

Method 2: load all raw/denormalized data to BQ, then normalize/join data in BQ


IMPLEMENTATION

With dataframes df1, df2
- Merge: pd.merge(df1, df2, on='field', how='left')
- Join: df1.set_index('field', inplace=True); df1.join(df2)


"""


###### LOAD.PY