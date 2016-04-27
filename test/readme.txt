W205 Project
Campaign Finance Explorer

1. OVERVIEW

Problem Statement/Key Questions:
    - Which candidates should I vote for?
    - Who contributes to candidates?  Individuals?  Companies?  PACs?
    - What interests do these individuals/companies/PACs represent?

Solution: tool to perform exploratory data analysis of campaign contributions and independent expenditures for 
    - Total contributions and expenditures
    - Aggregate totals by candidate, donor, donor type, expenditure type, etc.
    - Total contributions over time, by location


2. DATA

2.1. Sources
    - Main site with files and descriptions: http://www.fec.gov/finance/disclosure/ftpdet.shtml
    - FTP site with files: ftp://ftp.fec.gov/FEC

2.2. Main Files
    - Dimensions - files for current election cycle (2016) updated daily
        - Committee Master File - cmXX.zip
        - Candidate Master File - cnXX.zip

    - Transactions - files for current election cycle (2016) updated weekly
        - Contributions to Candidates (and other expenditures) from Committees - pas2XX.zip
        - Contributions by Individuals - indivXX.zip

2.3. Metadata
    - Data dictionaries and codes - see Format Description in main site
    - Header files - see data dictionaries for files


3. PROJECT

3.1. Environment
    - EC2 instance: public DNS
    - BigQuery project: public URL

3.2. Directory Structure

/campaign_finance
    campaign_finance.py
    extract.py
    transform.py
    load.py
    /data_master

    /data_raw
        - cn12.txt, cn14.txt, cn16.txt
        - cm12.txt, cm14.txt, cm16.txt
        - itcont12.txt, itcont14.txt, itcont16.txt
        - itpas212.txt, itpas214.txt, itpas216.txt

3.3. Application Modules
    - Extract
        - Download main files for current election cycle to raw data folder (data_raw)
        - Unzip files to text files
        - Rename raw text files (add 2-digit year for election cycle)

    - Transform
        - Read raw text files and headers into data frames
        - Filter out unused columns
        - Write transformed data (no headers) to master data folder (data_master)

    - Load
        - Load transformed data into database
        - Create materialized views for queries

3.4. How to Use Campaign Finance Explorer
    - Visualization - public URL for Tableau workbook
        - Dashboards
        - Worksheets
    - BigQuery query browser
        - Saved queries
        - Exporting files

