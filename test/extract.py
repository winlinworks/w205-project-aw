import sys
from ftplib import ftplib

ftp = FTP('ftp.fec.gov')	# connect to host: ftp.fec.gov
ftp.login()		# user = anonymous, pass = anonymous