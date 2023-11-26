from persegiPanjang import persegiPanjang
v = "y"

while v == "y":
    panjang = float(input("Masukkan Panjang : "))
    lebar = float(input("Masukkan Lebar   : "))
    pp = persegiPanjang(panjang,lebar)

    print("Keliling : ",pp.keliling())
    print("Luas : ",pp.luas())

    print(pp.__str__())

    v = str(input("Ulangi Program?(y/n) : "))

 