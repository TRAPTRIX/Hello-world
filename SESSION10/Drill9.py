Conan={
    "Author": "Aoyama GOSHO",
    "Main character" : ["Kudo Shinichi","Ai"],
    "Content": "Detective"
}

print("About CONAN")
a=0

Question_1={
    "Question":"Ten tac gia? ",
    "Answer":["Gosho","Hayate","Kagari"]
}
print(Question_1["Question"])
print(Question_1["Answer"])

# for v in Conan.values():
#     print(v)

while True:
    i= input("Choose one name above? ")
    if i == "Gosho":
        print("Hura!")
        a=a+1
        break

    elif i == "Hayate" or "Kagari":
        print('Wrong answer! Again!')
    

    
Question_2={
    "Question":"Nhan vat chinh? ",
    "Answer":["Kudo","Ayumi","Mitsuki"]
}
print(Question_2["Question"]) 
print(Question_2["Answer"]) 


while True:
    h= input("Choose one answer above? ")
    if h == "Kudo":
        print("Hura!")
        a=a+1
        break
    elif h == "Ayumi" or "Mitsuki":
        print('Wrong answer! Again!')
   

print("Correct answer:",a)

    

