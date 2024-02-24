import re
txt="ab gabb  abbb"  
x=re.search(r'a[bb]{2,3}',txt)
print(x)
