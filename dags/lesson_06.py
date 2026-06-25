# ==========================================
# Урок 6. TaskFlow API
# ==========================================

# Работа с датой
from datetime import datetime

# Импортируем DAG
from airflow import DAG

# Импортируем декоратор task
from airflow.decorators import task


# Создаем DAG
with DAG(

    dag_id="lesson_06",

    start_date=datetime(2026, 1, 1),

    schedule=None,

    catchup=False,

):

    # ----------------------------
    # Получение данных
    # ----------------------------
    @task
    def extract():

        print("Получаем данные")

        return [5, 8, 12, 20]


    # ----------------------------
    # Обработка данных
    # ----------------------------
    @task
    def transform(data):

        doubled = [x * 2 for x in data]

        print(doubled)

        return doubled


    # ----------------------------
    # Загрузка
    # ----------------------------
    @task
    def load(data):

        print("Сохраняем")

        print(data)


    # Создаем зависимости между задачами
    load(
        transform(
            extract()
        )
    )