import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
from fastapi.responses import JSONResponse

from schemas import UploadData
from uploader import DriveUploader

# Load the .env file
load_dotenv(".env")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

drive_uploader = DriveUploader()


@app.post("/upload_to_drive")
def Upload(upload_data: UploadData):

    file_path = upload_data.FilePath

    if not os.path.isfile(file_path):
        return JSONResponse({"status": "error", "message": "file does not exist"},
                            status_code=404)

    uploaded_id = drive_uploader.upload_to_drive(file_path)
    if uploaded_id:
        return JSONResponse({"status": "success", "message": "file uploaded successfully", "id": uploaded_id},
                            status_code=201)

    return JSONResponse({"status": "error", "message": "file upload failed"},
                        status_code=500)
