def penjumlahan (a, b):
  hasil = a + b
  print(f"{a} + {b} = {hasil}")

def pengurangan (a,b):
  hasil = a - b
  print(f"{a} - {b} = {hasil}")
  
def perkalian (a,b):
  hasil = a * b
  print(f"{a} x {b} = {hasil}")
  
def pembagian(a, b):
  hasil = a /b
  print(f"{a} / {b} = {hasil}")
  
print("1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian")
pilihan = int(input())
x = int(input("Angka ke-1 : "))
y = int(input("Angka ke-2 : "))

if pilihan == 1:
  penjumlahan(x,y)
elif pilihan == 2:
  pengurangan(x,y)
elif pilihan == 3:
  perkalian(x,y)
elif pilihan == 4:
  pembagian(x,y)
else:
  print("Pilihan anda tidak valid!!")