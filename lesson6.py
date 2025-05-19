
def has_digit(password):
    return any(character.isdigit() for character in password)


def has_letters(password):
    return any(character.isalpha() for character in password)


def has_upper_letters(password):
    return any(character.isupper() for character in password)


def has_lower_letters(password):
    return any(character.islower() for character in password)


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


