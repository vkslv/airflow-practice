from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="lesson_02",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    start = EmptyOperator(task_id="start")

    process = EmptyOperator(task_id="process")

    finish = EmptyOperator(task_id="finish")

    start >> process >> finish