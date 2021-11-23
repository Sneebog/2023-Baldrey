def getPword(passcheck):
    if len(passcheck) >= 6 and len(passcheck) <= 8:
        Plonted = 2
    else:
        Plonted = 1
    return Plonted
#main program
Password = input("What is your password?")
check = getPword(Password)
while check == 1:
    Password = input("ERROR, What is your password?")
    check = getPword(Password)
print("password accepted")