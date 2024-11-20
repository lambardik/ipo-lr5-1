string = str(input("Введите строку: ")) 
print("Длина строки:",len(string)) 

glasnye = 0 
soglasnye = 0

string = string.lower() 

glasnye = ["Аа","Уу","Оо","Ии","Ээ","Ее","Ёё","Яя","Юю"] 

for i in string: 
    if i in glasnye:
        glasnye+=1
    else:
        soglasnye+=1
        
print("Кол-во гласных: ",glasnye)
print("Кол-во согласных: ",soglasnye)
