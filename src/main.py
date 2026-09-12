from fastapi import FastAPI

from src.files.router import FilesRouter


app = FastAPI()

app.include_router(FilesRouter)