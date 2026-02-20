hint = input().strip()
secret = input().strip().lower()

print("\n" * 25)

state = ["*"] * len(secret)

attempts = 10
win = False

while attempts > 0:
    print(hint)
    print("".join(state))
    choice = input("Буква или слово (0 - буква, 1 - слово)?").strip()

    if choice == "0":
        letter = input().strip().lower()
        if len(letter) != 1:
            attempts -= 1
            continue

        found = False
        for i, ch in enumerate(secret):
            if ch == letter and state[i] == "*":
                state[i] = letter
                found = True

        attempts -= 1

        if "*" not in state:
            win = True
            break

    elif choice == "1":
        word = input().strip().lower()
        attempts -= 1
        if word == secret:
            win = True
            break
        else:
            continue
    else:
        attempts -= 1

if win:
    print("Победа!")
else:
    print("Проигрыш!")