password = input()
pass_lenght = len(password)


print('Введите пароль: ', password)


def password_score_all(password):
    score = 0
    if any(letter.isdigit() for letter in password):
        score += 2
    if any(letter.isupper() for letter in password):
        score += 2
    if any(letter.islower() for letter in password):
        score += 2
    if any(not letter.isalpha() and not letter.isdigit() for letter in password):
       	score += 2
    if len(password) >= 12:  
        score += 2
    return score


if __name__ == "__main__":
	print('Рейтинг пароля:', password_score_all(password))
	password_score_all(password)





