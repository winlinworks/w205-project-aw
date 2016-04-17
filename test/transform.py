import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials

# Committee Master (cn.txt)
# Decode fields
# 	CMTE_DSGN, CMTE_TP, CMTE_PTY_AFFILIATION, CMTE_FILING_FREQ, ORG_TP

def transformCommMaster(bigquery_service, project_id):
    try:
        # # [START build_service]
        # # Grab the application's default credentials from the environment.
        # credentials = GoogleCredentials.get_application_default()
        # # Construct the service object for interacting with the BigQuery API.
        # bigquery_service = build('bigquery', 'v2', credentials=credentials)
        # # [END build_service]

        # [START run_query]
        query_request = bigquery_service.jobs()
        query_data = {
            'query': (
                'SELECT TOP(TRANSACTION_AMT,10) as amount, '
                'COUNT(*) '
                'FROM [test_data.itcont16];')
        }

        query_response = query_request.query(
            projectId=project_id,
            body=query_data).execute()
        # [END run_query]
        # [START print_results]
        print('Query Results:')
        for row in query_response['rows']:
            print('\t'.join(field['v'] for field in row['f']))
            # [END print_results]
    except HttpError as err:
        print('Error: {}'.format(err.content))
        raise err


# Candidate Master (cm.txt)
# Decode fields
# 	CAND_OFFICE, CAND_ICI, CAND_STATUS, CAND_PTY_AFFILIATION

def transformCandMaster(bigquery_service, project_id):
    print 'Hello World 2'

# Contributions by Individuals (itcont.txt) / Committees (itpas2.txt)
# Decode fields
# 	RPT_TP, TRANSACTION_TP, ENTITY_TP

# Convert date strings to Tableau "mm-dd-yyyy" format (TRANSACTION_DT)

# Delete columns to reduce file size
# 	IMAGE_NUM, TRAN_ID, FILE_NUM, SUB_ID

def transformContribs(bigquery_service, project_id):
    print 'Hello World 3'

# String conversion

# 	Standardize employer names
#	Cluster employers into industries??