txt=input()
list=[]
for i in txt.lower():
    if i.isalpha() and i not in list:
        list.append(i)
print(len(list))