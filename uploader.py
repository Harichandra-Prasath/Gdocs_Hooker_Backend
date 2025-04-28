import os

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


SCOPE = ['https://www.googleapis.com/auth/drive']


class DriveUploader:
    def __init__(self):
        creds = service_account.Credentials.from_service_account_file(
            os.getenv("GOOGLE_CREDS_JSON"), scopes=SCOPE)
        self.Service = build('drive', 'v3', credentials=creds)

    def upload_to_drive(self, upload_path: str):

        name = upload_path.split("/")[-1]

        try:
            file_metadata = {'name': name,
                             'mimeType': 'application/vnd.google-apps.document',
                             'parents': [os.getenv("SHARED_FOLDER_ID")],
                             }

            media = MediaFileUpload(upload_path)

            file = self.Service.files().create(
                body=file_metadata, media_body=media, fields='id',
                supportsAllDrives=True).execute()

            return file.get("id")

        except HttpError as error:
            print(f"An error occured during uploading {error}")

        return None
