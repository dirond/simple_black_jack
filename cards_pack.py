from card import Card
from random import randint, seed

class CardsPack(Card):
    _suits=('♥','♦','♣','♠')
    _names=('2','3','4','5','6','7','8','9','10','J','Q','K','A')
    def __init__(self, pack_count):
        CardsPack._names*=pack_count
        self._unshf_cards=[]
        self.shf_cards=[]
        for suit in CardsPack._suits:
            for name in CardsPack._names:
                card=Card(suit,name)
                self._unshf_cards.append(card)
        self._shuffle()
        
   
    def _shuffle(self):
        pack=self._unshf_cards[:]
        while pack:
            i=randint(0,len(pack)-1)
            self.shf_cards.append(pack.pop(i))
        return self.shf_cards
    
    def take_card(self):
        return self.shf_cards.pop()
    
    def remaining_cards(self):
        return len(self.shf_cards)
if __name__=='__main__':
    my_pack=CardsPack(5)
    for card in my_pack.shf_cards:
        print(card)
    print('your card is \n{}'.format(my_pack.take_card()))
    print(len(my_pack.shf_cards))