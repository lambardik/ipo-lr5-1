string = str(input("Введите строку: ")) 
print("Длина строки:",len(string)) 
glasnye = 0
soglasnye = 0

string = string.lower() 

glas = ["а","у","о","и","э","е","ё","я","ю"] 

for i in stroka: 
    if i in glas:
        glasnye+=1
    elif i ==" ":
        continue
    else:
        soglasnye+=1
        
print("Количество гласных: ",glasnye)
print("Количество согласных: ",soglasnye)
