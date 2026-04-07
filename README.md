# MySQL/MariaDB Backup to Google Drive with Telegram Notification

Script Python sederhana untuk melakukan backup database MySQL atau MariaDB secara otomatis, mengompresnya ke format `.gz`, mengunggahnya ke **Google Drive**, dan mengirimkan notifikasi status melalui **Bot Telegram**.

---

## 🚀 Fitur Utama
- **Backup Aman**: Menggunakan `mysqldump`.
- **Kompresi**: Format `.sql.gz` untuk menghemat ruang Drive.
- **Upload Google Drive**: Otomatis masuk ke folder pilihan Anda.
- **Notifikasi Telegram**: Pesan real-time jika backup berhasil atau gagal.
- **Pembersihan Otomatis**: Menghapus file backup lokal setelah berhasil diunggah.

---

## 📋 Prasyarat
- Python 3.x
- MySQL/MariaDB Server
- Akun Google (untuk Google Drive API)
- Bot Telegram (lewat @BotFather)

---

## 🛠️ Cara Instalasi

1.  **Clone Repository**:
    ```bash
    git clone https://github.com/username/repo-name.git
    cd repo-name
    ```

2.  **Buat Virtual Environment** (Opsional tapi disarankan):
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install Dependensi**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Konfigurasi `.env`**:
    Copy file `.env.example` menjadi `.env` dan isi sesuai kredensial Anda.

5.  **Setup Google Drive API**:
    - Siapkan file `credentials.json` dari Google Cloud Console.
    - Jalankan `python generate_token.py` untuk mendapatkan akses.

---

## 🏃 Cara Menjalankan

Lakukan backup manual dengan perintah:
```bash
python -m app.main
```

---

## 🛡️ Lisensi
Distributed under the MIT License.
