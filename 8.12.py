import keyword

name = input().strip()
if name.isidentifier() and not keyword.iskeyword(name):
    print("может быть именем в Python")
else:
    print("не может быть именем в Python")
