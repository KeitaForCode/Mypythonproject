##########################################
######## FUNCTION EXERCISE###############
########################################

#Complete the task below by writing functions, keep in mind,
#These might be really taugh, it all about breaking the problem down into smaller, logical
#steps.


#########################################
########### ---Problem 1 ---############
#########################################

#given the list of integer, return true is the sequence of number 1,2,3 appears
#in the list somewhere

#for example

#arraycheck([1,1,2,3,1]) true
#arraycheck([1,1,2,4,1]) false
#arraycheck([1,2,1,2,3]) true

def arraycheck(nums):

    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+ 1] == 2 and nums[i+ 2] == 3:
            return True
        else:
            return False

print(arraycheck([1,2,3,3,1]))
print(arraycheck([1,1,2,4,1]))
print(arraycheck([1,2,1,2,3]))

#########################################
########### ---Problem 2 ---############
#########################################

#Given a String, return a new string made up of every character starting with the first so 'hello' yields 'hlo'

#for example

#StringBit('Hello') = 'Hlo'
#StringBit('Hi') = 'H'
#StringBit('Heeololeo') = 'Hello'

def stringBit(mystring):

    result = ''

    for i in range(len(mystring)):
        if i % 2 == 0:
            result = result + mystring[i]

    return result

print(stringBit('Heeololeo'))


#########################################
########### ---Problem 3 ---############
#########################################

#Given two strings return true if either of the string appears at the very end
#of the other string, ignoring upper/lower case differences (in other words the
#computation should not be 'case sensitive')

#example

#end_other('Hiabc', 'abc') = true
#end_other('AbC', 'HiaBc') = true
#end_other('abc', 'abXabc') = true

def end_other(a, b):
    a.lower()
    b.lower()

    return (b.endswith(a) or a.endswith(b))

    #return a[-(len(b)):] == b or a == b[-(len(a)):]

print(end_other('HiaBc', 'abc'))

#########################################
########### ---Problem 4 ---############
#########################################

#Given a String, return a string where for every character in the original,
#there are two characters

#doubleChar('The') = TThhee
#doubleChar('AABB') = AAAABBBB
#doubleChar('Hi-There') = HHii--TThheerree

def doubleChar(mystring):
    result = ''

    for char in mystring:
        result += char*2
    return result

print(doubleChar('AAbb'))

#########################################
########### ---Problem 5 ---############
#########################################

#Read this problem statement very carefully

#Given three int values, a,b,c, return their sum. However if any of the values is a
#teen - in the range of 13-19 inclusive, then that value count as 0, accept 15
#and 16 do not count as a teens, write a seperate helper 'def fix_teen(n)' that takes
#in an int value and return that fixed for the teen rule.
#
#In this way, you avoid repeating the teen code 3 times (i.e decomposition).
#define the helper below and at the same indent level as the main no_teen_sum().
#Again, You will have two functions for this problem

#examples

#no_teen_sum(1,2,3) = 6
#no_teen_sum(2,13,1) = 3
#no_teen_sum(2,1,14) = 3

def no_teen_sum(a,b,c):
    return fixed_teen(a) + fixed_teen(b) + fixed_teen(c)

def fixed_teen(n):
    if n in [13,14,15,16,17,18,19]:
        return 0
    return n

print(no_teen_sum(2,13,1))



#########################################
########### ---Problem 6 ---############
#########################################

#Return the number of even integers in the given array

#example

#count_evens([2,1,2,3,4]) = 3
#count_evens([2,2,0]) = 3
#count_evens([1,3,5]) = 0

def count_evens(nums):
    count = 0

    for element in nums:
        if element % 2 == 0:
            count += 1
    return count

print(count_evens([2,4,6,8,10]))
