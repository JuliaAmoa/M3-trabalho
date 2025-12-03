"""Como usar
1. Instale dependências: pip install -r requirements.txt
2. Defina a variável OMDB_API_KEY (ou crie .env com OMDB_API_KEY=sua_chave)
3. Rode: uvicorn app.main:app --reload --port 8000"""

from typing import Any, Dict

import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query

# Carrega .env
load_dotenv()

OMDB_URL: str = "http://www.omdbapi.com/"
OMDB_KEY = os.getenv("OMDB_API_KEY")


app: FastAPI = FastAPI(title="Consulta de Filmes (OMDb)")


def _fetch_from_omdb(title: str) -> Dict[str, Any]:
    """Faz a requisição ao OMDb e retorna o JSON decodificado.

    Lança requests.exceptions.RequestException em caso de erro de rede/HTTP."""
    params: Dict[str, str] = {"apikey": OMDB_KEY or "", "t": title, "plot": "full", "r": "json"}
    resp = requests.get(OMDB_URL, params=params, timeout=8)
    resp.raise_for_status()
    return resp.json()


@app.get("/filme")
def filme(titulo: str = Query(..., min_length=1)) -> Dict[str, str]:
    """Endpoint GET /filme

    Parametros de Query
    - titulo: título do filme a ser consultado (obrigatório)

    Retorna um dicionário com as chaves:
    - titulo: título do filme
    - ano: ano de lançamento
    - sinopse: sinopse completa (plot)"""
    if OMDB_KEY is None:
        raise HTTPException(status_code=500, detail="OMDB_API_KEY não configurada")

    try:
        data: Dict[str, Any] = _fetch_from_omdb(titulo)
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Timeout ao consultar OMDb")
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="Erro ao consultar OMDb")

    if data.get("Response") == "False":
        raise HTTPException(status_code=404, detail=data.get("Error", "Filme não encontrado"))

    return {
        "titulo": data.get("Title", ""),
        "ano": data.get("Year", ""),
        "sinopse": data.get("Plot", ""),
    }
