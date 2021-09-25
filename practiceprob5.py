# guessing game
import  random

def guessGame(a,b,k):
    guess = int(input(f"guess a number between {a} and {b}\n"))
    nguess = 1
    while guess != k:
        if guess<k:
            guess = int(input("guess a bigger no\n"))
            nguess+=1
        else:
            guess = int(input("guess a smaller no\n"))
            nguess+=1
    print(f"you guess tho no in {nguess}")
    return nguess

if __name__ == '__main__':
    a =int(input("enter the valu of a\n"))
    b =int(input("enter  the valu of b\n"))
    k = random.randint(a,b)
    print("player1 turns")
    g1= guessGame(a,b,k)
    print("player2 turns")
    g2= guessGame(a,b,k)

    if g1<g2:
        print("player1 won the match!")

    elif g2<g1:
        print("player2 won the match!")

    else:
        print("its a tie!")


