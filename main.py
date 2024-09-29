from typing import Union

from fastapi import FastAPI, UploadFile
from model import model_pipeline
from PIL import Image
import io	

# uvicorn main:app --reload -> got to main.py and run app
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ask")
def ask(text: str, image: UploadFile):
    context = image.file.read()
    # image = Image(image.file)
    image = Image.open(io.BytesIO(context))
 
    result = model_pipeline(text, image)
    
    return {
        "answer": result
    }
    
	
	# return model_pipeline(text, image.file)
    