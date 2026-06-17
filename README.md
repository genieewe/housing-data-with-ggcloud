# End-to-End Medallion Architecture for rent house price

## Project Overview
An automated, scalable Data Engineering pipeline that extracts raw Japan housing data, processes it through a Medallion Architecture (Bronze, Silver, Gold), and loads it into a Google Cloud data warehouse for final analysis and visualization. 

This project was built to demonstrate containerized orchestration, secure cloud integration, and memory-safe data processing techniques.

## Architecture & Tech Stack
* **Orchestration:** Apache Airflow (Dockerized)
* **Language:** Python (google-cloud-bigquery, Matplotlib, Seaborn)
* **Data Warehouse:** Google Cloud BigQuery
* **Architecture Pattern:** Medallion (Bronze -> Silver -> Gold)
* **Environment:** GitHub Codespaces / Jupyter Notebooks

## Key Engineering Decisions
* **Memory-Safe Ingestion:** Instead of loading the entire raw dataset into local RAM using Pandas, the extraction layer utilizes native BigQuery streaming. This ensures the pipeline remains stable and scalable regardless of host hardware limitations.
* **Idempotent Data Layers:** The Bronze layer utilizes `WRITE_TRUNCATE` configurations, ensuring that daily Airflow runs are perfectly idempotent and do not create duplicate records.
* **Decoupled Visualization:** By storing the finalized "Gold" data in BigQuery, the backend architecture is completely decoupled from the presentation layer. The final business insights are rendered efficiently via cloud-executed Jupyter Notebooks.

## Presentation Layer
![Example of share house rent fee data from Kaggle](tokyo_rent_analysis.png)

## How to Run Locally

1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/tokyo-housing-data-pipeline.git](https://github.com/your-username/tokyo-housing-data-pipeline.git)

