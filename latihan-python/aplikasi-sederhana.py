'''
    1. kalkulator sederhana @
    2. Tebak angka (pake random) @
    3. Konversi Suhu @
    4. Cek Ganjil/Genap @
    5. Hitung luas bangun datar
    6. Hitung Volume bangun ruang
    7. prgram hitung kata
    8. Cek bilangan prima
    9. Kertas gunting batu @
'''

# Note for Update or Bug
# Isi cara main game kuis
# Isi beberapa pertanyaan baru di game kuis
# Tambah try except di input, agar tidak error jika user input string

import random
import time 

# Kuis Start
def main_kuis():
    print("")
    for x in range(29):
        print("=",end='', flush=True)
        time.sleep(0.1)
    print("\n Selamat datang di Game Kuis")
    print(f"{29*"="}")

    while True:
        menu = ["Main", "Cara Main", "Menu Utama"]
        for x, y in enumerate(menu, start=1):
            print(f" {x}. {y}")
            time.sleep(0.3)

        try:
            pilih = int(input("\n Pilihan : "))
            if pilih == 1:
                system_kuis()
                break
            elif pilih == 2:
                how_kuis()
                time.sleep(2)
                input("Tekan [Enter]")
            elif pilih == 3:
                main()
                break
            else:
                print("Silahkan masukan angka yang ada di list")
        except ValueError:
            print("Hanya bisa memasukan angka saja")

def system_kuis():
    pertanyaan = ["Apakah bumi itu bulat?","47 x 11 ="]
    pilihan_ganda = [["A. Tentu saja","B. Mungkin","C. Tidak","D. Tidak tau"],
                     ["A. 417","B. 517","C. 317","D. 442"]]
    kunci_jawaban = ["A","B"]
    jb_benar = 0
    total_soal = len(pertanyaan)

    print("")
    for x, y in enumerate(pertanyaan, start=1):
        z = len(y) + 5
        print(z*"*")
        print(f" {x}. {y}")
        print(z*"*")
        time.sleep(0.5)

        for a in pilihan_ganda[x-1]:
            print(a)
            time.sleep(0.5)

        while True:
            jawab = input("Jawabanmu : ").upper()
            if jawab in ["A","B","C","D"]:
                if jawab == kunci_jawaban[x-1]:
                    print("\nBenar\n")
                    jb_benar += 1
                    break
                else:
                    print(f"\nSalah\nJawabannya adalah {kunci_jawaban[x-1]}\n")
                    break
                break
            else:
                print("\nKamu hanya bisa menjawab A,B,C, dan D")

    time.sleep(1)
    hasil_kuis(jb_benar, total_soal)

def hasil_kuis(skor, total_soal):
    print("*************")
    print("    Hasil    ")
    for i in range(13):
        print("*",end='', flush=True)
        time.sleep(0.1)
    print(f"\nKamu berhasil menjawab benar {skor} dari {total_soal} pertanyaan")    
    print(f"Skormu adalah {(skor/total_soal) * 100}")   
    after_kuis() 

def after_kuis():
    print("\n 1. Main lagi \n 2. Menu Utama \n 3. Keluar Program")
    while True:
        pilihan = int(input("\n Pilihan : "))
        if pilihan == 1:
            main_kuis()
            break
        elif pilihan == 2:
            main()
            break
        elif pilihan == 3:
            print()
            break
        else:
            print("Pilih yang ada di list woi")
    print()

def how_kuis():
    print("Cara main kuis (belum ada, devnya sibuk scroll fesnuk)")
# Kuis End

# Game Kertas Gunting Batu Start
def main_janken():
    print("\n=== Selamat Datang di Permainan Kertas Gunting Batu ===")
    while True:
        print(" 1. Main \n 2. Cara Main \n 3. Menu Utama")
        pilihan = int(input("\nPilihan : "))
        if pilihan == 1:
            system_janken()
            break
        elif pilihan == 2:
            how_janken()
            input("Tekan [Enter]")
        elif pilihan == 3:
            main()
            break
        else:
            print("Input tidak valid")

