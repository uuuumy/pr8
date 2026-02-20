def cities():
    text = input().lower().split()

    if not text:
        return

    def player_name(index):
        return "Петя" if index % 2 == 0 else "Вася"

    for i in range(1, len(text)):
        prev_city = text[i - 1]
        current_city = text[i]

        last_letter = prev_city[-1]
        if last_letter in "ьыъ":
            last_letter = prev_city[-2]

        if current_city[0] != last_letter:
            print(player_name(i - 1))
            return

    print(player_name(len(text) - 1))
cities()