import pandas as pd
import pandas_gbq
from google.oauth2 import service_account

if __name__ == "__main__":
    keypath = "/opt/airflow/dags/gcp-key.json"
    credentials = service_account.Credentials.from_service_account_file(keypath)

    csv_location = "/opt/airflow/dags/tokyosharehouse.csv"

    destination_table = "housing_raw_data.raw_bronze"
    project_id = "japan-house-data"

    chunk_size = 10000
    first_chunk = True

    for chunk in pd.read_csv(csv_location, chunksize = chunk_size):
        if first_chunk:
            chunk.columns = [
                c.replace('(', '_').replace(')', '').replace(' ', '_').replace('/', '_').lower() 
                for c in chunk.columns
            ]
            chunk.to_gbq(
                destination_table = destination_table,
                project_id = project_id,
                credentials = credentials,
                if_exists = "replace"
            )
            first_chunk = False
        else:
            chunk.columns = [
                c.replace('(', '_').replace(')', '').replace(' ', '_').replace('/', '_').lower() 
                for c in chunk.columns
            ]
            chunk.to_gbq(
                destination_table = destination_table,
                project_id = project_id,
                credentials = credentials,
                if_exists = "replace"
            )

    print("Upload complete")