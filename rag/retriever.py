import numpy as np, json
from etl.nlp_utils import gerar_embedding
from db.db_utils import listar_noticias_gold
import json

def buscar_contexto(input, top_k=10):
    input = input.upper()
    emb_input = np.array(gerar_embedding(input))
    noticias = listar_noticias_gold()
    resultados = []
    for n in noticias:
        emb_noticia = np.array(json.loads(n.embedding))
        if emb_noticia.size == 0:
            continue
        score = np.dot(emb_input, emb_noticia) / (np.linalg.norm(emb_input) * np.linalg.norm(emb_noticia))
        resultados.append((score, n))
    resultados.sort(key=lambda x: x[0], reverse=True)
    return [n for _, n in resultados[:top_k]]
