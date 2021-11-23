max = int(input())
num = int(input())
secmax = num
if max < num:
    max, secmax = num, max
num = int(input())
if max < num:
    max = num
elif secmax < num:
    num, secmax = secmax, num
print(max, secmax, num)
     
