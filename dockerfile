FROM apache/airflow:2.9.0
RUN pip install google-cloud-bigquery pandas apache-airflow apache-airflow-providers-google
