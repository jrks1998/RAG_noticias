import requests as rr
import json

MODEL_ID = 'qwen3.8:27b'
URL = 'http://localhost:11434/api/chat'

def gerar_resposta(prompt: str, max_tokens: int = 5000, mostrar_thinking: bool = True) -> str:
    payload = {
        'model': MODEL_ID,
        'messages': [
            {
                'role': 'user',
                'content': prompt
            }
        ],
        'stream': True,
        'think': True,
        'options': {
            'num_predict': max_tokens,
            'temperature': 0.2
        }
    }
    dentro_thinking = False
    resp = rr.post(URL, json = payload, stream = True)

    for linha in resp.iter_lines():
        if linha:
            chunk = json.loads(linha)
            msg = chunk.get('message', {})

            thinking = msg.get('thinking', '')
            if thinking and mostrar_thinking:
                if not dentro_thinking:
                    print('\n[THINKING] ', end='', flush=True)
                    dentro_thinking = True
                print(thinking, end='', flush=True)

            token = msg.get('content', '')
            if token:
                if dentro_thinking:
                    print('\n[RESPOSTA] ', end='', flush=True)
                    dentro_thinking = False
                print(token, end='', flush=True)

            if chunk.get('done'):
                break
    print()
