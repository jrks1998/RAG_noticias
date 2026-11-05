from datetime import datetime, timedelta
from airflow.sdk import dag, task

FEEDS_G1 = {
    'economia': 'https://g1.globo.com/rss/g1/economia',
    'educacao': 'https://g1.globo.com/rss/g1/educacao',
    'mundo': 'https://g1.globo.com/rss/g1/mundo',
    'politica': 'https://g1.globo.com/rss/g1/politica',
    'tecnologia': 'https://g1.globo.com/rss/g1/tecnologia'
    }

@dag(schedule = timedelta(minutes = 3), start_date = datetime(2026, 11, 5), catchup = False, tags = ['rag', 'bronze'])
def g1_bronze():
    @task
    def coletar(categoria: str):
        from scrappers.g1.g1_scrapping_utils import scrapping_criar_lista_salvar_noticias_bronze
        scrapping_criar_lista_salvar_noticias_bronze(FEEDS_G1[categoria], categoria)

    coletar.expand(categoria = list(FEEDS_G1))
g1_bronze()