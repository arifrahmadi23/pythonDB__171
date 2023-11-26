def jumlahBilAsli():
    sum1 = 0
    count = 1
    while (count < 10):
        sum1 = sum1 + count
        count = count + 1
    print (count)
    print (sum1)
jumlahBilAsli()

#1
def check_zero_non_zero():
    n = int(input("Masukan angka = "))
    if n == 0:
        print ("Ini nol")
    else :
        print ("bukan nol")
check_zero_non_zero()

#2
def nomor_1():
    num1 = int(input("Masukkan angka 1 : "))
    num2 = int(input("Masukkan angka 2 : "))
    if num1 > num2:
        print ("Yang paling besar adalah",num1)
    else :
        print ("Yang paling besar adalah", num2)
nomor_1()

#3
def nomor3():
    n = int(input("masukan angka : "))
    if n < 0:
        print ("Bilangan negatif")
    else :
        print ("Bialngan Positif")
nomor3()

#4
def nomor4():
    vokal = ["a","i","u","e","o"]
    n = str(input("masukan huruf : "))
    if n in vokal:
        print ("vokal")
    else :
        print ("konsonan")
nomor4()

#5
def evanilaimhs(float):

  if float >= 90:
    return "Kinerja Luar Biasa"
  elif float >= 80:
    return "Kinerja Sangat Baik"
  elif float >= 70:
    return "Kinerja Bagus"
  elif float >= 60:
    return "Kinerja Rata-rata"
  else:
    return "Kinerja Kurang"
print("soal 1")
float = int(input("Masukkan nilai siswa dalam persentase: "))
nilaimhs = evanilaimhs(float)
print("Kinerja siswa adalah:", nilaimhs)







   