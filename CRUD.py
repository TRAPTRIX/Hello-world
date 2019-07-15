i=["read","soccer","smile"]
print(i)
while True:
    # a="C"
    # b="R"
    # c="U"
    # d="D"
    #print(a, b, c, d)
    print("C , R, U, D")
    n=input("Your choice, one capital above? ")
    if n=="C":
        e=input("The thing that u like? ")
        i.append(e)
        print(i)
    elif n=="R":
        print(*i, sep="\n")
    elif n=="U":
        f=input("Any changes?")
        if f=="read" or "soccer" or "smile":
            g=input("Your change?")
            if f=="read":
                i[0]=g
                print(i)
            elif f=="soccer":
                i[1]=g
                print(i)
            elif f=="smile":
                i[0]=g
                print(i)
    elif n=="D":
        h=input("Do u want to delete anything above?")
        if h=="read":
            i.remove("read")
            print(i)
        elif h=="soccer":
            i.remove("soccer")
            print(i)
        elif h=="smile":
            i.pop(2)
            print(i)
        





    
