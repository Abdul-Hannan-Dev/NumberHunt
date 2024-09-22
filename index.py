import random
a=1 
b=10
num=random.randint(a,b)
print(f'In this game, you have to guess the number from {a} to {b}. You will have maximum 5 turns')
attempts=0
while True:
        attempts+=1
        try:
            guessed_num=int(input("guess the number: "))
        except ValueError:
            print("Please enter a valid number")
            attempts-=1
            continue
        if guessed_num < a or guessed_num>b:
            print(f'Please enter a number from {a} and {b}')
            attempts-=1
            continue
        if guessed_num==num:
            print(f'Congrats! You guessed the right number at your attempt no. {attempts}"\n" Wanna Play again? Press 1 to play again')
            retry=int(input())
            if retry!=1:
                break
            else:
                attempts=0
                num=random.randint(a,b)
                print(f'In this game, you have to guess the number from {a} to {b}. You will have maximum 5 turns')
        else:
            print( f'Oops..! You guessed the wrong number.')
            if guessed_num>num and attempts!=5:
                print(f'Hint: Your number is bigger than the correct number')
            elif guessed_num<num and attempts!=5:
                 print(f'Hint: Your number is smaller than the correct number') 
        if attempts==5:
            print(f'You failed :(\n the right number was: {num}"\n" Wanna play again? Press 1')
            retry=int(input())
            if retry!=1:
                break
            else:
                attempts=0
                num=random.randint(a,b)
                print(f'In this game, you have to guess the number from {a} to {b}. You will have maximum 5 turns')
        else:
            continue
