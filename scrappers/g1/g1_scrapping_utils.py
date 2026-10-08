import feedparser
from models.noticia import BronzeNoticia
import hashlib
from db.db_utils import salvar_noticia_bronze
from datetime import datetime

def scrapper(url):
    feed = feedparser.parse(url)
    return feed

def criar_lista_noticia_bronze(feed, categ):
    NOTICIAS_BRONZE = []
    for entry in feed.entries:
        if entry.get('summary').strip() != '':
            categoria = categ
            veiculo = 'g1'
            titulo = entry.get('title', 'sem titulo')
            subtitulo = entry.get('subtitle', 'sem subtitulo')
            materia = entry.get('summary', 'sem materia')
            data_pub = entry.get('published')
            link = entry.get('link', 'sem link')
            try:
                data_pub = datetime.strptime(data_pub, '%a, %d %b %Y %H:%M:%S %z')
            except (TypeError, ValueError):
                data_pub = datetime.now()
                print('sem data de publicação')
            hash = hashlib.sha256((titulo + materia + data_pub.strftime('%Y-%m-%d %H:%M:%S') + veiculo).encode()).hexdigest()
            noticia = BronzeNoticia(veiculo = veiculo, titulo = titulo, subtitulo = subtitulo, materia = materia, data_publicacao = data_pub, link = link, categoria = categoria, hash = hash)
            NOTICIAS_BRONZE.append(noticia)
    return NOTICIAS_BRONZE

def salvar_noticias_bronze(lista_noticias):
    for noticia in lista_noticias:
        salvar_noticia_bronze(noticia)

def scrapping_criar_lista_salvar_noticias_bronze(url, categoria):
    salvar_noticias_bronze(criar_lista_noticia_bronze(scrapper(url), categoria))
