a= "I hate learning code!"
with open("New.txt", 'a') as out:
    out.write(a + '\n')
    
Result: create a new file named New.txt includes:
I hate learning code!
