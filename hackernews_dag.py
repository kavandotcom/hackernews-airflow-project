from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from hackernews_etl import run_hackernews_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'hackernews_dag',
    default_args=default_args,
    description='ETL process for Hacker News',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_hackernews_etl',
    python_callable=run_hackernews_etl,
    dag=dag,
)

run_etl
