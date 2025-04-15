text = "Приклад тексту з голосними і приголосними літерами"

vowels = "аеєиіїпвокківаоуюяAEЄИБЇОУЮЯ"

count = 0
for letter in text:
    if letter in vowels:
        count += 1

print("Кількість голосних літер у рядку:", count)
