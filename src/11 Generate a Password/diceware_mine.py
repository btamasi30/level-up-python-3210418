# # Python Code Challenge #11: Generate a Password

# Your goal is to implement a function, `generate_passphrase()`, that takes the number of words to include in the password as the input argument and returns a string containing a sequence of randomly selected words from the [Diceware list](https://theworld.com/~reinhold/diceware.wordlist.asc) separated by spaces.

# ```console
# >>> generate_passphrase(4)
# 'correct horse battery staple'
# ```

from random import randint

def roll_dice5x6(): #roll 5 six-sided dice
  outp = ''
  for i in range(5):
    outp += str(randint(1,6))
  return outp

# Official Diceware algorithm
def generate_passphrase(num_words, wordlist_path='src/11 Generate a Password/diceware.wordlist.asc'):
  #Open only valuable rows
  with open(wordlist_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()[2:7778]

  word_dict = {}
  #Put Items to a Dictionary
  for line in lines:
    temp = line.split()
    word_dict[temp[0]] = temp[1]
    
  #Choose create a passwod from the list based on dices
  passelements = []
  for j in range (num_words):
      passelements.append(f"{word_dict[roll_dice5x6()]}")
  return ' '.join(passelements)

# Simplified algorithm
def generate_passphrase2(num_words, wordlist_path='src/11 Generate a Password/diceware.wordlist.asc'):
  #Open only valuable rows
  with open(wordlist_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()[2:7778]
    word_list = [line.split()[1] for line in lines]
   
    passelements = [word_list[randint(0,len(word_list))] for i in range(num_words)] 
    return ' '.join(passelements)


print(generate_passphrase(4))
print(generate_passphrase2(4))