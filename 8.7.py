txt = input()

minlen = 10000000000000000
txt_new = txt.split()

for word in txt_new:
    if len(word) < minlen:
        minlen = len(word)
print(minlen)
