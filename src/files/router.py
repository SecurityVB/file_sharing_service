from fastapi import APIRouter, UploadFile

FilesRouter = APIRouter()

@FilesRouter.post("files/upload")
async def upload_file(ufile: UploadFile):
    pass

@FilesRouter.post("files/download/{id}")
async def upload_file(id: str):
    pass