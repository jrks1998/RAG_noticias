from models.noticia import GoldNoticia

def montar_prompt(pergunta: str, noticias: list[GoldNoticia]) -> str:
    contexto = []
    noticias.sort(key = lambda n: n.data_publicacao, reverse = True) # ordenando as notícias por data de publicação. a ideia é ter as notícias mais recentes na frente
    for n in noticias:
        trecho = (
            f"Título: {n.titulo}\nResumo: {n.resumo}\nCategoria: {n.categoria}\nLink: {n.link}\nData Publicação: {n.data_publicacao}"
        )
        contexto.append(trecho)

    contexto_str = "\n\n".join(contexto)

    prompt = (
        f"você é um assistente especializado em análise de notícias.\n\n"
        f"a seguir estão algumas notícias relevantes:\n{contexto_str}\n\n"
        f"pergunta: {pergunta}\n\n"
        f"com base nas notícias acima, forneça uma resposta clara, objetiva e contextualizada."
    )

    return prompt
