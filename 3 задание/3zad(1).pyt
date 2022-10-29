a=input("Введите слово!")
b=[a]
c = len(a) #сколько букв в слове
d = list(a) 
print (d)
s=(c // 2)-1
ss=(c // 2)
if (c % 2) ==0:
    print (d[s],d[ss])
    print ('ЧЕТНОЕ СЛОВО')
else:
    print (d[ss])
    print ('НЕ ЧЕТНОЕ СЛОВО')
