# -*- coding: utf-8 -*-
"""
Created on Tue Nov 5 01:56:48 2019

@author: Eugenio
"""

def z_function(string):
    n = len(string)
    z = [n]

    for i in range(1, n):
        low_lim = up_lim = i
        while (up_lim < n and string[up_lim - low_lim] == string[up_lim]): up_lim += 1
        z.append(up_lim - low_lim)
    return z

# Enter and validate test_cases
while True:
    try:
        test_cases = int(input("Enter number of test cases (between 1 and 10): "))
        assert(test_cases > 0 and test_cases < 11), 'Number must be between 1 and 10'
        break
    except:
    	print("Please enter a valid amount of tests cases")

words = list()

# Enter and validate words to be analyse
for x in range (0, test_cases):
    
    while True:
        try:
            word = input('Enter word to be analyze: ')
            assert(word.islower()), 'String must be a-z'
            break
        except:
            print("Please enter a valid string")

    words.append(word)

#print(words)

print()
print("Solution")
print(*list(sum(z_function(x)) for x in words), sep = "\n")
