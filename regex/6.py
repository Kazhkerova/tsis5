def d(s):
    rep=[' ',',','.']
    for c in rep:
        s=s.replace(c,':')
    return s
t="hello ,  world."
l=d(t)
print(l)