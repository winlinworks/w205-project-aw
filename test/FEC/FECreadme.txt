              Welcome to the Federal Election Commission's FTP site.
         
         
              We will be using this site to provide basic information 
         about candidates and committees involved in financing federal 
         elections.  This is just one of many ways the Commission 
         discloses information about financing of campaigns for Congress 
         and the Presidency.    To find about more about the FEC, you can 
         call us at (800) 424-9530.
         
         
         
         A couple of technical notes:
         
         -- all the data files provided here have been compressed using 
         PKZIP.  You will need to PKUNZIP them after you've downloaded 
         them.  (PKZIP and PKUNZIP are registered trademarks of PKWARE, 
         Inc., 9025 Deerwood Dr. Brown Deer, WI 53223.  They are 
         shareware programs used for compression and decompression of 
         data files.)
         
         -- remember to download data files in binary, and documentation 
         files in ascii.
         
         -- all documentation files have the extension .txt, with the 
         rest of the name corresponding to the data file name.  The data 
         files have the extention .zip.
         
         
         
         
         About the subdirectories
         
              There are two different sets of files available from this 
         site.  One contains files created at the completion of each two 
         year election cycle which summarize the basic information 
         reported to the FEC and provide the material in what we think is 
         a more useful format for analysis.  (Some of you may have seen 
         the Commissions published Reports on Financial Activity, or used 
         data from these volume's provided in the past on computer 
         tapes.)
         
              A second subdirectory contains the raw material from which 
         the summaries are prepared.  One of the files in this directory, 
         for example, contains every contribution or independent 
         expenditure made to a candidate by a PAC or party or other type 
         of committee.  (These files have previously been available on 
         tape through the Freedom of Information Act.) 
         
         
         
         
         
         About the files themselves
         
         
              Summary directory
         
         -- The data files included here provide financial information 
         about campaigns for federal office.  There are three types of 
         organizations active in this process, and there are files which 
         focus on each.  For each two year election cycle there are three 
         summary files. 
         
              Also remember that there is a corresponding documentation 
         file for each data file, with the extention .txt
              				    
              cansum94.zip  149,701 bytes     unzips to 955,152 bytes
              
                   A fixed length, undelimited file with one record for 
              each campaign for the U.S. House or Senate during 1993-94.  
              This file includes summary information about the financing 
              of the campaign, including total receipts, the total 
              coming from individuals, totals from each of six 
              categories of Political Action Committees, totals from 
              Party committees, campaign spending, cash on hand, and 
              debts owed by the campaign.
              
              pacsum94.zip  275,721 bytes  unzips to 2,116,418 bytes
              
                   A fixed length, undelimited file with one record for 
              each PAC involved in 1993-94 federal elections.  It 
              includes financial information from the PAC, e.g. pac 
              receipts and spending, contributions to Senate and House 
              candidates, contributions to Democrats, Republicans and 
              other party candidates, contributions to incumbent members 
              of Congress, challengers, and candidates in open seats.
              
              ptysum94.zip  26,156 bytes   unzips to 220,756 bytes
              
                   A fixed length, undelimited file with one record for 
              each party committee involved in 1993-94 federal 
              elections.  The file includes financial information for 
              the party committee including receipts and disbursements, 
              contributions to federal candidates, and expenditures made 
              on behalf of Congressional campaigns.
              
         
         
              There are also two more detailed files available for 
         each two year election cycle.  These contain information 
         about specific PACs or party committees' contributions and 
         expenditures related to federal campaigns.  For example;
         
              pacdet94.zip  1,863,918 bytes unzips to 16,081,408      
              bytes 
              
                  A fixed length undelimited file with a record 
              for each candidate to whom a PAC made either a 
              contribution or an independent expenditure.  It 
              identifies the candidate and the total amount given 
              or spent by the PAC.  This file can be used then to 
              see which candidates a PAC has supported, and 
              alternatively you can see which PACs have given to 
              a specific candidate. 
              
              
              
              ptydet94.zip 43,520 bytes unzips to 289,280 bytes
              
              The same as the PAC detailed file described above, 
              but it contains only party committee activity.  
              				    
              
              
         
              Detailed Directory
         
              foiacm.zip  
              
              The Committee Master file, provides basic information 
              about each committee registered with the FEC.  It 
              includes the name and sponsor for PAC's, name, 
              treasurer's name, and mailing address for all 
              committees (Campaign committees, PAC's, Parties, and 
              others).  Perhaps most important, it includes the FEC 
              ID number for each committee along with this basic 
              information.  This number provides the link to 
              financial data files which contain the ID number of 
              committees making and receiving contributions.
              
              
              foiacn.zip  
              
              The Candidate Master file provides basic information 
              about campaigns - name, party, state, district, 
              incumbent/challenger/open seat status, year of 
              election, address, etc.  It also contains an ID number 
              unique to that candidate which provides the link to 
              financial files where candidate activity is provided.
              
              
	itcont.zip

	      This file contains each contribution from an individual
	      to and federal committee, if the contribution was at 
              least $200 or more.  It includes the ID number of the 
              committee receiving the contribution, the name, city,
              state, zip code, and place of business of the contributor
              along with the date and amount of the contribution.
              NOTE: this is a very large file, you must be able to
              store up to 150 megabites of data at the end of an 
              election cycle

         itpas2.zip

	      This file contains each contribution or independent
              expenditure made by a PAC, party committee, candidate
	      committee, or other federal committee to a candidate during
              the two year election cycle.  It includes the ID number
              of the contributing committee and the ID number of the 
	      recipient.  You will need to use the committee and candidate
              master files in conjunction with this file to set up a
              relational data base to analyze these data.

         itoth.zip

	     This file contains all transactions (contributions, transfers
             etc., among federal committees).  As such, it includes all
             the data which appears in itpas2.zip, along with other 
             information, including PAC contributions to party committees
             and party transfers from state to state or from the national
             party committees to their state committees.  (Note that this
             file includes only federal transfers, not soft money 
             transactions.)              

         
         All of the information provided here is as reported to the 
         FEC by the campaigns and committees included.  It is public 
         information with one restriction on its use.  Information about individual people
         derived from FEC reports may not be used for solicitation or for commercial
         purpose.  The official 
         record of the Commission is the microfilmed copy of the 
         original report and is available at the Commission, 999 E 
         Street N.W. Washington, D.C. 20463.  You can get additional 
         information about the Commission and federal campaign finance 
         by calling (800) 424-9530.	     
         
         

