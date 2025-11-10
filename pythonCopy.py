'''
You cannot copy a list simply by typing list2 = list1, Because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also be made in list2
'''

# use copy method 

# fruits = ["orange","apple","banana","cherry","kiwi","mango"]
# mylist = fruits.copy()
# fruits[1] = 'rangane'
# print(fruits)
# print(mylist)

########################################## List Method #################################

# fruits = ["orange","apple","banana","cherry","kiwi","mango"]
# myList = list(fruits)
# fruits[1] = "ranange"
# print(fruits)
# print(myList)

########################################## Slice Method #################################

# fruits = ["orange","apple","banana","cherry","kiwi","mango"]
# myList = fruits[:]
# fruits[1] = "ranange"
# print(fruits)
# print(myList)
