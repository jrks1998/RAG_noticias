from datetime import datetime
from airflow.sdk import dag, task, Asset

NOTICIAS_BRONZE = Asset('sqlite://noticias/bronze')
NOTICIAS_SILVER = Asset('sqlite://noticias/silver')

@dag(schedule = [NOTICIAS_BRONZE], start_date = datetime(2026, 11, 5), catchup = False, tags = ['rag', 'silver'])
def g1_silver():
    @task(outlets = [NOTICIAS_SILVER])
    def bronze_p_silver():
        from etl.transformar import bronze_para_silver
        bronze_para_silver()
    bronze_p_silver()
g1_silver()