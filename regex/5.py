import re
txt=" Av vvA aDFVb avjn=b a_c acb"
x=re.search(r'a.*b$',txt)
print(x)