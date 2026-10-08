from models.noticia import BronzeNoticia, SilverNoticia, GoldNoticia
import re
from db.db_utils import listar_noticias_bronze, listar_noticias_silver, salvar_noticia_silver, salvar_noticia_gold
import json

def limpar_materia_bronze(noticia_bronze: BronzeNoticia):
    materia = noticia_bronze.materia
    materia = re.sub(r'<.*?>', '', materia).strip()
    if materia == '':
        return 'SEM MATERIA'

    return {
        'veiculo': noticia_bronze.veiculo.strip().upper(),
        'titulo': noticia_bronze.titulo.strip().upper(),
        'subtitulo': noticia_bronze.subtitulo.strip().upper(),
        'materia': materia.strip().upper(),
        'data_publicacao': noticia_bronze.data_publicacao,
        'link': noticia_bronze.link.strip().upper(),
        'categoria': noticia_bronze.categoria.strip().upper(),
        'hash': noticia_bronze.hash.strip()
    }

def transformar_dt_bronze_para_silver(data_bronze):
    return data_bronze.replace(microsecond = 0)

def converter_para_silver(noticia_bronze: BronzeNoticia):
    dados = limpar_materia_bronze(noticia_bronze)
    if dados != 'SEM MATERIA':
        dados['data_publicacao'] = transformar_dt_bronze_para_silver(dados['data_publicacao'])
        return SilverNoticia(**dados)
    return None

def converter_para_gold(noticia_silver: SilverNoticia):
    from etl.nlp_utils import gerar_embedding, gerar_resumo, gerar_tags, extrair_entidades
    
    embedding = gerar_embedding(f'{noticia_silver.titulo} {noticia_silver.materia}')
    resumo = gerar_resumo(noticia_silver.materia)
    tags = gerar_tags(noticia_silver.materia)
    entidades = extrair_entidades(noticia_silver.materia)
    tags_enriquecidas = list(set(tags + entidades))

    return GoldNoticia(
        veiculo = noticia_silver.veiculo,
        titulo = noticia_silver.titulo,
        materia = noticia_silver.materia,
        data_publicacao = noticia_silver.data_publicacao,
        link = noticia_silver.link,
        categoria = noticia_silver.categoria,
        hash = noticia_silver.hash,
        embedding = json.dumps(embedding),
        resumo = resumo,
        tags = ','.join(tags_enriquecidas)
    )

def bronze_para_silver():
    bronze_noticias = listar_noticias_bronze()
    for noticia in bronze_noticias:
        silver = converter_para_silver(noticia)
        if silver != None:
            salvar_noticia_silver(silver)

def silver_para_ouro():
    silver_noticias = listar_noticias_silver()
    for noticia in silver_noticias:
        gold = converter_para_gold(noticia)
        salvar_noticia_gold(gold)