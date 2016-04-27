# connect to BigQuery


#!/usr/bin/env python

"""Command-line application that demonstrates basic BigQuery API usage.
This sample queries a public shakespeare dataset and displays the 10 of
Shakespeare's works with the greatest number of distinct words.

This sample is used on this page:
    https://cloud.google.com/bigquery/bigquery-api-quickstart

For more information, see the README.md under /bigquery.
"""

# [START all]
import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import GoogleCredentials


def main(project_id):
    # [START build_service]
    # Grab the application's default credentials from the environment.
    credentials = GoogleCredentials.get_application_default()
    # Construct the service object for interacting with the BigQuery API.
    bigquery_service = build('bigquery', 'v2', credentials=credentials)
    # [END build_service]

    try:
        # [START run_query]
        query_request = bigquery_service.jobs()
        query_data = {
            'query': (
                'SELECT TOP(corpus, 10) as title, '
                'COUNT(*) as unique_words '
                'FROM [publicdata:samples.shakespeare];')
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Your Google Cloud Project ID.')

    args = parser.parse_args()

    main(args.project_id)
# [END all]



# Convert code fields to names, descriptions for easier interpretation
# Committee master (cn)
# 	CMTE_DSGN
# 	CMTE_TP
# 	CMTE_PTY_AFFILIATION
# 	CMTE_FILING_FREQ
# 	ORG_TP

# Candidate master (cm)
# 	CAND_OFFICE
# 	CAND_ICI
# 	CAND_STATUS
# 	CAND_PTY_AFFILIATION

# Contributions by individuals (itcont),
# Contributions to candidates from committees (pas2)
# 	RPT_TP
# 	TRANSACTION_TP
# 	ENTITY_TP

# Delete unused columns to reduce file size
# 	IMAGE_NUM
# 	TRAN_ID
# 	FILE_NUM
# 	SUB_ID

# String conversion
# 	Convert date strings to date format (TRANSACTION_DT)
# 	Standardize employer names
#	Cluster employers into industries??