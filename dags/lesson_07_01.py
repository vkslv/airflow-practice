from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import get_current_context

with DAG(
    dag_id='lesson_07_01',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
):
    @task
    def show_context():
        context = get_current_context()
        print(context.keys())

    show_context()