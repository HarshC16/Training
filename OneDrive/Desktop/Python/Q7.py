a=int(input())

d=dict(input().split() for _ in range(a))

print('Welcome to the birthday dictionary. We know the birthdays of:')
print(d.keys())
print("Who's birthday do you want to look up?")
bday=input()
k=0
for u in (d.keys()):
    if(bday==u):
        print(bday+" birthday is on "+ d[bday])
        k=1
if(k!=1):
    print('Person not found')