str1 = input()
str2 = input()
str3 = input()

allstr = list(set(str1)) + list(set(str2)) + list(set(str3))
result = [i for i in allstr if allstr.count(i) == 1]

print(''.join(result))

