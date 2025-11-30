from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
OMDB_URL = 'http://www.omdbapi.com/'

if not OMDB_API_KEY:
    print("ERRO CRÍTICO: Chave da API não configurada!")

def buscar_dados_filme(titulo: str):
    params = {'apikey': OMDB_API_KEY, 't': titulo}
    response = requests.get(OMDB_URL, params=params)
    dados = response.json()
    
    if dados.get('Response') == 'False':
        return None
        
    return {
        "titulo": dados.get("Title", "N/A"),
        "ano": dados.get("Year", "N/A"),
        "sinopse": dados.get("Plot", "N/A"),
        "poster": dados.get("Poster", "N/A") 
    }

@app.get("/api/filme")
def api_filme(titulo: str):
    resultado = buscar_dados_filme(titulo)
    if not resultado:
        raise HTTPException(status_code=404, detail="Filme não encontrado.")
    return resultado

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
def buscar_filme_visual(request: Request, nome_filme: str = Form(...)):
    resultado = buscar_dados_filme(nome_filme)
    
    erro = None
    if not resultado:
        erro = "Filme não encontrado! Verifique o nome (tente em inglês)."
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "filme": resultado,
        "erro": erro
    })