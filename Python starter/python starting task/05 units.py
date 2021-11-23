print("Give an number between 100 and 999")
num = int(input())
hundreds = num // 100
tens = (num % 100) // 10
units = (num % 100) % 10
print(hundreds, "hundreds,", tens , "tens and", units, "units")