def system_janken():
    list_janken = ["Batu", "Gunting", "Kertas"]
    skor_player = 0
    skor_komputer = 0

    while True:
        fin = random.choice(list_janken)

        print("\nMana pilihan mu?")
        for x, y in enumerate(list_janken, start=1):
            print(f" {x}. {y}")

        serangan = int(input("\n Silahkan pilih : ")) -1

        if isJankenValid(serangan):
            hasil = hasil_janken(fin, list_janken[serangan])

            time.sleep(0.5)
            if hasil == 1:
                print(f"\n[Komputer] {fin} vs [Kamu]  {list_janken[serangan]}, {list_janken[serangan]} menang")
                skor_player += 1
            elif hasil == 2:
                print(f"\n[Komputer] {fin} vs [Kamu]  {list_janken[serangan]}, {fin} menang")
                skor_komputer += 1
            elif hasil == 3:
                print(f"\n[Komputer] {fin} vs [Kamu]  {list_janken[serangan]}, hasilnya seri")
            else:
                print("gagal")

            time.sleep(0.7)
            if skor_komputer >= 5:
                print(f"\nKamu kalah dengan skor {skor_player} : {skor_komputer}")
                break
            elif skor_player >= 5:
                print(f"\nSelamat kamu menang dengan skor {skor_player} : {skor_komputer}")
                break
            else:
                print(f"\nKomputer {skor_komputer} : {skor_player} Kamu")
                
            time.sleep(1)
        else:
            print("Masukan angka yang tepat yaaa")

    time.sleep(2)
    input("Tekan [Enter]")
    after_janken()

def hasil_janken(system, user):
    if user == "Batu" and system == "Gunting" or user == "Gunting" and system == "Kertas" or user == "Kertas" and system == "Batu":
        return 1
    elif user == system:
        return 3
    else:
        return 2

def how_janken():
    tutor = ["Aku akan memilih secara random antara Batu, Gunting, dan Kertas",
             "Kamu juga harus memilih antara Batu, Gunting, dan Kertas agar bisa mengalahkanku",
             "Jika ada Batu dan Gunting, maka Batu menang",
             "Jika ada Gunting dan Kertas, maka Gunting menang",
             "Jika ada Kertas dan Batu, maka Kertas menang",
             "Jika keduanya memilih pilihan yang sama, maka seri",
             "Kamu akan mendapatkan 1 skor setiap pilihanmu mengalahkanku",
             "Siapa yang mendapakan 5 skor dialah pemenangnya",
             ]
    print("\nCara main : ")
    for x, y in enumerate(tutor, start=1):
        print(f" {x}. {y}")
        time.sleep(0.2)
    print()
    time.sleep(2)

def isJankenValid(a):
    if a in [0,1,2]:
        return True

def after_janken():
    print("\n 1. Main lagi \n 2. Menu Utama \n 3. Keluar Program")
    while True:
        pilihan = int(input("\n Pilihan : "))
        if pilihan == 1:
            main_janken()
            break
        elif pilihan == 2:
            main()
            break
        elif pilihan == 3:
            print()
            break
        else:
            print("Pilih yang ada di list woi")
    print()
# Game Kertas Gunting Batu End

# Cek Ganjil Genap Start
def main_ganjil_genap():
    print("\nCek Ganjil Genap")
    print(" 1. Mulai\n 2. Tentang\n 3. Menu Utama")

    while True:
        pilihan = int(input("\nPilihan : "))
        if pilihan == 1:
            system_ganap()
            break
        elif pilihan == 2:
            about_ganap()
            break
        elif pilihan == 3:
            main()
            break
        else:
            print("Pilihanmu tidak valid, silahkan masukan angka yang ada di list")

