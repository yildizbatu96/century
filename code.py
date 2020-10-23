def yillar():
    a=input("What is the year?: ")
    stra=str(a)

    if (len(stra)<3):
        print(stra+ " is 1. century")
    elif(len(stra) == 3):
        if(int(stra[1:3]) == "00"):
            print(int((stra[0])+". century"))
        elif(int(stra[1:3]) != "00"):
            print((int(stra[0])+1), ". century")
    else:
        if(int(stra[2:4]) == "00"):
            print(int((stra[:2]), ". century"))
        else:
            print(int((stra[:2]))+1, ". century")
            
            
print(yillar())
