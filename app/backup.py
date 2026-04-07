import os
import datetime
from app.config import DB_USER, DB_PASSWORD, BACKUP_DIR, MYSQLDUMP_PATH

def backup_db(db_name):
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{db_name}_{timestamp}.sql"
    filepath = os.path.join(BACKUP_DIR, filename)

    # Menggunakan custom path jika ada di .env, jika tidak pakai command default
    dump_bin = MYSQLDUMP_PATH if MYSQLDUMP_PATH else "mysqldump"

    command = (
        f'"{dump_bin}" -u{DB_USER} -p{DB_PASSWORD} '
        f"--single-transaction --quick --lock-tables=false "
        f"{db_name} > {filepath}"
    )

    result = os.system(command)

    if result != 0:
        raise Exception(f"Backup gagal untuk database: {db_name}. Pastikan database aktif dan path {dump_bin} benar.")

    return filepath
