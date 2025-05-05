import os
import argparse
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
from fastapi.responses import JSONResponse

from schemas import UploadData
from uploader import DriveUploader

parser = argparse.ArgumentParser()
parser.add_argument("--env-file", type=str, required=True,
                    help="Path to .env file")
args = parser.parse_args()

load_dotenv(dotenv_path=args.env_file)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

drive_uploader = DriveUploader()


@app.get("/check")
def Check():
    return JSONResponse({"message": "running"})


@app.post("/upload_to_drive")
def Upload(upload_data: UploadData):

    file_path = upload_data.FilePath

    if not file_path.startswith(os.getenv("HOME")):
        return JSONResponse({"status": "error", "message": "Invalid Path (not home)"}, status_code=400)

    if not os.path.isfile(file_path):
        return JSONResponse({"status": "error", "message": "file does not exist"},
                            status_code=404)

    _, extension = os.path.splitext(file_path)
    if extension != ".docx":
        return JSONResponse({"status": "error", "message": "only docx format is allowed "}, status_code=400)

    uploaded_id = drive_uploader.upload_to_drive(file_path)
    if uploaded_id:
        return JSONResponse({"status": "success", "message": "file uploaded successfully", "id": uploaded_id},
                            status_code=201)

    return JSONResponse({"status": "error", "message": "file upload failed"},
                        status_code=500)


if __name__ == "__main__":
    uvicorn.run("main:app", port=int(os.getenv("PORT", 8000)))
