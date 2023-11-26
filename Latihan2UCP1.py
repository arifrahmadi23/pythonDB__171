#1
#Write a PYTHON program to print the natural numbers up to n
def gen_nat_no_while():
    i=1
    n=int(input("enter the limit: "))
    while(i<=n):
        print(i)
        i+=1
gen_nat_no_while()

#2-------------------------------------------------------------------
#Write a PYTHON program to print even numbers up to n
def gen_nat_no_while():
    i=2
    n=int(input("enter the limit: "))
    while(i<=n):
        print(i)
        i+=2
gen_nat_no_while()

#3--------------------------------------------------------------------
#Write a PYTHON program to print odd numbers up to n
def gen_nat_no_while():
    i=1
    n=int(input("enter the limit: "))
    while(i<=n):
        print(i)
        i+=2
gen_nat_no_while()

#4----------------------------------------------------------------------------
# Program Python untuk mencetak jumlah bilangan asli sampai dengan n
# Membaca nilai n
n = int(input("Masukkan nilai n: "))
# Mendeklarasikan variabel untuk menyimpan jumlah
jumlah = 0
# Mencetak bilangan asli hingga n
for i in range(1, n + 1):
    jumlah += i
# Mencetak jumlah
print("Jumlah bilangan asli hingga n adalah", jumlah)

#5.-----------------------------------------------------------------------------
# Program Python untuk menghitung rata-rata
# Membaca nilai n
n = int(input("Masukkan nilai n: "))
# Membaca nilai-nilai
nilai = []
for i in range(n):
    nilai.append(float(input("Masukkan nilai ke-%d: " % (i + 1))))
# Menghitung rata-rata
rata_rata = sum(nilai) / n
# Mencetak rata-rata
print("Rata-rata adalah", rata_rata)

#5----------------------------------------------------------------------------
# Program Python untuk mencetak jumlah bilangan ganjil sampai dengan n
# Membaca nilai n
n = int(input("Masukkan nilai n: "))
# Mendeklarasikan variabel untuk menyimpan jumlah
jumlah = 0
# Mencetak bilangan ganjil hingga n
for i in range(1, n + 1, 2):
    jumlah += i
# Mencetak jumlah
print("Jumlah bilangan ganjil hingga n adalah", jumlah)

#6------------------------------------------------------------------------------
# Program Python untuk mencetak jumlah bilangan genap sampai dengan n
# Membaca nilai n
n = int(input("Masukkan nilai n: "))
# Mendeklarasikan variabel untuk menyimpan jumlah
jumlah = 0
# Mencetak bilangan ganjil hingga n
for i in range(2, n + 1, 2):
    jumlah += i
# Mencetak jumlah
print("Jumlah bilangan ganjil hingga n adalah", jumlah)

#7----------------------------------------------------------------------------------
# Program Python untuk mencetak bilangan asli sampai dengan n dengan urutan terbalik
# Membaca nilai n
n = int(input("Masukkan nilai n: "))
# Mencetak bilangan asli hingga n dengan urutan terbalik
for i in range(n, 0, -1):
    print(i)

#8--------------------------------------------------------------------------------------

