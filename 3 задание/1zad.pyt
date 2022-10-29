n = 0
o = 0
z = 0
a = [0,0,0,0,0,-1,-2,-3,-4,-5,-6,-7,8,9,10,11,12,13,14,15]
for i in  range(len(a)):
     if a[i]>0:
          print(a[i],end=" ")
          n=n+1
print('положительные:',n)
for i in range(len(a)):
     if a[i]<0:
          print(a[i],end=" ")
          o=o+1
print('отрицательные:',o)
for i in range(len(a)):
     if a[i]==0:
          print(a[i],end=" ")        
          z=z+1
print('количество нулей:',z)
