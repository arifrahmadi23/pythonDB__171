def makanan():
    global totalMakan, jumlahPorsi, namaMakanan

def minuman():
    global totalMinum, jumlahGelas, namaMinuman

print("|===================================|")
print("|                MENU               |")
print("|===================================|")
print("|            MENU MAKANAN           |")
print("|===================================|")
print("| 1. Oseng Ayam          RP.11.000  |")
print("| 2. Ayam Geprek         RP.11.000  |")
print("| 3. Ayam Bali           RP.11.000  |")
print("| 4. Ayam Surundeng      RP.11.000  |")
print("| 5. Ayam Penyet         RP.11.000  |")
print("|===================================|")
menuMakanan = int(input("1/2/3/4/5 : "))
jumlahPorsi = int(input("Berapa Posrsi : "))

if menuMakanan == 1:
    totalMakanan = jumlahPorsi * 11000
    print ("")


