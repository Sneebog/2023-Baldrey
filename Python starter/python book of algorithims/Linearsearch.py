array = ["g","i","j","e","z","h","t","y","p","6","9",]
def linearsearch(namelist, namesearched):
    found = False   
    i = 0
    index = -1
    while i < (len(namelist)) and found == False:
        if namelist[i] == namesearched:
            index = i
            found = True
        i += 1
    return index
search = str(input("What are you searching for?"))
print(linearsearch(array, search))