# # Python Code Challenge #9: Simulate Dice

# Your goal is to implement a function, `roll_dice()`, that takes a variable number of input arguments representing the number of sides on an arbitrary number of dice, its and its output should print a table of the probability for each possible outcome.

# ## Example Test Output
# Rolling one four-sided die and two six-sided dices:
# ```console
# >>> roll_dice(4,6,6)

# OUTCOME PROBABILITY
# 3       0.69%
# 4       2.06%
# 5       4.14%
# 6       6.95%
# 7       9.70%
# 8       12.55%
# 9       13.93%
# 10      13.85%
# 11      12.52%
# 12      9.70%
# 13      6.95%
# 14      4.17%
# 15      2.09%
# 16      0.70%
# ```

import random
from collections import Counter

counter = 1000000

def roll_dice(*args):
  dices = [] #Kocka oldalszámok
  #Ha szám jön, akkor az kockaoldalszám
  for arg in args:
    if isinstance (arg, int): 
      dices.append(arg)
    rolls =[]
    for i in range(counter):
      rolls.append(sum((random.randint(1,x) for x in dices)))
  cnt = Counter(rolls)
  
  # A trükk a ciklus, ahol minden lehetséges összegen végigmegy len(dices) Ahány kocka van anniszor 1 az alap, sum(dices) a max ami kijöhet
  for oroll in range(len(dices), sum(dices)+1):  
    print(f"{oroll}\t{cnt[oroll]*100/counter :0.2f}%")

 

 
roll_dice(4,6,6)
print("\n")
roll_dice(4,6,6, 20)