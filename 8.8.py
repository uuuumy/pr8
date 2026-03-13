txt = input()

txt_new = txt.split()
txt_new.sort(key=len)
print(' '.join(txt_new))
