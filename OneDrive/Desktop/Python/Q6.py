z=True
while(z):
    a=input().lower()
    b=input().lower()

    if(a=='rock'):
        if(b=='scissors'):
            print('Player one wins')
        elif(b=='paper'):
            print('Player two wins')
        elif(b=='rock'):
            print('It is a Tie')
        else:
            print('Wrong Input from Player Two')
    elif(a=='scissors'):
        if(b=='scissors'):
            print('It is a Tie')
        elif(b=='paper'):
            print('Player one wins')
        elif(b=='rock'):
            print('Player two wins')
        else:
            print('Wrong Input from Player Two')
    elif (a == 'paper'):
        if (b == 'paper'):
            print('It is a Tie')
        elif (b == 'rock'):
            print('Player one wins')
        elif (b == 'scissors'):
            print('Player two wins')
        else:
            print('Wrong Input from Player Two')
    else:
        print('Wrong Input ')
    print("If you wanna play again type 'Yes'")
    q=input()
    if(q=='Yes'):
        z=True
    else:
        z=False
