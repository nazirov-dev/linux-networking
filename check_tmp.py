import os


def check_and_create_file():
    # Tekshiriladigan fayl yo'li
    payload_path = "/tmp/payload.txt"
    target_path = "/home/suxrob/SSH{Yuklama_Joylashtirildi}"

    # Agar payload mavjud bo'lsa
    if os.path.exists(payload_path):
        # Maqsad fayl yaratish
        with open(target_path, "w") as f:
            f.write("SSH{Yuklama_Joylashtirildi}")

        # Payload faylini o'chirish
        os.remove(payload_path)


if __name__ == "__main__":
    check_and_create_file()
