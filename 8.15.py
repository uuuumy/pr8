secret = input().strip()

while not (secret.isdigit() and len(secret) == 4
           and len(set(secret)) == 4):
    secret = input("Нужно четырёхзначное число с "
                   "неповторяющимися цифрами: ").strip()

print("\n" * 25)

attempts = 10
win = False

for _ in range(attempts):
    guess = input().strip()

    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    common_digits = sum(1 for d in set(guess) if d in secret)
    cows = common_digits - bulls

    print(f"Быков: {bulls} Коров: {cows}")

    if bulls == 4:
        win = True
        break

print("Победа!" if win else "Проигрыш!")