import re

# Fungsi sederhana untuk mendeteksi email, nomor telepon, atau alamat
def deteksi_privasi(teks):
    hasil = {
        "email": re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", teks),
        "nomor_telepon": re.findall(r"\b\d{10,15}\b", teks),
        "alamat": re.findall(r"\b\d{1,4}\s\w+\s\w+", teks)
    }
    return hasil

# Contoh teks dokumen
dokumen = """
    Nama: John Doe
    Email: john.doe@example.com
    Nomor Telepon: 081234567890
    Alamat: 1234 Elm Street
"""

# Deteksi data sensitif
hasil = deteksi_privasi(dokumen)

# Tampilkan hasil
print("Data sensitif yang ditemukan:")
for tipe, nilai in hasil.items():
    print(f"{tipe.capitalize()}: {', '.join(nilai) if nilai else 'Tidak ditemukan'}")
