from player import Player
from cards_pack import CardsPack
import os
class Game():
    
    def __init__(self):
        self.man=Player('You')
        self.cpu=Player('Casino')            
        self.reload_dispenser() 
        
    def reload_dispenser(self):
        self.pack=CardsPack(5)
    
    def show_cards(self):
        r=os.system('clear')
        '''Build row of cards'''
        for player in (self.cpu,self.man):
            BORDERS=[]
            NAME=[]
            BODY=[]
            SUIT=[]
            
            cards_count=len(player.cards)
            result=[]
            print('_' * 7 * cards_count)
            print(player.name.title()+' cards:')
            for card in player.cards:
                card=card.__str__().split('\n')              
                BORDERS.append(card[0])
                NAME.append(card[1])
                BODY.append(card[2])
                SUIT.append(card[3])
            for part in(BORDERS,NAME,BODY,SUIT,BORDERS):
                result.append(part)          
            for res in result:
                for symb in res:
                    print(symb,end=' ')
                print()
            print('\nTotal score: {}'.format(player.get_score()))
            print('_' * 7 * cards_count)
            
   
    def low_cards(self):
        if self.pack.remaining_cards()<10:
            return True
        else:
            return False
            
    def move(self,player,taked_card):
        player.cards.append(taked_card)
        if taked_card.name=='A' and player.score+int(taked_card.score)>21:
            player.score+=1
        else:   
            player.score+=int(taked_card.score)

    def show_result(self,player):
        message=''
        if player==self.man:
            if player.get_score()==21:
                message='Congratulations! You win!'
            elif player.get_score()>21:
                message='Sorry, you lose with {} points.'.format(player.get_score())
        else:
            if player.get_score()==21 and len(player.cards)==2:
                message='Sorry, you lose. Casino has blackjack!'
            elif player.get_score()>21:
                message='Congratulations! You win! Casino has {} points'.format(player.get_score())
            elif player.get_score()>self.man.get_score():
                message='Sorry, you lose. Casino has {} points'.format(player.get_score())
            elif player.get_score()<self.man.get_score():
                message='Congratulations! You win with {} points!'.format(self.man.get_score())
            elif player.get_score()>=17 \
            and player.get_score()==self.man.get_score():
                message='Draw.'
        return message
        
    def drop_players_hands(self):
        self.man.drop_cards()
        self.cpu.drop_cards()
   
    def first_move(self):
        r=os.system('clear')
        for player in (self.cpu,self.man,self.man):
            self.move(player,self.pack.take_card())
        self.show_cards()
        if self.man.get_score()==21:
            print('Congratulations! You have blackjack!')
            return False
        return True
        
    def play(self):
        while True:
            ans=input('\nTake another? y/n ')
            if ans=='y':
                #r=os.system('clear')
                player=self.man
                self.move(player,self.pack.take_card())
                self.show_cards()
                result=self.show_result(player)
                if result:
                    print(result)
                    break
            elif ans=='n':
                #r=os.system('clear')
                player=self.cpu
                while player.get_score()<17:
                    self.move(player,self.pack.take_card())
                    self.show_cards()
                result=self.show_result(player)
                if result!='':
                    print(result)
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