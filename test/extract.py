import sys
from ftplib import FTP
import urllib

ftp = FTP('ftp.fec.gov')        # connect to host: ftp.fec.gov
ftp.login()             # user = anonymous, pass = anonymous

ftp.cwd('FEC')  # change directory to 'FEC'
ftp.cwd('2016') # change directory to '2016'
ftp.retrlines('LIST')   # list directory contents

# Download data files:

# 2016

dfiles = ['cm16.zip', 'cn16.zip', 'pas216.zip', 'indiv16.zip']
for filename in dfiles:
  f = open(filename, 'wb')
  ftp.retrbinary('RETR ' + filename, f.write)
  f.close()

#2014
ftp.cwd('../2014') # change directory to 2014
ftp.retrlines('LIST')  # list directory contents

d4files = ['cm14.zip', 'cn14.zip', 'pas214.zip', 'indiv14.zip']
for filename in d4files:
   f = open(filename, 'wb')
   ftp.retrbinary('RETR ' + filename, f.write)
   f.close()

#2012 files

ftp.cwd('../2012')  # change directory to 2012
ftp.retrlines('LIST')

d2files = ['cm12.zip', 'cn12.zip', 'pas212.zip', 'indiv12.zip']
for filename in d2files:
   f = open(filename, 'wb')
   ftp.retrbinary('RETR ' + filename, f.write)
   f.close()


#Now get the header files


filenames = ['cm_header_file.csv', 'cn_header_file.csv', 'pas2_header_file.csv', 'indiv_header_file.csv']
for name in filenames:
    url = 'http://www.fec.com/finance/disclosure/metadata/' + name
    urllib.urlretrieve(url, name)


# 1. Committee Master
#               - data: ftp://ftp.fec.gov/FEC/2016/cm16.zip, ../cm14.zip, ../cm12.zip
#               - header: http://www.fec.gov/finance/disclosure/metadata/cm_header_file.csv

# 2. Candidate Master
#               - data: ftp://ftp.fec.gov/FEC/2016/cn16.zip, ../cn14.zip, ../cn12.zip
#               - header: http://www.fec.gov/finance/disclosure/metadata/cn_header_file.csv

# 3. Contributions to Candidates (and other expenditures) from Committees
#               - data: ftp://ftp.fec.gov/FEC/2016/pas216.zip, ../pas214.zip, ../pas212.zip
#               - header: http://www.fec.gov/finance/disclosure/metadata/pas2_header_file.csv

# 4. Contributions by Individuals
#               - data: ftp://ftp.fec.gov/FEC/2016/indiv16.zip, ../indiv14.zip, ../indiv12.zip
#               - header: http://www.fec.gov/finance/disclosure/metadata/indiv_header_file.csv


ftp.quit()



