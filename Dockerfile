FROM apache/airflow:3.3.2
COPY requirements-airflow.txt /
RUN pip install --no-cache-dir -r /requirements-airflow.txt \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.3.2/constraints-3.12.txt"
