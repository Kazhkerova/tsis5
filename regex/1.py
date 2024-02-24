import re
txt="abbb as a ab dab gabb"
x=re.findall(r'a[b]*',txt)
print(x)

