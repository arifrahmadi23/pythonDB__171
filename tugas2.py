#1.
def nomor_1():
    num1 = int(input("Masukkan angka 1 : "))
    num2 = int(input("Masukkan angka 2 : "))
    if num1 > num2:
        print ("Yang paling besar adalah",num1)
    else :
        print ("Yang paling besar adalah", num2)
nomor_1()

#2.
def nomor_2():
    num1 = int(input("Masukkan angka 1 : "))
    num2 = int(input("Masukkan angka 2 : "))
    num3 = int(input("Masukkan angka 3 : "))
    if (num1 > num2) and (num1 > num3) :
        print ("Yang paling besar adalah", num1)
    elif (num2 > num1) and (num2 > num3):
        print ("Yang paling besar adalah",num2)
    else :
        print ("Yang paling besar adalah",num3)
nomor_2()

#3.
def nomor_3():
    length =int(input("Masukkan angka :"))
    x = 0
    y = 1
    iteration = 0
    if length <= 0:
        print("Masukkan angka > dari 0!")
    elif length == 1:
        print("Hasil element".format(length),":")
    else:
        print("Hasil element".format(length),":")
    while (iteration < length):
        print(x, end=',')
        z = x + y
        x = y
        y = z
        iteration += 1
nomor_3()

#4.
def nomor_4():
    n = int(input("Masukkan angka : "))
    for i in range (1,n+1,2):
        print (i)
nomor_4()

#5.
def nomor_5():
    for i in range (3):
        print ("A B C")
nomor_5()


    





        
