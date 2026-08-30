from fastapi import FastAPI

app = FastAPI(
    title="SecureShop API",
    description="SecureShop backend for the SecureCloud DevSecOps project",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "secureshop-api",
    }
