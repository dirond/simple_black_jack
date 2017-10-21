#-*-coding:utf8;-*-
#qpy:3
#qpy:console
from game import Game
print("\n\n\t\t<-----Let's play Blackjack!----->")
new_game=Game()
while True:
    if new_game.low_cards():
        print('Cards over. Dispenser will be reload.')
        new_game.reload_dispenser()
    ans=input('\nPress "q" for exit\n')
    if ans!="q":
        if (new_game.first_move()):
            new_game.play()
        new_game.drop_players_hands()
    else:
        break