class Player():
    
    def __init__(self,name):
        self.cards=[]
        self.score=0
        self.money=100
        self.name=name
    
    def get_score(self):
        return self.score
    def drop_cards(self):
        self.cards=[]
        self.score=0