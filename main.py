
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Zoho(BaseModel):
    interviewer_id: str 
    interviewer_email: str 

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/get_data")
def get_data(z:Zoho):
    print(z)
    return {"OK":"OK"}

