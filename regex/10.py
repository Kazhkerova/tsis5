str =" firstName veRSE deF "
s=''.join(['_'+ i.lower() if i.isupper() else i for i in str] )
print(s.lstrip('_'))