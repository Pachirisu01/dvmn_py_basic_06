
def has_digit(password):
    for letter in password:
        if letter.isdigit():
            return True
    return False

def has_letters(password):
    for letter in password:
        if letter.isalpha():
            return True
    return False

def has_upper_letters(password):
    for letter in password:
        if letter.isupper():
            return True
    return False

def has_lower_letters(password):
    for letter in password:
        if letter.islower():
            return True
    return False

def is_very_long(password):
    return len(password) >= 12

def main():
    password = input("Введите пароль: ")
    score = 0
    if has_digit(password):
        score += 2
    if has_letters(password):
        score += 2
    if has_upper_letters(password):
        score += 2
    if has_lower_letters(password):
        score += 2
    if is_very_long(password):
        score += 2
    print('Рейтинг пароля : ', score)
    return score



if __name__ == "__main__":
    main()


