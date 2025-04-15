def count_chars(text):
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result

def unique_chars(text):
    return list(set(text))

def analyze_text(text, ignore_spaces=False, ignore_digits=False, ignore_punct=False):
    result = {}
    for char in text:
        if ignore_spaces and char.isspace():
            continue
        if ignore_digits and char.isdigit():
            continue
        if ignore_punct and not char.isalnum() and not char.isspace():
            continue
        result[char] = result.get(char, 0) + 1
    return result

if __name__ == "__main__":
    test_text = "Привіт, світе 2023!"
    
    print("\n1. Підрахунок усіх символів:")
    print(count_chars(test_text))
    
    print("\n2. Унікальні символи:")
    print(unique_chars(test_text))
    
    print("\n3. Аналіз з фільтрацією (без пробілів і цифр):")
    print(analyze_text(test_text, ignore_spaces=True, ignore_digits=True))