from fastapi import FastAPI

app = FastAPI(title="Learn GitHub Actions API")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}


@app.get("/health")
def read_health() -> dict[str, str]:
    return {"status": "ok"}


def inc(x: int) -> int:
    return x + 1
