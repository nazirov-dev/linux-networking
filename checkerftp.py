from ftplib import FTP
import os

# FTP ma'lumotlari
FTP_HOST = "localhost"  # FTP server manzili
FTP_USER = "haady"  # FTP login
FTP_PASS = "haady"  # FTP parol
CHECK_FOLDER = "flag3"  # Tekshiriladigan papka
CHECK_FILE = "payload.txt"  # Tekshiriladigan fayl


def check_and_create_flag():
    try:
        # FTPga ulanamiz
        ftp = FTP(FTP_HOST)
        ftp.login(user=FTP_USER, passwd=FTP_PASS)

        # flag3 papkasiga o'tamiz
        ftp.cwd(CHECK_FOLDER)

        # Papkadagi fayllar ro'yxatini olamiz
        files = ftp.nlst()

        # Fayl mavjudligini tekshiramiz
        if CHECK_FILE in files:
            ftp.quit()
            os.system("echo 'FTP{FTP_Orqali_Yuklash}' > /home/haady/FTP-flag3.txt")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")


if __name__ == "__main__":
    check_and_create_flag()
