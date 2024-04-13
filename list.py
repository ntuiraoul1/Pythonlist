# Working with lists
#  a list defined as similar to a variable

# Countries = [
    # 'Cameroon',
    # 'Brasil',
    # 'United States'
    # 'Belgium'
# ]

# Countries[0] = 'Congo'
# Countries[1] = 'Portugal'


# print(type(Countries))

# to get the index, you put 
# the variable list name and 
# add square brackets and put 
# the index within, when you 
# put 2 brackets, with indices
# within, you are saying that the
# program should go to the list 
# and print the particular index 
# letter found in the first index
#  and when you say [1:] the program 
# prints all the elements from index 
# position 1 to the end

# if you want to know the datatype 
# of a variable, you put type(variable_name)

# since the program runs line by line, 
# you can replace a giiven element in a 
# list by just giving new element name 
# and indexing it in the next line
# not that you cannot use this approach 
# to add an element to a list.




# observe that while indexing,we start 
# from zero(indexing from the beginner) 
# this is because zero is a neutral number
# (in terms of sign) so it is used to start 
# indexing, but then staring indexing from 
# the back, we start from -1 to get the 
# length of the list, you simply say len(variale_name).




# List attributes and methods

list1 = [1,2,3,4,5]
list2 = ['banana', 'apples', 'mangoes', 'oranges']

# these are 2 lists, lets say we want to 
#  join them together, we use the extend method

list1.extend(list2)
list2.append('Pineapple')
print(list2)
print(list1)

# you can also search for the index of a given element in the list by using 
# print(list2.index('mango')) but if you are 
# rather interesteed in the number of times given value apears in a list, 
# use the mango .count method as follows
# if you want to add to a list, you use the append attribute 