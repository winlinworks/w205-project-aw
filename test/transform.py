import argparse
import pandas as pd

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials

# Committee Master (cnXX.txt)
# Decode fields: CMTE_DSGN, CMTE_TP, CMTE_PTY_AFFILIATION, ORG_TP

def transformCommMaster(bigquery_service, project_id):
    try:
        # [START build_service]
        # Grab the application's default credentials from the environment.
        credentials = GoogleCredentials.get_application_default()

        # Construct the service object for interacting with the BigQuery API.
        bigquery_service = build('bigquery', 'v2', credentials=credentials)
        # [END build_service]

        # [START run_query]
        query_request = bigquery_service.jobs()
        query_data = {
            'query': (
                'SELECT test_data.cm16.CMTE_ID as cmte_id, '
                'test_data.cm16.CMTE_DSGN as cmte_dsgn, '
                'test_data.cm16.CAND_ID as cand_id, '
                'test_data.cd_cmte_dsgn.DESC as cmte_dsgn, '
                'test_data.cd_cmte_tp.DESC as cmte_tp, '
                'test_data.cd_pty_affil.DESC as pty_affil, '
                'test_data.cd_org_tp.DESC as org_tp '
                'FROM [test_data.cm16] as cm'
                'LEFT JOIN [test_data.cd_cmte_dsgn] as cd_cmte_dsgn'
                'ON cm.CMTE_DSGN=cd_cmte_dsgn.CODE'
                'LEFT JOIN [test_data.cd_cmte_tp] as cd_cmte_tp'
                'ON cm.CMTE_TP=cd_cmte_tp.CODE'
                'LEFT JOIN [test_data.cd_pty_affil] as cd_pty_affil'
                'ON cm.CMTE_PTY_AFFILIATION=cd_pty_affil.CODE'
                'LEFT JOIN [test_data.cd_org_tp] as cd_org_tp'
                'ON cm16.ORG_TP=cd_org_tp.CODE;'
                )
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


# Candidate Master (cmXX.txt)
# Decode fields - CAND_OFFICE, CAND_ICI, CAND_STATUS, CAND_PTY_AFFILIATION

def transformCandMaster(bigquery_service, project_id):

    print 'Hello World 2'

# Contributions by Individuals (itcontXX.txt) / Committees (itpas2.txt)
# Decode fields - RPT_TP, TRANSACTION_TP, ENTITY_TP

# Convert date strings to Tableau "mm-dd-yyyy" format (TRANSACTION_DT)

# Delete columns - IMAGE_NUM, TRAN_ID, FILE_NUM, SUB_ID

def transformContribs(bigquery_service, project_id):
    print 'Hello World 3'

# String conversion

# 	Standardize employer names
#	Cluster employers into industries??