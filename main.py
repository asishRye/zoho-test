
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, status
import logging


app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
	logging.error(f"{request}: {exc_str}")
	print(exc_str)
	content = {'status_code': 10422, 'message': exc_str, 'data': None}
	
	return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


class Zoho(BaseModel):
	pass
@app.get("/")
def read_root():
	return {"Hello": "World"}


@app.post("/get_data")
async def  get_data(z:Zoho, req: Request):
	a = await req.body()
	print(a)

	return {"OK":"OK"}

