def break_example():
    y=int(input("Massukan angka : "))
    for i in range (0,y+1):
        if i == y:
            print ("Thank you!")
            break
        else:
            print(i)
    print("End of Prg")
break_example()
