txt=input()
for word in txt.split():
    if txt.count(word) == 2:
        print(word)
        break