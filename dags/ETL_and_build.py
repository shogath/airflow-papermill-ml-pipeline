from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.papermill.operators.papermill import PapermillOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='ETL_and_build',
    default_args=default_args,
    schedule_interval='@once',
    start_date=datetime(2022, 1, 1),
    template_searchpath='/usr/local/airflow/notebooks',
    catchup=False
) as dag_1:

    load_data_task = PapermillOperator(
        task_id="load_data",
        input_nb="/opt/airflow/notebooks/1_Load_data.ipynb",
        output_nb="/opt/airflow/results/out-1_Load_data-{{ execution_date }}.ipynb",
        parameters={"execution_date": "{{ execution_date }}"},
        kernel_name='python3',
    )
    eda_task = PapermillOperator(
        task_id="eda",
        input_nb="/opt/airflow/notebooks/2_EDA.ipynb",
        output_nb="/opt/airflow/results/out-2_EDA-{{ execution_date }}.ipynb",
        parameters={"execution_date": "{{ execution_date }}"},
        kernel_name='python3',
    )
    data_preprocessing_task = PapermillOperator(
        task_id="data_preprocessing",
        input_nb="/opt/airflow/notebooks/3_Data_Pre-processing.ipynb",
        output_nb="/opt/airflow/results/out-3_Data_Pre-processing-{{ execution_date }}.ipynb",
        parameters={"execution_date": "{{ execution_date }}"},
        kernel_name='python3',
    )
    model_building_task = PapermillOperator(
        task_id="model_building",
        input_nb="/opt/airflow/notebooks/4_Model_building.ipynb",
        output_nb="/opt/airflow/results/out-4_Model_building-{{ execution_date }}.ipynb",
        parameters={"execution_date": "{{ execution_date }}"},
        kernel_name='python3',
    )

load_data_task >> eda_task >> data_preprocessing_task >> model_building_task