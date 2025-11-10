# list comprehension offers a shorter syntax when you want to create a new list based onthe values of an existing list.

# normal for loop to check value starting from a
# fruits = ["apple","banana","cherry","kiwi","mango"]
# newList = []

# for x in fruits:
#     if "a" in x:
#         newList.append(x)

# print(newList)

# list comprehension

# newList = [x for x in fruits if "a" in x]
# print(newList)

# Syntax : [expression for item in iterable if condition == True]

########################################## Sort List #################################

# Sort method sort the list alphabetically. 

# fruits = ["orange","apple","banana","cherry","kiwi","mango"]
# fruits.sort()
# print(fruits)

#Sort method sort the number numerically
# num = [9,3,6,2,0,1,5]
# num.sort();
# print(num)

#Sort decending use keyword reverse = true
# num = [9,3,6,2,0,1,5]
# num.sort(reverse = True)
# print(num)