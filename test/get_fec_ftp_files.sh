
# connect to FTP site and open FTP shell
ftp ftp.fec.gov

# credentials: name = anonymous; no password

### IN FTP SHELL

# go to parent dir
cd FEC
ls

# change to dir for each year, check contents
cd FEC/2014
ls

# download files

# individual and committee contributions
get indiv14.zip

# miscellaneous transactions (including data in pas214.zip)
get oth14.zip

# PAC contributions and independent expenditures
get pas214.zip



### IN BASH SHELL

# unzip all zip files in dir
unzip '*.zip'


# TIPS:

# Can use bash in local dir e.g., !ls, !mv, !rm, etc.

# For Git...
# ALWAYS USE... use git rm -r --cache;
# DON'T USE... git rm -r... = DEATH

