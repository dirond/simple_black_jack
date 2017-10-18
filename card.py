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
   return '[{0} {1}]'.format(
   self.name.title(),self.suite)
if __name__=='__main__':
    test_card=Card('♥','jack',10)
    print(test_card)