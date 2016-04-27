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

from extract import *
from transform import *

PROJECT_ID = 'w205-project-1272'

def main():
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
                'SELECT TOP(TRANSACTION_AMT,10) as amount, '
                'COUNT(*) '
                'FROM [test_data.itcont16];')
        }

        query_response = query_request.query(
            projectId=PROJECT_ID,
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

    main()
    
    # parser = argparse.ArgumentParser(
    #     description=__doc__,
    #     formatter_class=argparse.RawDescriptionHelpFormatter)
    # parser.add_argument('project_id', help='Your Google Cloud Project ID.')
    # args = parser.parse_args()
    # main(args.project_id)
    
    
# [END all]


