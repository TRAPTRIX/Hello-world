while True:
    n= input("Enter your family name:")
    if n.isalpha():
        break
    else:
        print("Error")
     
while True:
    sn= input("Enter your surname:")
    if sn.isalpha():
       break
    else:
        print("Error")
print(sn , n)
