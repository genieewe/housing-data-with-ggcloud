from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import timedelta, datetime

default_args = {
    'owner' : 'genie',
    'depend_on_past' : True, #if yesterday's progress failed, it stopped until it is fixed
    'start_date' : datetime(2026, 5, 21),
    'retries' : 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG (
    dag_id = 'tokyo_housing_data_pipeline',
    description = 'Daily automated ELT for Japan share house price',
    default_args = default_args,
    schedule = '@daily',
    catchup = False,
    tags = ['housing', 'bigquery', 'ELT']
) as dag:
    load_bronze_data = BashOperator (
        task_id = 'load_csv_to_bronze',
        bash_command = 'python3 /opt/airflow/dags/load-data.py'
    )

    silver_query = "SELECT * FROM `housing_raw_data.raw_bronze`"
    run_silver_sql = BigQueryInsertJobOperator (
        task_id = 'load_bronze_to_silver',
        configuration = {
            "query": {
                "query": silver_query,
                "useLegacySql": False,
            }
        }
    )

    gold_query = "SELECT * FROM `housing_raw_data.gold_master_housing`"
    run_gold_sql = BigQueryInsertJobOperator (
        task_id = 'load_silver_to_gold',
        configuration = {
            "query": {
                "query": gold_query,
                "useLegacySQL": False,
            }
        }
    )

    load_bronze_data >> run_silver_sql >> run_gold_sql
