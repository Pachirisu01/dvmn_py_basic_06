PASSWORD = input("Введите пароль: ")


def password_score_all(PASSWORD):
    score = 0
    if any(letter.isdigit() for letter in PASSWORD):
        score += 2
    if any(letter.isupper() for letter in PASSWORD):
        score += 2
    if any(letter.islower() for letter in PASSWORD):
        score += 2
    if any(not letter.isalpha() and not letter.isdigit() for letter in PASSWORD):
       	score += 2
    if len(PASSWORD) >= 12:  
        score += 2
    return score


if __name__ == "__main__":
    print(f"Введённый пароль: {PASSWORD}")
    print(f"Рейтинг пароля: {password_score_all(PASSWORD)}")




