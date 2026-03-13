txt = input()
txt_new = txt.split()
list = []
for word in txt_new:
    if word != txt_new[0] and len(set(word)) == len(word):
        list.append(word)
print(' '.join(list))
