# 🎬 Sistema de Consulta de Filmes (OMDB API)

Projeto desenvolvido como requisito avaliativo para a disciplina de **Introdução à Programação em Python** no curso de **Sistemas para Internet** (UNIVALI).

O sistema consiste em uma aplicação web híbrida que consome a API pública da OMDb (Open Movie Database).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.13+
- **Framework Web:** FastAPI
- **Servidor:** Uvicorn
- **Requisições HTTP:** Requests
- **Template Engine:** Jinja2
- **Estilização:** Tailwind CSS (via CDN)
- **Gerenciamento de Ambiente:** Python-dotenv

---

## 📦 Instalação e Configuração

Siga os passos abaixo para rodar o projeto localmente.

### 1. Instale as dependências

Certifique-se de estar na pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

### 2. Configuração da Chave de API (Importante!)

Este projeto utiliza variáveis de ambiente para segurança. Você precisa de uma chave gratuita da [OMDb API](http://www.omdbapi.com/apikey.aspx).

- Crie um arquivo chamado .env na raiz do projeto (mesmo nível do main.py).

- Adicione o seguinte conteúdo, substituindo pela sua chave (sem aspas e sem espaços extras):

```bash
OMDB_API_KEY=sua_chave_aqui
```

Nota: O arquivo .env contém credenciais sensíveis e não está incluído no repositório. Utilize o arquivo .env.example como referência.

---

## ▶️ Como Executar

Com as dependências instaladas e o .env configurado, execute:

```bash
uvicorn main:app --reload
```

O servidor iniciará em http://127.0.0.1:8000.

---

## 📡 Endpoints e Uso

### 1. Interface Web
Acesse http://127.0.0.1:8000/ no seu navegador.

- Digite o nome do filme (ex: Batman).

- O sistema exibirá o pôster e as informações formatadas.

### 2. API JSON
Faça uma requisição GET para a rota de API:

- **URL:** http://127.0.0.1:8000/api/filme?titulo=Batman

**Exemplo de Resposta (JSON):**

```bash
{
  "titulo": "Batman",
  "ano": "1989",
  "sinopse": "The Dark Knight of Gotham City begins his war on crime...",
  "poster": "[https://m.media-amazon.com/images/](https://m.media-amazon.com/images/)..."
}
```

### 3. Documentação Automática (Swagger UI)
O FastAPI gera documentação automática e interativa. 

Acesse http://127.0.0.1:8000/docs para consultar a documentação.
