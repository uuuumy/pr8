txt=input()
max_count=1
curr_count=1
for i in range(1,len(txt)):
    if txt[i] == txt[i  - 1]:
        curr_count += 1
    else:
        if curr_count > max_count:
            max_count=curr_count
        curr_count=1
print(max_count)