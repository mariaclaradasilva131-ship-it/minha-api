from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def aluno():
    return {
        "matricula": "2024118isinf0020",
        "nome": "Maria Clara"
    }