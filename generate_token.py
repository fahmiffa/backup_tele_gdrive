import os.path
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Scope yang dibutuhkan untuk mengunggah file ke Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    creds = None
    # Mengecek apakah token.pickle sudah ada
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Jika tidak ada token (belum login) atau token tidak valid
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Menggunakan credentials.json yang sudah ada di folder Anda
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            
            # Menggunakan console flow agar lebih stabil di beberapa lingkungan
            creds = flow.run_local_server(port=0, open_browser=True)

        
        # Menyimpan token ke file token.pickle
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
        
    print("✅ Berhasil men-generate token.pickle!")

if __name__ == '__main__':
    main()
