W205 Project: Visualization of Campaign Finances for Candidates for President, House, and Senate


1. OVERVIEW

Problem Statement/Key Questions:
- Which candidate should I vote for?
- Who is contributing to a candidate's campaign?  Individuals?  Companies?  PACs?
- What interests do these 

Solution: Interactive Visualization of Transactions
- Summary of individual contributions and independent expenditures
- Group by candidate, donor, donor type, expenditure type, etc.
- Contributions and policy positions over time
- Spatial analysis of contributions and delegates


2. DATA

Sources:
    - Main site: http://www.fec.gov/finance/disclosure/ftpdet.shtml
    - FTP site: ftp://ftp.fec.gov/FEC

Main Files to Download:
    - Dimensions - updated daily
        - Committee Master File - cmXX.zip
        - Candidate Master File - cnXX.zip
    - Transactions - updated weekly
        - Contributions to Candidates (and other expenditures) from Committees - pas2XX.zip
        - Contributions by Individuals - indivXX.zip

Static Metadata:
    - Header files
    - Data dictionaries and codes


3. APPLICATION

Directory Structure:

/campaign_finance
    campaign_finance.py
    extract.py
    transform.py
    load.py
    /data_master
    /data_raw

Modules:
    - Extract
        - Download raw ZIP files
        - Unzip and rename files

    - Transform
        - Read data files and headers into data frames
        - Filter out unused columns and rows
        - Write transformed data to disk
        - Log entries for transformations

    - Load
        - Load transformed data into database
        - Create materialized views for queries


RESULTS


