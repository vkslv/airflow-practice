from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import get_current_context



# Требования:
# @task
# schedule="@daily"
# catchup=True
# start_date поставь на 5 дней назад (от текущей даты)

# Внутри задачи выведи:
# logical_date
# run_id


with DAG(
    dag_id='lesson_08',
    start_date=datetime(2026, 06, 21),
    schedule="@daily",
    catchup=True
):
    
    @task
    def show_context():
        context = get_current_context()

        logical_date = context['logical_date']
        run_id = context["run_id"]

        print(logical_date)
        print(run_id)
    
    show_context()