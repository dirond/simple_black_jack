from player import Player
from cards_pack import CardsPack
class Game():
    def __init__(self):
        self.man=Player('You')
        self.cpu=Player('Casino')            
        self.pack=CardsPack() 
        
    def show_cards(self):
        for player in (self.cpu,self.man):
            print('_'*30)
            print(player.name.title()+' cards:')
            print('  ',end='')
            for card in player.cards:
                print(card, end=' ')
            print('\nTotal score: {}'.format(player.get_score()))
            print('_'*30)
    
    def move(self,player,taked_card):
        player.cards.append(taked_card)
        if taked_card.name=='A' and player.score+int(taked_card.score)>21:
            player.score+=1
        else:   
            player.score+=int(taked_card.score)

    def show_result(self,player):
        if player==self.man:
            if player.get_score()==21:
                message='Congratulations! You have blackjack!'
            elif player.get_score()>21:
                message='Sorry you lose. Game over.'
        else:
            if player.get_score()==21:
                message='Sorry you lose. Casino has blackjack!'
            elif player.get_score()>21:
                message='Congratulations! You win! Casino has {} points'.format(player.get_score())
            else:
                message='Sorry, You lose. Casino has {} points'.format(player.get_score())
        return message
        
    def first_move(self):
        for player in (self.cpu,self.cpu,self.man,self.man):
            self.move(player,self.pack.take_card())
        self.show_cards()
        if self.cpu.get_score()==21:
            print('Sorry you lose. Casino has blackjack!')
            return False
        elif self.man.get_score()==21:
            print('Congratulations! You have blackjack!')
            return False
        return True
        
    def play(self):
        while True:
            ans=input('\nTake another? y/n ')
            if ans=='y':
                player=self.man
                self.move(player,self.pack.take_card())
                self.show_cards()
                if player.get_score()==21:
                    print('Congratulations! You have blackjack!')
                    break
                elif player.get_score()>21:
                    print('Sorry, You lose. Game over.')
                    break
            elif ans=='n':
                min_score=self.man.get_score()
                player=self.cpu
                while player.get_score()<min_score:
                    self.move(player,self.pack.take_card())
                    self.show_cards()
                else:
                    if player.get_score()==21:
                        print('Sorry you lose. Casino has blackjack!')
                        break
                    elif player.get_score()>21:
                        print('Congratulations! You win! Casino has {} points'.format(player.get_score()))
                        break
                    else:
                        print('Sorry, You lose. Casino has {} points'.format(player.get_score()))
                        break
            else:
                print('input y or n')
                continue
        
            
if __name__=='__main__':
    while True:
        ans=input('\nPress "s" for start playing, or another button for exit\n')
        if ans=="s":
            test2_game=Game()
            if (test2_game.first_move()):
                test2_game.play()
        else:
            break