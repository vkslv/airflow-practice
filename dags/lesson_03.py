from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def hello_airflow():
    print("Hello Airflow!")
    print("Я выполняюсь внутри таски")


with DAG(
    dag_id="lesson_03",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    task_hello = PythonOperator(
        task_id="hello_task",
        python_callable=hello_airflow,
    )