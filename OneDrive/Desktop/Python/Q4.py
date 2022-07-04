a=int(input())
b=int(input())
l1=[]
l2=[]
l3=[]
l4=[]
for i in range (a):
    z=int(input())
    l1.append(z)

for j in range (b):
    x=int(input())
    l2.append(x)

for i in range (a):
    for j in range (b):
        if (l1[i]==l2[j]):
            l3.append(l1[i])
k=len(l3)
print(k)
for p in range (k-1):
    if(l3[p]==l3[p+1]):
        l4.append(p)

l4.reverse()
o=len(l4)
n=0
for e in range (o):
    del l3[l4[n]]
    n=n+1

print(l1)
print(l2)
print(l3)
