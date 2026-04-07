# MySQL/MariaDB Backup to Google Drive with Telegram Notification

Script Python sederhana untuk melakukan backup database MySQL atau MariaDB secara otomatis, mengompresnya ke format `.gz`, mengunggahnya ke **Google Drive**, dan mengirimkan notifikasi status melalui **Bot Telegram**.

---

## 🚀 Fitur Utama
- **Backup Aman**: Menggunakan `mysqldump` dengan dukungan path kustom.
- **Kompresi Otomatis**: Format `.sql.gz` untuk efisiensi ruang GDrive.
- **Upload Google Drive**: Folder penyimpanan dapat dikonfigurasi via ID.
- **Notifikasi Telegram**: Pesan real-time sukses/gagal di Telegram.
- **Pembersihan Otomatis**: File lokal dihapus setelah berhasil diunggah.
- **Cron Job Ready**: Kinerja stabil saat dijalankan secara otomatis di Linux.

---

## 📋 Konfigurasi Detail (`.env`)
Copy file `.env.example` menjadi `.env` dan lengkapi nilai-nilainya:

| Variabel | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `DB_USER` | Username database MySQL | `root` |
| `DB_PASSWORD` | Password database MySQL | `p@ssword123` |
| `DB_NAME` | Nama database yang ingin di-backup | `my_database` |
| `BACKUP_DIR` | Folder penampung backup lokal (sementara) | `backup` |
| `DRIVE_FOLDER_ID` | ID folder di Google Drive | `10RnPbSvwjqjkQ...` |
| `TELEGRAM_BOT_TOKEN` | Token dari @BotFather | `8284753068:AAGH...` |
| `TELEGRAM_CHAT_ID` | ID chat profil/grup di Telegram | `8451185743` |
| `MYSQLDUMP_PATH` | Path lengkap ke file `mysqldump` | `C:\xampp\mysql\bin\mysqldump.exe` |

---

## 🛠️ Instalasi & Setup

1.  **Clone Repo**:
    ```bash
    git clone https://github.com/fahmiffa/backup_tele_grdive.git
    cd backup_tele_grdive
    ```

2.  **Virtual Environment & Install**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # (Di Windows: venv\Scripts\activate)
    pip install -r requirements.txt
    ```

3.  **Google Drive Authentication**:
    Pastikan `credentials.json` sudah ada di folder utama, lalu jalankan:
    ```bash
    python generate_token.py
    ```
    Ikuti proses login di browser sampai muncul file `token.pickle`.

---

## ⏰ Otomatisasi (Cron Job di Linux)

Untuk menjalankan backup secara otomatis setiap hari jam 12 malam di Linux, ikuti langkah ini:

1.  Buka Crontab:
    ```bash
    crontab -e
    ```

2.  Tambahkan baris berikut di paling bawah (asumsikan folder projek ada di `/home/user/backup_tele_grdive`):
    ```cron
    0 0 * * * cd /home/user/backup_tele_grdive && /home/user/backup_tele_grdive/venv/bin/python3 -m app.main >> /home/user/backup_tele_grdive/backup.log 2>&1
    ```

---

## 🏃 Cara Manual
Jalankan script kapan saja dengan perintah:
```bash
python -m app.main
```

---

## 🛡️ Lisensi
Diterbitkan di bawah Lisensi MIT.
