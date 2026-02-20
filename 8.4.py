txt=input()
for _ in set(txt):
    if txt.count(_) == 3:
        print(_)
        break
