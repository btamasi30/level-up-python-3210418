# Python Code Challenge #4: Find All List Items

# Your goal is to implement a function, `index_all()`, that takes a list of objects and the item to search for as input arguments and returns a list of indices for where that item exists within the list.

# NOTE: Since the input argument could be a list of lists, your function should be able to traverse multidimensional lists to find all instances of the item, and the elements of the returned list should also be lists to indicate multidimensional indices.

# ## Example Test Output
# ```console
# >>> example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
# >>> index_all(example, 2)
# [[0, 0, 1], [0, 1], [1, 1]]
# >>> print(index_all(example, [1, 2, 3]))
# [[0, 0], [1]]
# ```

def index_all(inlist, list_item):
  indexes = []
  for i, value in enumerate(inlist): # Az Enumerate segít abban, hogy egy indexet is kapjunk az elemek mellé
    if value == list_item:
        # Ha a keresett elem megegyezik az aktuális listaelemmel, akkor tegyük el az indexét "Listaként" ezért a []
        indexes.append([i])
    elif isinstance(inlist[i], list):
        # Ha a listában nested lista van, rekurzívan kérjük vissza az eredményt, majd a for segítségével lista elemenként adjuk hozzá az indexhez.
        for i2 in index_all(inlist[i], list_item):  
          indexes.append([i] + i2)
  return indexes

example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print ("Example: ", example)
searchstr = 2
print ("Keressük: ", searchstr)
print ("Eredmény: ",index_all(example, searchstr))
print("-----")
searchstr = [1, 2, 3]
print ("Keressük: ", searchstr)
print("Eredmény: ",index_all(example,searchstr))
