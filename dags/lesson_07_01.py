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
        
        # Достаём основные поля
        logical_date = context["logical_date"]
        ds = context["ds"]
        ts = context["ts"]
        run_id = context["run_id"]
        data_interval_start = context["data_interval_start"]
        data_interval_end = context["data_interval_end"]

        # Печатаем значения в лог
        print("logical_date:", logical_date)
        print("ds:", ds)
        print("ts:", ts)
        print("run_id:", run_id)
        print("data_interval_start:", data_interval_start)
        print("data_interval_end:", data_interval_end)
        
    show_context()