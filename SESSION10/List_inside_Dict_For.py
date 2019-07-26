Conan={
    "Author": "Aoyama GOSHO",
    "Main character" : ["Kudo Shinichi","Ai"],
    "Content": "Detective"
}
# print("\n")
# for v in Conan.values():
#     print(Conan)
#     print(Conan, v)
# print("\n")
# for k in Conan.keys():
#     print(Conan, k)

# Conan["Nation"] = "Japan"
# for i in Conan.values():
#     print("-",i)

# Conan["Main character"]="Conan Edogawa"

Conan["Main character"].append("Ran")
Conan["Main character"].pop(1)
print(Conan)
print(Conan["Main character"][1])

i = 1
for k, v in Conan.items():
 
    print(i,". ",k,v)
    i=i+1
    
