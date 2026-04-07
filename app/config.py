import os
from dotenv import load_dotenv

load_dotenv()

# Definisikan base directory (folder root projek)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
BACKUP_DIR = os.getenv("BACKUP_DIR", "backup")

DRIVE_FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

MYSQLDUMP_PATH = os.getenv("MYSQLDUMP_PATH")
