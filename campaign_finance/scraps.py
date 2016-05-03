
# CONFIG.PY


# dict for classification codes and descriptions (WIP)
# (k, v) = (code, description)
CLASS_CODES = {
    'AMNDT_IND': {},
    'CAND_ICI': {},
    'CAND_STATUS': {},
    'CMTE_DSGN': {},
    'CMTE_FILING_FREQ': {},
    'CMTE_TP': {},
    'ENTITY_TP': {},
    'ORG_TP': {},
    'OFFICE': {},
    'RPT_TP': {},
    'TRANSACTION_PGI': {},
    'TRANSACTION_TP': {}
}


# EXTRACT.PY



# [START get_headers]
def get_headers():
    try:
        site_url = 'http://www.fec.gov/finance/disclosure/metadata/'

        # download candidate and committee file headers
        for file_name in CANDCOMM_FILES['head']:
            file_url =  site_url + file_name
            urllib.urlretrieve(file_url, RAW_DIR + file_name)

            print('-- Downloaded: %s' % file_name)

        # download contribution file headers
        for file_name in CONTRIB_FILES['head']:
            file_url =  site_url + file_name
            urllib.urlretrieve(file_url, RAW_DIR + file_name)

            print('-- Downloaded: %s' % file_name)

    except urllib.error_perm, e:
        print 'ERROR: cannot read file "%s"' % file_name
        os.unlink(file_name)
# [END get_headers]



# TRANSFORM.PY


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


transform
  - convert TRANSACTION_DT string to "mm-dd-yyyy" date format
  - standardize EMPLOYER string
  - group EMPLOYER into new col INDUSTRY

"""


# LOAD.PY