from fastapi import FastAPI

app = FastAPI(
    title="LAB9 - API CI/CD",
    description="Aplicacao de demonstracao para pipeline de homologacao e producao.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "API LAB9 funcionando",
        "environment": "container",
        "status": "ok",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
