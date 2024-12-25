import random
print('Hello! do you want to play the game"guess the number"?')
print('Sumbit your number beetwen 1 and 100', end=' ')
n = int(input())
x = random.randint(0,100)
count=0
while count!=1:
    if n == x:
        count+=1
        print('You won! you  guessed number!')
        break
    elif n < x:
        print('Oops!,too little.Try again')
        n = int(input())
    elif n > x:
        print('Oops!,too much.Try again')
        n = int(input())
