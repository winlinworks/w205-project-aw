import sys
from ftplib import FTP
from urllib

ftp = FTP('ftp.fec.gov')	# connect to host: ftp.fec.gov
ftp.login()		# user = anonymous, pass = anonymous

ftp.cwd('FEC')	# change directory to 'FEC'
ftp.retrlines('LIST')	# list directory contents

# Download data files:
# 1. Committee Master
# 		- data: ftp://ftp.fec.gov/FEC/2016/cm16.zip, ../cm14.zip, ../cm12.zip
#		- header: http://www.fec.gov/finance/disclosure/metadata/cm_header_file.csv

# 2. Candidate Master
# 		- data: ftp://ftp.fec.gov/FEC/2016/cn16.zip, ../cn14.zip, ../cn12.zip
# 		- header: http://www.fec.gov/finance/disclosure/metadata/cn_header_file.csv

# 3. Contributions to Candidates (and other expenditures) from Committees
# 		- data: ftp://ftp.fec.gov/FEC/2016/pas216.zip, ../pas214.zip, ../pas212.zip
# 		- header: http://www.fec.gov/finance/disclosure/metadata/pas2_header_file.csv

# 4. Contributions by Individuals
# 		- data: ftp://ftp.fec.gov/FEC/2016/indiv16.zip, ../indiv14.zip, ../indiv12.zip
# 		- header: http://www.fec.gov/finance/disclosure/metadata/indiv_header_file.csv


ftp.quit()