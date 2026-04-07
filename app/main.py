from app.backup import backup_db
from app.compress import compress_file
from app.upload import upload_file
from app.notify import send_telegram_message
from app.config import DB_NAME
import os
import traceback

def run():
    print("Start backup process...")
    
    try:
        # Step 1: Backup DB
        sql_file = backup_db()
        print(f"Backup created: {sql_file}")

        # Step 2: Compress File
        gz_file = compress_file(sql_file)
        print(f"Compressed: {gz_file}")

        # Step 3: Upload to GDrive
        file_id = upload_file(gz_file)
        print(f"Uploaded to Drive, ID: {file_id}")

        # Optional: delete local files
        os.remove(sql_file)
        os.remove(gz_file)

        # Step 4: Notify Telegram (Success)
        msg = f"<b>✅ Database Backup Success</b>\n" \
              f"<b>Database:</b> {DB_NAME}\n" \
              f"<b>Status:</b> Berhasil diunggah ke GDrive\n" \
              f"<b>Google Drive ID:</b> <code>{file_id}</code>"
        send_telegram_message(msg)
        print("Done ✅")

    except Exception as e:
        # Step 4: Notify Telegram (Error)
        error_msg = f"<b>❌ Database Backup FAILED</b>\n" \
                    f"<b>Database:</b> {DB_NAME}\n" \
                    f"<b>Error:</b> {str(e)}"
        send_telegram_message(error_msg)
        print(f"Error during backup: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    run()