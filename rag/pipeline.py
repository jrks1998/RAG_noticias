from rag.retriever import buscar_contexto
from rag.prompt_builder import montar_prompt
from rag.llm import gerar_resposta
from db.db_utils import get_session

def responder_pergunta(pergunta: str, top_k: int = 8) -> str:
    noticias = buscar_contexto(pergunta, top_k=top_k)
    prompt = montar_prompt(pergunta, noticias)
    return gerar_resposta(prompt)
