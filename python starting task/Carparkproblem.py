#Crazycode
row = 20
column = 20
park = [row],[column]
for row in range(0,9):
    for column in range(0,5):
        park[row][column] = "empty"
    next 
next 
Regis = input("what is your registration?")
flag = False
while flag != True:
    Gimble = int(input("What Row?"))
    Gomble = int(input("What Column?"))
    if (Gimble >= 1 and Gimble <= 10) and (Gomble >= 1 and Gomble <= 6):
        flag = True
parkrow = Gimble - 1
parkcolumn = Gomble - 1
if park[parkrow, parkcolumn] == "empty":
     park[parkrow, parkcolumn] = Regis
else:
    print("that Space is taken")
for row in range(0,9):
    for column in range(0,5):
        print(park[row,column])
    next 
next
#Crazycode end