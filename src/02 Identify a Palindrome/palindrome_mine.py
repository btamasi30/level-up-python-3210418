# Megoldás 2, ha a regexpet használjuk
# import re  

def is_palindrome(text):
  print(text)
  cleartext = ''.join(c.lower() for c in text if c.isalnum() and c != ' ')
  #Megoldás 2: A lower miatt elég csak a kisbetűt összeszedni
  # cleartext = ''.join(re.findall("[a-z]", txt.lower()))
  revtext = cleartext[::-1]
  return cleartext == revtext

  
print(is_palindrome("Géza kék az ég"))

print(is_palindrome('hello world'))

print(is_palindrome('Go hang a salami, I’m a lasagna hog.'))