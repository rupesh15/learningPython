# first_word = "Rupesh"
# last_word = "Pathak"

# #print(first_word+last_word)
# #print(first_word+" "+ last_word);
# #print(first_word*5)

# # Can write the string with multiple line by 3 """ or '''
# s = """I am learning
# python on my own"""
# print(s)

#s = "this is rupesh"
# print(s[3]) # output -  s
# print(s[-4]) # output - p
#print(s[50]) # will throw IndexError: string index out of range


########################################## String Slicing #################################

#string_value = "rupeshpathak"
# print(string_value[1:6]) # upesh
# print(string_value[:6])  #rupesh
#print(string_value[2:])
# print(string_value[::-1]) #string reversal "kahtaphsepur"
# print(string_value[::1]) # same "rupeshpathak"
# print(string_value[::-2])  # khaheu

########################################## String Iteration #################################

# s = "python"
# for char in s:
#     print(char)

########################################## String Immutability #################################

# name = "rupeshpathak"
# name = "R" + name[1:6] + "P" + name[7:]
# print(name)

# name = "rupesh" 
# print(id(name)) 140473348959568
# name = "pathak" 140473348969984
# print(id(name)) both id is id differnt which mean both are different variable with same name

########################################## Delete String #################################

# s = "rupesh"
# print(s)
# del s
# print(s) will throw error as s is already deleted: NameError: name 's' is not defined

########################################## Updating String #################################

# s = "rupeshPathak is my name"
# s1 = "R" + s[1:]
# s2 = s.replace("name", "fullname")
# print(s1)
# print(s2)
# s[0] = "L"
# print(s) As string in immutable so value of string will not get replaced

########################################## Common String Methods #################################

# name = "rupesh"
# lastname = "PATHAK"
# print(len(name))
# print(name.upper())
# print(lastname.lower())

# s = "  rupesh Pathak    "
# print(s.strip()) strip will strip the whitespace
# print(s.replace("Pathak", "Kumar Pathak")) replace will replace the file

########################################## Concatenating and Repeating Strings #################################

# s1 = "Hello"
# s2 = "World"
# print(s1 + " " + s2) // Hello World

# s = "Hello "
# print(s * 3) // Hello Hello Hello 

########################################## Formatting Strings #################################

# firstname = "Rupesh"
# lastname = "Pathak"
# print(f"first name is {firstname} and lastname is {lastname}");
#print("first name is {} and lastname is {}".format("rupesh","pathak") );

########################################## Formatting Strings #################################

# name = "RupeshPathak"
# print("Pathak" in name) // true
# print("ravi" in name)  // false
