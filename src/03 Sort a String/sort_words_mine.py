def sort_words(text):
  wordlist = text.split()
  return ' '.join(sorted(wordlist,key=str.casefold))

mytext = "Laci liba benő Béla Kati Sára"
print(mytext)
print(sort_words(mytext))