l=list(map(int,(input().split())))
l1=[]

for k in l:
    if(k%2==0):
        l1.append(k)

print(l1)