
def has_digit(password):
    return any(character.isdigit() for character in password)


def has_symbols(password):
    return any(not character.isalnum() for character in password)


def has_upper_letters(password):
    return any(character.isupper() for character in password)


def has_lower_letters(password):
    return any(character.islower() for character in password)


def is_very_long(password):
    return len(password) >= 12


def main():
    password = input("Введите пароль: ")
    score = 0

    check_points= [
        (has_digit, 2),
        (has_symbols, 2),
        (has_upper_letters, 2),
        (has_lower_letters, 2),
        (is_very_long, 2)
    ]

    for check, points in check_points:
        if check(password):
            score += points 

    print('Рейтинг пароля : ', score)
    return score


if __name__ == "__main__":
    main()


