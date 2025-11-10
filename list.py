#Lists

'''
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, 
all with different qualities and usage.
'''

# List: List items are ordered, changeable, and allow duplicate values.

'''
Ordered: When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
note: There are some list methods that will change the order, but in general: the order of the items will not change.
Changeable: The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
Allow Duplicate: Since lists are indexed, lists can have items with the same value
'''

#list length:
'''
length_list = ['hello', 'this', 'is', 'the', 'list']
print(len(length_list)) #output: 5
print(type(length_list)) #output: <class 'list'>
'''

#list Constructor
'''
cons_list = list(('hello', 'this', 'is', 'the', 'list'))
print(cons_list)
'''

########################################## Python Collection #################################

'''
list: List is a collection which is ordered and changeable. Allows duplicate members.
Tuple: Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set: Set is the collection which is unordered and unchangeable and unidexed. Allows duplicate members.
Dictionary: Dictionary is collection of odered and changable. No duplicate members.

'''

# s = {10, 2, 5, 8}
# print(s)   # Output might be {8, 2, 10, 5} (order not guaranteed)

########################################## Access List Items #################################

#my_name = ["my","name","is","rupesh"]
# print(my_name[3]) // rupesh
#print(my_name[-1]) // rupesh
#print(my_name[2:]) // ['is','rupesh']

#check if element exist.
'''
basket = ["pen","pencil","erraser","sharpner"]
if "pencil" in basket:
   print("yes the pencil is in basket")
'''   

########################################## Add List Items #################################

# To add the item to the end of the list use the append

# first_item = ["apple", "bada apple", "chota apple", "apple"]
# second_item = ("ball","bada ball", "chota ball")
# first_item.append(second_item);
# print(first_item)

# Insert in a list insert() the item in particular location

# first_item.insert(1,second_item)
# print(first_item) // ['apple', 'bada apple', 'chota apple', ('ball', 'bada ball', 'chota ball')]

'''
Think of your list as a train 🚆
append() → attaches one new coach (even if that coach has multiple seats inside)
extend() → attaches each seat from another coach one by one.
'''

# first_item.extend(second_item)
# print(first_item); // ['apple', 'bada apple', 'chota apple', 'ball', 'bada ball', 'chota ball']

########################################## Remove List Items #################################

# Remove method removes specific item from the lists.
# first_item.remove("bada apple")
# print(first_item)

# if there are more the one item in the list. remove() method removes the first occurence.
# first_item.remove("apple")
# print(first_item)

# pop() method removes the specified index
# first_item.pop(-1)
# print(first_item);

# del keyword also remove the specified index
# del first_item[0]
# print(first_item)

#clear() clear entire list but list remain without content
# first_item.clear()
# print(first_item)
