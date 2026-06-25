# Импортируем класс datetime
from datetime import datetime

# Импортируем DAG
from airflow import DAG

# Импортируем декоратор task и функцию для получения контекста
from airflow.decorators import task, get_current_context


with DAG(
    dag_id="lesson_07",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
):

    @task
    def show_context():
        # Получаем контекст текущего запуска задачи
        context = get_current_context()

        # Достаем значения из контекста
        dag_id = context["dag"].dag_id
        task_id = context["task"].task_id
        run_id = context["run_id"]
        logical_date = context["logical_date"]

        # Выводим значения в лог
        print("dag_id:", dag_id)
        print("task_id:", task_id)
        print("run_id:", run_id)
        print("logical_date:", logical_date)

    show_context()