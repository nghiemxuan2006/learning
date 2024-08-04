from typing import Union
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os, shutil
FOLDER_PATH = os.getenv('FOLDER_PATH', '')
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def getRoot():
    return {"message": "File saved successfully"}


@app.post("/upload/")
async def uploadfile(file: UploadFile):
    try:
        file_path = os.path.join(FOLDER_PATH,file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return {"message": "File saved successfully"}
    except Exception as e:
        return {"message": e.args}