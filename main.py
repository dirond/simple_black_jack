#-*-coding:utf8;-*-
#qpy:3
#qpy:console
from game import Game
print("\n\n\t\t<-----Let's play Blackjack!----->")
while True:
        ans=input('\nPress "q" for exit\n')
        if ans!="q":
            new_game=Game()
            if (new_game.first_move()):
                new_game.play()
        else:
            break