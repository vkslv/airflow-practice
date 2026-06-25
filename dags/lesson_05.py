# ==========================================
# Урок 5. Передача данных через XCom
# ==========================================

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


# ----------------------------
# Получаем данные
# ----------------------------
def extract():

    print("Получаем данные")

    data = [5, 8, 12, 20]

    # Возвращаем список.
    # Airflow автоматически сохранит его в XCom.
    return data


# ----------------------------
# Обрабатываем данные
# ----------------------------
def transform(ti):
    """
    ti = TaskInstance.
    Через него можно работать с XCom.
    """

    # Получаем результат задачи extract
    data = ti.xcom_pull(task_ids="extract")

    print("Получили из XCom:")

    print(data)

    doubled = [x * 2 for x in data]

    print("После обработки:")

    print(doubled)

    return doubled


# ----------------------------
# Сохраняем
# ----------------------------
def load(ti):

    data = ti.xcom_pull(task_ids="transform")

    print("Получили:")

    print(data)

    print("Данные успешно сохранены!")


with DAG(

    dag_id="lesson_05",

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

    extract_task >> transform_task >> load_task