def system_ganap():
    while True:
        angka = int(input("\nMasukan Angka : "))
        if angka % 2 == 0:
            print(f"{angka} adalah bilangan genap")
            break
        elif angka % 2 != 0:
            print(f"{angka} adalah bilangan ganjil")
            break
        else:
            print("Harap masukan angka")
    print()
    after_ganap()

def about_ganap():
    print("Ini bagian about (isinya masih kosong bjir, devnya males bikin)")
    input("Tekan [Enter] jika sudah selesai membaca")
    print()

def after_ganap():
    time.sleep(2)
    print("\n 1. Ulangi \n 2. Menu Utama \n 3. Keluar Program")
    while True:
        pilihan = int(input("\n Pilihan : "))
        if pilihan == 1:
            main_ganjil_genap()
            break
        elif pilihan == 2:
            main()
            break
        elif pilihan == 3:
            print()
            break
        else:
            print("Pilih yang ada di list woi")
    print()
# Cek Ganjil Genap End

#Konversi Suhu Start
def main_suhu():
    menu_suhu()

    while True:
        pilihan = int(input("\nSilahkan masukan pilihan anda : "))
        if pilihan == 0:
            main()
            break
        elif pilihan in [1,2,3,4,5,6,7,8,9,10,11,12]:
            suhu = float(input("Suhu : "))
            if pilihan in [1,2,3]:
                hasil = operasi_suhu_celcius(pilihan, suhu)
                print("\nCelcius : ", suhu,"°C")
                break
            elif pilihan in [4,5,6]:
                hasil = operasi_suhu_fahrenheit(pilihan, suhu)
                print("\nFahrenheit : ", suhu,"°F")
                break
            elif pilihan in [7,8,9]:
                hasil = operasi_suhu_kelvin(pilihan, suhu)
                print("\nKelvin : ", suhu,"K")
                break
            elif pilihan in [10,11,12]:
                hasil = operasi_suhu_reamur(pilihan, suhu)
                print("\nReamur : ", suhu,"°Ré")
                break

        else:
            print("Pilihan anda tidak valid, mohon masukan angka yang ada di list")

    print(hasil,"\n")
    after_suhu()

            
def after_suhu():
    time.sleep(1)
    print("\n 1. Coba lagi\n 2. Menu Utama\n 3. Keluar Program")

    while True:
        jwb = int(input("\nPilihan : "))
        if jwb == 1:
            main_suhu()
            break
        elif jwb == 2:
            main()
            break
        elif jwb == 3:
            print()
            break
        else:
            print("Input tidak valid")

def operasi_suhu_celcius(pilihan, c):
    # Fahrem, kelv, re
    if pilihan == 1:
        konversi = (c * (9/5)) + 32
        suhu = ["Fahrenheit","°F"]
    elif pilihan == 2:
        konversi = c + 273.15
        suhu = ["Kelvin", "K"]
    elif pilihan == 3:
        konversi = c * (4/5)
        suhu = ["Reamur", "°Ré"]

    hasil_akhir = f"{suhu[0]}, : {konversi} {suhu[1]}"
    return hasil_akhir
        
def operasi_suhu_fahrenheit(pilihan, f):
    if pilihan == 4:
        konversi = (f - 32) * (5/9)
        suhu = ["Celcius","°C"]
    elif pilihan == 5:
        konversi = (f -32) * (5/9) + 273.15
        suhu = ["Kelvin", "K"]
    elif pilihan == 6:
        konversi = (f - 32) * (4/9)
        suhu = ["Reamur", "°Ré"]

    hasil_akhir = f"{suhu[0]}, : {konversi} {suhu[1]}"
    return hasil_akhir

def operasi_suhu_kelvin(pilihan, k):
    if pilihan == 7:
        konversi = k - 273.15
        suhu = ["Celcius","°C"]
    elif pilihan == 8:
        konversi = (k - 273.15) * (9/5) + 32
        suhu = ["Fahrenheit","°F"]
    elif pilihan == 9:
        konversi = (k - 273.15) * (4/5)
        suhu = ["Reamur", "°Ré"]

    hasil_akhir = f"{suhu[0]}, : {konversi} {suhu[1]}"
    return hasil_akhir

