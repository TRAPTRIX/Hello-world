# list:["",""   ]
# dic:{
#     "" : "",
#     "" : "",
# }

# print(items, sep="\n"): xuong dong



restaurant_management=[
{
    "name":"Huy",
    "role":"waiter",
    "hours":12,
    "salary (Hour)":0.8,
},
{
    "name":"Tung",
    "role":"cook",
    "hours":24,
    "salary (Hour)":1.5,
},
{
    "name":"M.Duc",
    "role":"Manager",
    "hours":20,
    "salary (Hour)":2,
}
]

restaurant_management.append({
    "name":"Don",
    "role":"Waiter",
    "hours":12,
    "salary (Hour)":0.9,
})
print(*restaurant_management, sep="\n")

# print(restaurant_management[3])
print("UPDATE")

restaurant_management[0]={
    "name":"Huyen",
    "role":"Waitress",
    "hours":14,
    "salary (Hour)":1,
}
print(*restaurant_management, sep="\n")

# print("DELETE")
# restaurant_management.pop(3)
# print(*restaurant_management, sep="\n")

Huy_income = restaurant_management[1]['hours']*restaurant_management[1]['salary (Hour)']*20
print(Huy_income)


Tung_income = restaurant_management[2]['hours']*restaurant_management[2]['salary (Hour)']*20
print(Tung_income)

Money = Huy_income+Tung_income
print(Money)







