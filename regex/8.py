import re
txt=" Av vvA ADFVb bsdd  a_c"
x=re.findall(r'[A-Z][^A-Z]*',txt)
print(x)