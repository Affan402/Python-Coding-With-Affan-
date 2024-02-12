#Declare mylist : ARRAY [0:9] OF INTEGER
myList = [15, 26, 34, 45, 54, 62, 69, 75, 86]

#Function of Linear Search
def LinearSearch(Num):
    
    global myList
    index = 0 
    #Flag
    found = False
    
    while found == False and index < 8:
        
        if Num == myList[index]:
            found = True
        else:
            index +=1 
    if found == True:
        return index
    else:
        return -1

#Calling function     
x= LinearSearch(34)

if x == -1 :
    #Display on terminal
    print("Number not found ")
else:
    #Display on terminal
    print("Number found at", x)
