#Time to reveiw all the basics data types we learned! this should be relatively straignt forward and quick reassignment

###############################
########## Problem 1 ##########
###############################

# Given a string

s = 'django'

# use indexing to print out the following

print('Answers to problem one')
#'d'
print(s[0])
#'o'
print(s[-1])
#'djan'
print(s[:4])
#'jan'
print(s[1:4])
#'go'
print(s[4:6])

#Bonus: Use indexing to reverse the strings
print(s[::-1])

###############################
########## Problem 2 ##########
###############################

#Given this nested list
l = [3,7,[1,4,'Hello']]
#Reassign 'hello' to be 'goodbye'

print('Answers to problem two')
l[2][2] = 'goodbye'.capitalize()
print(l)

###############################
########## Problem 3 ##########
###############################
#Using keys and indexing, grab the 'hello' from the following Dictionaries
print('Answers to problem three')

d1 = {'simple_key': 'Hello'}
print(d1['simple_key'])

d2 = {'key1':{'key2':'Hello'}}
print(d2['key1']['key2'])

d3 = {'key1':[{'nest_key':['This is too deep', ['Hello']]}]}
print(d3['key1'][0]["nest_key"][1][0])


###############################
########## Problem 4 ##########
###############################

#Use a set to find a unique value of the list below
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

print('Answers to problem four')
print(set(mylist))


###############################
########## Problem 5 ##########
###############################

#You are given two variables:
age = 4
name = 'Sammy'

#Use print formating to print the following string:
"Hello my Dog's name is Sammy and he is 4 years old"
print('Answers to problem five')

print("hello my dog's name is", name, 'and he is', age, 'years old')

print("hello my dog's name is {a} and he is {b} years old.".format(a = name, b=age))
