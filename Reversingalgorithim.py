
n = ["a", "b", "c"]

def iterative(list): 
    i = len(list) - 1   
    while i > -1:
        print(list[i])
        i -= 1
def recursive(list):
    if len(list) == 0:
        return []
    else:
        return[list[-1] + recursive(list[:-1])]
print(recursive(n))