txt = input()

list = []
txt_new = txt.split()

for word in txt_new[::-1]:
    list.append(word)
print(' '.join(list))
