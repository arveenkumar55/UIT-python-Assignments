#!/usr/bin/env python
# coding: utf-8

# In[41]:


"""Wordcount exercise
Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
def print_words(filename):
    dic={}
    with open(filename,'r') as f:
        output = f.readlines()
        for line in output:
            data=line.split()
            for value in data:
                string=value.lower()
                if string in dic:
                    dic[string]=dic[string]+1
                else:
                    dic[string]=1
    for value in sorted(dic):
        print(value + '      .....' +str(dic[value]))
                    
def print_top(filename):
    dic={}
    with open(filename,'r') as f:
        output = f.readlines()
        for line in output:
            data=line.split()
            for value in data:
                string=value.lower()
                if string in dic:
                    dic[string]=dic[string]+1
                else:
                    dic[string]=1
    sorted_dictionary = sorted(dic.items(),key=lambda x: x[1],reverse=True)
    size= len(sorted_dictionary)
    dict1 ={}
    if size>=20:
        for i in range(0,20):
            print(str(sorted_dictionary[i][0]) + '      .....' +str(sorted_dictionary[i][1]))

    
    else:
        print("files doesn't contain 20 distinct words")


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print ('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print ('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()


# In[ ]:




