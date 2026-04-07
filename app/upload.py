import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from app.config import DRIVE_FOLDER_ID

def upload_file(file_path):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': file_path.split("/")[-1]
    }

    if DRIVE_FOLDER_ID:
        file_metadata['parents'] = [DRIVE_FOLDER_ID]

    media = MediaFileUpload(file_path, resumable=True)

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    return file.get('id')