def operasi_suhu_reamur(pilihan, re):
    if pilihan == 10:
        konversi = re * (5/4)
        suhu = ["Celcius","°C"]
    elif pilihan == 11:
        konversi = (re * (9/4)) + 32
        suhu = ["Fahrenheit","°F"]
    elif pilihan == 12:
        konversi = (re * (5/4)) + 273.15
        suhu = ["Kelvin", "K"]
        
    hasil_akhir = f"{suhu[0]}, : {konversi} {suhu[1]}"
    return hasil_akhir

def menu_suhu():
    list_suhu = ["Celcius ke Fahrenheit", "Celcius ke Kelvin", "Celcius ke Reamur",
            "Fahrenheit ke Celcius", "Fahrenheit ke Kelvin", "Fahrenheit ke Reamur",
            "Kelvin ke Celcius", "Kelvin ke Fahrenheit", "Kelvin ke Reamur",
            "Reamur ke Celcius", "Reamur ke Fahrenheit", "Reamur ke Kelvin"]
    print("\n===== Konversi Suhu =====")
    for x, y in enumerate(list_suhu, start=1):
        print(f" {x}. {y}")
        time.sleep(0.2)
    print("0. Kembali")
# Konversi Suhu End

# Tebak Angka Start
def random_game():
    print("\nSelamat datang di Game Tebak Angka")
    while True:
        print(" 1. Main\n 2. Cara Main\n 3. Kembali")
        pilih = int(input("\nPilihan : "))

        if pilih == 1:
            play_random_game()
            break
        elif pilih == 2:
            how_random_game()
        elif pilih == 3:
            main()
            break
        else:
            print("Input tidak valid, hanya bisa memasukan angka yang ada di list")

def kalah_random_game():
    kalah = [r"（￣へ￣）ゞ Yahh... sepertinya kamu belum berhasil kali ini.",
             r"(￣ヘ￣;) kamu kalah... hmm.",
             r"(ーー;) yah kalah yaa...",
             r"(・・;)ゞ kamu kalah... coba lagi deh.",
             r"（︶^︶） Hmmm... kamu kalah. Tapi nggak apa-apa, semua orang juga pernah kok.",
             r"(*￣ー￣)ノ Yahh kamu kalah... aku udah duga sih, tapi tetep semangat ya~"]
    i = random.randint(0, 5)
    print()
    print(kalah[i])    
    after_random()

def selamat_random_game():
    kata_selamat = [r"(＾▽＾)／★☆ Selamaaaat! ☆★＼(＾▽＾)",
                    r"☆*:.｡.o(≧▽≦)o.｡.:*☆ Selamat atas pencapaiannya!",
                    r"＼(＾▽＾)／ Waaa~ Selamat yaa!",
                    r"ヽ(〃＾▽＾〃)ﾉ Kamu keren! Selamat!",
                    r"｡ﾟ+.(･∀･)ﾟ+.ﾟ Yeay! Kamu berhasil~",
                    r"\(^ω^\ ) Congrats~ ( /^ω^)/"]
    i = random.randint(0, 5)
    print()
    print(kata_selamat[i])
    after_random()

def play_random_game():
    angka_sebenarnya = random.randint(1, 100)
    salah = 0

    while True:
        if cek_nyawa(salah):
            kalah_random_game()
            break
        else:
            jawab = int(input("\nApakah kamu bisa menebak angka rahasia ini? Pilihanmu adalah .. "))
            if jawab > angka_sebenarnya:
                salah += 1
                print(f"\n{jawab} ya, sayangnya itu kebanyakan")
            elif jawab < angka_sebenarnya:
                salah += 1
                print(f"\n{jawab}? Kurang deh kayaknya")
            else:
                selamat_random_game()
                break
        
        if 7 - salah != 0:
            print("Kamu punya",7 - salah,"kesempatan lagi")

