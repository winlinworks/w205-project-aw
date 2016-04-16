import sys
from ftplib import FTP

ftp = FTP('ftp.fec.gov')	# connect to host: ftp.fec.gov
ftp.login()		# user = anonymous, pass = anonymous

ftp.cwd('FEC')	# change directory to 'FEC'
ftp.retrlines('LIST')	# list directory contents

ftp.quit()