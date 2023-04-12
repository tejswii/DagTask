from airflow import DAG
from airflow.operators.dummy_operator import  DummyOperator
from airflow.operators.bash import  BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def hey():
        print("hey")

with DAG(dag_id = "Dag_1",start_date = datetime(2023,1,1),
        schedule_interval="@hourly",catchup=False) as dag:
                start = DummyOperator(task_id = "start")
                bash_op = BashOperator(task_id ="bashOp",bash_command = " echo hey")
                py_op = PythonOperator(task_id ="pythonOp",python_callable = hey)
                end = DummyOperator(task_id = "end")

start >> bash_op >> py_op >> end
