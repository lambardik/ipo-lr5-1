stroka = str(input("Введите строку: ")) 
print("Длина строки:",len(stroka)) 
glasnye = 0
soglasnye = 0

stroka = stroka.lower() 

glas = ["а","у","о","и","э","е","ё","я","ю"] 

for i in stroka: 
    if i in glas:
        glasnye+=1
    else:
        soglasnye+=1
        
print("Количество гласных: ",glasnye)
print("Количество согласных: ",soglasnye)
