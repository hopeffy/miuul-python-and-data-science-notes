# type da true donmesi aslinda ayni tipte oldugunu da anlariz

# list, tuple, dictionary, set are the python collections, arrays.

# list
list1 = ["a", "b", "c"]
type(list1)

# dictionary  (hashmap)
dictionary = {"ali": 1, "berna": 2, "cemile": 3}
type(dictionary)

# tuple
tuple1 = ("python", "ml", "ds")
type(tuple1)

# set
set1 = {"python", "ml", "ds"}
type(set1)

# changing data type
a = 45
type(a)
float(a)

# looong strings
longstring = """" loooooooooooooooooooong
ooooooooooooooooooong string"""
print(longstring)

# string index
name = "john"
name[0]

# string slice islemi. Include 0 and exclude 2
name[0:2]

# string contains characters
# python has case sensitivity

"h" in name
"g" in name

# list ile tuple arasindaki fark, tuple degistirilemezler listesi.

##########################
# String Methods
##########################

# dir function ile method list
dir(int)

# len = reach the dimension and this is function
name = "John,John"
len(name)

# if this things has a class -> method
# if this things has not a class -> function

name.upper()
name.lower()

name.replace("o" , "e")
name.replace('o', 'e', 2)
name.split(',')

##########################
# List Methods
# - mutable
# - has index
# - contain different types of data types
##########################

notes = ['30', '40', '50', '60', '70', '80']
type(notes)
notes[4] = 60
notes[0:4]

len(notes)
notes.append(100)
notes.insert(1,101)
# pop method : delete value and return it
notes.pop()

##########################
# Dictionary
# - mutable
# - has index after 3.7
# - contain different types of data types
##########################

dictionary = {"name": ['john', 'jane', 'ali'],
              "age": 34}
dictionary['name'][2]

# dictionary[0][2] does not working. use the dict keys name not a index value.

'alí' in dictionary # return false
'ali' in dictionary['name'] # return true

dictionary.get('age')
dictionary.get("name")

dictionary['name'][1] = 'july'

# key- value
dictionary.keys()
dictionary.values()
dictionary.items()

# if it contains change it, if not just add new one
dictionary.update({'johan': 'johan2'})

dictionary.values()

# if it contains same attributes, this code change all of them and return just new ones. Delete old ones.
dictionary.update({'name': 'newjohn'})

print(dictionary)

# update ile degil de direkt mutable zaten esittir kullan
dictionary['name'][0] = 'johan'

##########################
# Tuples
# - immutable - unchangeable
# - ordered
# - contain different types of data types - heterogeneous
# - least usage
##########################

t = ('k1', 'k2', 'k3')

##########################
# SET
# - changeable
# - unordered + unique
# - contain different types of data types - heterogeneous
##########################

# difference() = difference of two sets (set  = kume)

numberList = [1, 2, 3]
numberList2 = [1, 2, 3, 5]
set1 = set(numberList)
set2 = set(numberList2)

set1.difference(set2)
set2.difference(set1)
set1 - set2

# symmetric_difference() : returns a set contains a mix of items that are not present in both sets.
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)
set1 ^ set2

# intersection() : returns a set contains only items that exist in both sets.(kesisim)
set1.intersection(set2)
set1 & set2

# union() : returns a set containing the union of sets (birlesim)
set1.union(set2)
set2.union(set1)

# isdisjoint() : returns true if none of items are present in both sets
set1.isdisjoint(set2)

# issubset() : returns true if all items in the set exists in the specified set (alt kume)
set1.issubset(set2)

# issuperset() : returns true if all items in the set exists in the original set, otherwise returns
# false. (all set
# items are include the another set )

