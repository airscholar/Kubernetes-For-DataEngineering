from airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'datamasterylab',
    'start_date': datetime(2024, 1, 24),
    'catchup': False
}

dag = DAG (
    'hello_datamasterylab',
    default_args=default_args,
    schedule_interval = timedelta(days=1)
)

t1 = BashOperator(
    task_id ='hello_world',
    bash_command= 'echo "Hello World"',
    dag = dag
)
t2 = BashOperator(
    task_id ='hello_dml',
    bash_command= 'echo "Hello Data Mastery Lab"',
    dag = dag
)

t1 >> t2