import torch
import spacy
from keybert import KeyBERT
import os
os.environ['HF_HUB_OFFLINE'] = '1'
from sentence_transformers import SentenceTransformer
from transformers import pipeline

model = SentenceTransformer('BAAI/bge-m3')
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = model.to(device)
summarizer = pipeline('text-generation', model = 'facebook/bart-large-cnn', device = 'cuda')
nlp = spacy.load('pt_core_news_sm')
keybert = KeyBERT()

def gerar_embedding(texto: str):
    if not texto or not texto.strip():
        return []
    vetor = model.encode(texto)
    return vetor.tolist()

def gerar_resumo(texto):
    if not texto or not texto.strip():
        return ''
    resumo = summarizer(texto, max_length = 100, min_length = 30, do_sample = False)
    return resumo[0]['generated_text']

def gerar_tags(texto):
    if not texto or not texto.strip():
        return []
    keywords = keybert.extract_keywords(texto, top_n = 5)
    return [kw for kw, score in keywords]

def extrair_entidades(texto):
    doc = nlp(texto)
    return [ent.text for ent in doc.ents]