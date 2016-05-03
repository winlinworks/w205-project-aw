"""Command-line application that loads data into BigQuery via HTTP POST.

This sample is used on this page:

    https://cloud.google.com/bigquery/loading-data-into-bigquery

For more information, see the README.md under /bigquery.
"""

import argparse
import json
import time

from googleapiclient import discovery
from googleapiclient.http import MediaFileUpload
from oauth2client.client import GoogleCredentials

from config import *


# [START make_post]
def load_data(project_id, dataset_id, table_id, schema_file, data_file):
    """Loads the given data file into BigQuery.

    Args:
        schema_path: the path to a file containing a valid bigquery schema.
            see https://cloud.google.com/bigquery/docs/reference/v2/tables
        data_path: the name of the file to insert into the table.
        project_id: The project id that the table exists under. This is also
            assumed to be the project id this request is to be made under.
        dataset_id: The dataset id of the destination table.
        table_id: The table id to load data into.
    """
    # Create a bigquery service object, using the application's default auth
    credentials = GoogleCredentials.get_application_default()
    bigquery = discovery.build('bigquery', 'v2', credentials=credentials)

    # Infer the data format from the name of the data file.
    source_format = 'CSV'
    if data_file[-5:].lower() == '.json':
        source_format = 'NEWLINE_DELIMITED_JSON'

    # Post to the jobs resource using the client's media upload interface. See:
    # http://developers.google.com/api-client-library/python/guide/media_upload
    insert_request = bigquery.jobs().insert(
        projectId=project_id,
        # Provide a configuration object. See:
        # https://cloud.google.com/bigquery/docs/reference/v2/jobs#resource
        body={
            'configuration': {
                'load': {
                    'schema': {
                        'fields': json.load(open(schema_file, 'r'))
                    },
                    'destinationTable': {
                        'projectId': project_id,
                        'datasetId': dataset_id,
                        'tableId': table_id
                    },
                    'sourceFormat': source_format,
                    'createDisposition': 'CREATE_IF_NEEDED'
                }
            }
        },
        media_body=MediaFileUpload(
            data_file,
            mimetype='application/octet-stream'))
    job = insert_request.execute()

    print('Waiting for job to finish...')

    status_request = bigquery.jobs().get(
        projectId=job['jobReference']['projectId'],
        jobId=job['jobReference']['jobId'])

    # Poll the job until it finishes.
    while True:
        result = status_request.execute(num_retries=10)

        if result['status']['state'] == 'DONE':
            if result['status'].get('errors'):
                raise RuntimeError('\n'.join(
                    e['message'] for e in result['status']['errors']))
            print('Job complete.')
            return

        time.sleep(1)
# [END make_post]


# [START loadAll]
def loadAll():
    table_id = 'itpas216'
    schema_file = MASTER_DIR + 'schema_itpas2.json'
    data_file = MASTER_DIR + 'itpas216.csv'

    load_data(PROJ_ID, DATA_ID, table_id, schema_file, data_file)
# [END loadAll]


if __name__ == '__main__':

    loadAll()

