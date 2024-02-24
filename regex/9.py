import re
txt=" Av vvA ADFVb bsdd  a_c"
x=re.sub(r'([a-z])([A-Z])',r'\1\2',txt)
print(x)