#!/usr/bin/env python
# coding: utf-8

# In[67]:


import math
# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    if len(s)<3:
        return s
    elif s[len(s)-3]+s[len(s)-2]+s[len(s)-1]!="ing":
        return s+"ing"
    else:
        return s+"ly"

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    value=''
    value1=''
    index=0
    data = s.split(' ')
    flag=False
    flag1=False
    for i in range(0,len(data)):
        if(data[i]=="not"):
            index=i  
            while i< len(data):
                value1=value1+" "+data[i]
                if data[i]=="bad":
                    flag=True
                    value=value+" "+"good"
                    return value
                    break
                if data[i]=="bad!":
                    flag=True
                    value=value+" "+"good!"
                    return value
                    break
                    
                i=i+1
            return value1
        if i<len(data) and flag1:
            value=value+" "+data[i]
            value1=value1+" "+data[i]
        else:
            flag1=True
            value=data[i]
            value1=data[i]
        if flag== True:
            break
    


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    value=''
    first_string_length1=math.ceil(len(a)/2)
    first_string_length2=math.floor(len(a)/2)
    second_string_length1=math.ceil(len(b)/2)
    second_string_length2=math.floor(len(b)/2)
    for i in range(0,first_string_length1):
        if i==0:
            value=a[i]
        else:
            value=value+a[i]
    for i in range(0,second_string_length1):
        value=value+b[i]
    for i in range(first_string_length1,first_string_length1+first_string_length2):
        value=value+a[i]
    for i in range(second_string_length1,second_string_length1+second_string_length2):
        value=value+b[i]
    return value


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print ('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    print
    print ('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    #print
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcdef', 'xyz'), 'abcxydefz')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()




# In[ ]:





# In[ ]:




