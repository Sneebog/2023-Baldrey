def multiples(f1,f2,f3,f4):
    print("Hi", f4, "here is yout times table")
    for i in range(f2,f3):
        print(f1, "x", i, "=", f1 * i)
    next
#main program
pupilname = input("What is your name?")
print("enter times table, start number and end number")
table = int(input())
startnum = int(input())
endnum = int(input())
multiples(table,startnum,endnum,pupilname)