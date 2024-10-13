text = input("Введите строку: ")
vowels = "аеёиоуыэюя"
consonants = "бвгджзйклмнпрстфхцчшщ"
vowel_count = sum(1 for char in text.lower() if char in vowels)
consonant_count = sum(1 for char in text.lower() if char in consonants)

print(f"Длина строки: {len(text)}")
print(f"Количество гласных: {vowel_count}")
print(f"Количество согласных: {consonant_count}")
