import random

def choose():
    words=["Basket","Billion","Analyse","Associate","hello","Balance","thanku","this","Hurrah"]
    pick=random.choice(words).lower()
    return pick

def jumbled(picked_word):
    jumbled_word="".join(random.sample(picked_word,len(picked_word)))
    return jumbled_word

def thank(p1_name,p1_point,p2_name,p2_point):
    print('Player 1,your points are : ',p1_point)
    print('Player 2,your points are : ',p2_point)
    print('Thanks for playing the game.')
    print('Have a good day.')

def play():
    p1_name=input('Player 1,Enter your name :- ')
    p2_name=input('Player 2,Enter your name :- ')
    p1_point=0
    p2_point=0
    turn =0

    while(True):
        picked_word=choose()
        word=jumbled(picked_word)
        print('Here is your jumbled word : ',word)
        
        if(turn % 2 == 0):
            ans=input("Player 1, It's your turn.Give your answere :- ").lower()
            if(ans == picked_word):
                print('Hurray! you got it.')
                p1_point=p1_point+1
                print('Player 1, your points are : ',p1_point)
            else:
                print('Oh! you do not get it.That is ',picked_word)
                print('Better luck next time.')
        
            c=int(input('Press 1 for continue and 0 for exit.'))
            if c==0:
                thank(p1_name,p1_point,p2_name,p2_point)
                break
                   
        else:
            ans=input('Player 2,Its your turn.Give your answere :- ').lower()
            if(ans==picked_word):
                print('Hurray! you got it.')
                p2_point=p2_point+1
                print('Player 2, your points are : ',p2_point)
            else :
                print('Oh! you do not get it.That is ',picked_word)
                print('Better luck next time.')
        
            c=int(input('Press 1 for continue and 0 for exit.'))
            if c==0:
                thank(p1_name,p1_point,p2_name,p2_point)
                break
            
        turn =turn +1
            
play()  