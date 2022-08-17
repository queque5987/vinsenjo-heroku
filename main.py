from fastapi import FastAPI
app = FastAPI()
{
    "message": "Hello world"
}

@app.get("/")
def hello():
    return {"message":"Hello world"}