# ==========================================
# Урок 4. Первый ETL-пайплайн
# ==========================================

# Импортируем класс для работы с датой
from datetime import datetime

# Импортируем объект DAG
from airflow import DAG

# Импортируем оператор,
# который умеет выполнять Python-функции
from airflow.operators.python import PythonOperator


# ==========================================
# ЭТАП 1. Получение данных
# ==========================================

def extract():

    print("=== EXTRACT ===")

    # Представим, что получили данные из API
    data = [5, 8, 12, 20]

    print("Получили данные:")
    print(data)


# ==========================================
# ЭТАП 2. Обработка данных
# ==========================================

def transform():

    print("=== TRANSFORM ===")

    data = [5, 8, 12, 20]

    doubled = [x * 2 for x in data]

    print("После обработки:")

    print(doubled)


# ==========================================
# ЭТАП 3. Загрузка
# ==========================================

def load():

    print("=== LOAD ===")

    print("Данные сохранены")


# ==========================================
# Создаем DAG
# ==========================================

with DAG(

    dag_id="lesson_04",

    start_date=datetime(2026, 1, 1),

    schedule=None,

    catchup=False,

) as dag:

    extract_task = PythonOperator(

        task_id="extract",

        python_callable=extract,

    )

    transform_task = PythonOperator(

        task_id="transform",

        python_callable=transform,

    )

    load_task = PythonOperator(

        task_id="load",

        python_callable=load,

    )

    # Определяем порядок выполнения
    extract_task >> transform_task >> load_task