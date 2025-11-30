import os

folder = "/home"

hapus_kata = "[Kusonime] "

for nama_file in os.listdir(folder):
    if hapus_kata in nama_file:
        nama_baru = nama_file.replace(hapus_kata, "",1)
        path_lama = os.path.join(folder, nama_file)
        path_baru = os.path.join(folder, nama_baru)

        os.rename(path_lama, path_baru)
        print(f"{nama_file} --> {nama_baru}")

print("Beres cuyyy")