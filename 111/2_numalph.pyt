a=[1,2,3]
b=['a','b','c','d','f']
def qwe (a,b):
    c=[]
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
    for i in range(len(a), len(b)):
        c.append(b[i])
    return c
print(qwe(a,b))