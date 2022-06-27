
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Zoho(BaseModel):
    data:str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/get_data")
def get_data(z:Zoho):
    print(z)
    return {"OK":"OK"}

