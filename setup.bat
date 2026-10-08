@echo off
echo Setup automático
echo [1/6] criar venv
python -m venv venv
if %errorlevel% neq 0 (
    echo [ERRO] falha ao criar venv. verifique se o python esta instalado e adicionado ao PATH como "python"
    pause
    exit /b 1
)
echo [2/6] ativar o venv
set "VENV_PYTHON=venv\Scripts\python.exe"
set "VENV_PIP=venv\Scripts\pip.exe"
if %errorlevel% neq 0 (
    echo [ERRO] falha ao ativar venv
    pause
    exit /b 1
)
echo [3/6] instalar dependências
"%VENV_PIP%" install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERRO] falha ao instalar dependencias. verifique se o pip esta instalado e adicionado ao PATH como "pip"
    pause
    exit /b 1
)
echo [4/6] instalar o modelo SpaCy (pt-BR)
"%VENV_PYTHON%" -m spacy download pt_core_news_sm
if %errorlevel% neq 0 (
    echo [ERRO] falha ao instalar modelo ScaPy. verifique se o python esta instalado e adicionado ao PATH como "python"
    pause
    exit /b 1
)
echo [5/6] baixar modelos HuggingFace
set "HF_CLI=venv\Scripts\hf.exe"
%HF_CLI% download BAAI/bge-m3
%HF_CLI% download facebook/bart-large-cnn
if %errorlevel% neq 0 (
    echo [ERRO] falha ao baixar modelos HuggingFace
    pause
    exit /b 1
)
echo [6/6] baixar modelo Ollama
ollama pull qwen3.8:27b
if %errorlevel% neq 0 (
    echo [ERRO] falha ao baixar modelo Ollama. verifique se o Ollama esta instalado e adicionado ao PATH como "ollama"
    pause
    exit /b 1
)