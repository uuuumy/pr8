txt = input()

balance = 0
correct = True

for ch in txt:
    if ch == '(':
        balance += 1
    elif ch == ')':
        if balance == 0:
            correct = False
            break
        balance -= 1

if balance != 0:
    correct = False

print("да" if correct else "нет")