def cek_nyawa(salah):
    if salah >= 7:
        return True
    
    return False

def after_random():
    time.sleep(2)
    jwb = input("\nApakah mau main lagi? [Y/N] ").lower()

    if jwb == "y":
        play_random_game()
    elif jwb== "n":
        random_game()
    else:
        print("Input tidak valid")
        main()

def how_random_game():
    print("\nCara Main : \n 1. Sistem akan memilih angka random dari 1-100")
    print(" 2. Kamu harus menebak angka yang dipilih sistem")
    print(" 3. Jika angka pilihanmu lebih besar dari angka sebenarnya, system akan memberi pesan \"Kebanyakan kak\"")
    print(" 4. Sedangkan jika angka pilihanmu lebih kecil dari angka sebenarnya, system akan memberi pesan \"Kurang deh kayaknya\"")
    print(" 5. Kalau kamu berhasil menebak angkanya, kamu akan diberi ucapan selamat")
    print(" 6. Ingat kamu cuman punya 7 Kesempatan lohh")
    print(r"Selamat bermain, semoga beruntung (＾ｗ＾)b")
    time.sleep(2)
    input("Tekan [Enter] jika sudah selesai membaca")
    print()
# Tebak Angka End

# Kalkulator sederhana Start
def main_kalku():
    list_ak = ["Penjumlahan", "Pengurangan","Perkalian","Pembagian","Menu Utama"]

    print("\n == Kalkulator Sederhana == ")
    for x, y in enumerate(list_ak, start=1) :
        print(f" {x}. {y}")
        time.sleep(0.1)
    print(" 0. Keluar")
    pilih = int(input("\nPilihan : "))
    system_kalkulator(pilih)
    print()

def system_kalkulator (pilih):
    while True:
        if pilih in [1,2,3,4]:
            a = int(input("\nAngka Pertama : "))
            b = int(input("Angka Kedua : "))

        if pilih == 1:
            print(f"\n{a} + {b} = {a+b}")
        elif pilih == 2:
            print(f"\n{a} - {b} = {a-b}")
        elif pilih == 3:
            print(f"\n{a} x {b} = {a*b}")
        elif pilih == 4:
            if b == 0:
                print("\nAngka tidak bisa dibagi 0\n")
            else:
                print(f"\n{a} / {b} = {a/b}")
        elif pilih == 5:
            main()
            break
        elif pilih == 0:
            break

        print("\n1. Ulangi\n2. Menu Utama\n0. Keluar")
        pilihan =  int(input("\nPilihan : "))

        if pilihan == 1:
            main_kalku()
            break
        elif pilihan == 2:
            main()
            break
        elif pilihan == 0:
            break
        else:
            print("Input tidak valid, hanya bisa memasukan angka yang ada di list")
# Kalkulator Sederhana End


def main():
    list_apk = ["Kalkulator",
                "Game Tebak Angka",
                "Konversi Suhu",
                "Cek Angka Ganjil Genap",
                "Kertas Gunting Batu",
                "Kuis Sederhana",]
    print("\nList Aplikasi : ")
    for x, y in enumerate(list_apk, start=1):
        print(f" {x}. {y}")
        time.sleep(0.3)
    print(" 0. Keluar\n")
    
    while True:
        pilihan = int(input("Pilihan : "))
        
        if pilihan == 1:
            main_kalku()
            break
        elif pilihan == 2:
            random_game()
            break
        elif pilihan == 3:
            main_suhu()
            break
        elif pilihan == 4:
            main_ganjil_genap()
            break
        elif pilihan == 5:
            main_janken()
            break
        elif pilihan == 6:
            main_kuis()
            break
        elif pilihan == 0:
            break
        else:
            print("\nPilihan tidak valid, silahkan masukan angka yang tersedia di list!!\n")

main()