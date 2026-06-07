from db_config import get_connection

try:
    conn = get_connection()
    if conn.is_connected():
        print("Koneksi ke database berhasil!")
    conn.close()
except Exception as e:
    print("Koneksi ke database gagal:", e)
