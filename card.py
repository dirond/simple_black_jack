class Card():
 def __init__(self,suite,name):
  self.suite=suite
  self.name=name
  if name=='A':
      self.score=11
  elif name.isdigit():
      self.score=name
  else:
      self.score=10
 def __str__(self):
   s=''
   if self.name!='10':
       s=' '
   return '+----+\n|{0}{2}  |\n|\
    |\n|  {1}|\n+----+'.format(
   self.name.title(),self.suite,s)
if __name__=='__main__':
    test_card=Card('♥','7')
    print(test_card)