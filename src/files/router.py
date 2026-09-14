import hashlib
import time

from fastapi import APIRouter, UploadFile

from src.files.config import UFILES_DIR


FilesRouter = APIRouter()

@FilesRouter.post("/files/upload")
async def upload_file(ufiles: list[UploadFile]):
    id_dir = hashlib.md5(str(time.time()).encode("utf-8")).hexdigest()
    directory = UFILES_DIR / id_dir
    for ufile in ufiles:
        file = ufile.file
        filename = ufile.filename
        directory.mkdir(parents=True, exist_ok=True)
        with open(directory / filename, 'wb') as f:
            f.write(file.read())

@FilesRouter.post("/files/download/{id}")
async def upload_file(id: str):
    pass