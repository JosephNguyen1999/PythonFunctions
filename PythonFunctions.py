#!/usr/bin/env python
# coding: utf-8

# # CSCI 3360 Homework 1

# ## Instructions

# The first homework assignment is designed to get yourself familiar with the Python programming lanaguage. You are to complete this assignment individually, but you may do general searches on the Internet if you are unsure how to complete a certain task using Python (be sure to cite the source of your help). **Please do not use any external libraries that we have not explicitly discussed in class (e.g., NumPy) to complete this homework**.
# 
# The skeleton code and some sample test cases are provided for you. You are to implement the functions and thoroughly test your code with more test cases. You may assume that the given input parameters are of the correct type, but you may still need to check the validity of the input. You are not allowed to modify the names and parameters of functions. You may choose to write additional helper functions if needed.
# 
# When you are finished, please submit a **Python script file (.py extension) named hw1.py** to eLC before the deadline.
# 
# If you are using Jupyter Notebook, please click **File -> Download as -> Python (.py)** to generate the Python script file. Do **NOT** submit the Jupyter Notebook file (.ipynb extension). Please be sure to excute the Python script file in the command line/console/shell/terminal to make sure your code still runs as expected.

# ## Academic Honesty Statement

# Please first complete the Academic Honesty Statement by filling in your name below. **Any homework submission without the Academic Honesty Statement properly filled in will receive a grade of 0**.

# In[1]:


# first fill in your name
first_name = "Joseph"
last_name  = "Nguyen"

print("****************************************************************")
print("CSCI 3360 Homework 1")
print(f"completed by {first_name} {last_name}")
print(f"""
I, {first_name} {last_name}, certify that the following code
represents my own work. I have neither received nor given 
inappropriate assistance. I have not consulted with another
individual, other than a member of the teaching staff, regarding
the specific problems in this homework. I recognize that any 
unauthorized assistance or plagiarism will be handled in 
accordance with the University of Georgia's Academic Honesty
Policy and the policies of this course.
""")
print("****************************************************************")


# ## Problem 1

# You will be given a string containing only the characters `():`
# 
# Implement the function that returns a number based on the number of sad and smiley faces there are.
# - The happy faces `:)` and `(:` are worth 1.
# - The sad faces `:(` and `):` are worth -1.
# 
# For example, `happy_number(':):(') -> -1`
# - The first 2 characters are `:)`        +1      (Total: 1)
# - The next 2 are `):`                    -1      (Total: 0)
# - The last 2 are `:(`                    -1      (Total: -1)

# In[2]:


# TODO: implement this function
def happy_number (s):
    a = 0
    if ":)" or "(:" in s:
        counter = s.count(":)") + s.count("(:")
        a += counter
    if ":(" or "):" in s:
        counter = s.count(":(") + s.count("):")
        a -= counter
    return a


# In[3]:


# Sample test cases. You should write more test cases to thoroughly test your code
assert happy_number(':):(') == -1
assert happy_number('(:)') == 2
assert happy_number('::::') == 0
# Additional test cases
assert happy_number("") == 0
assert happy_number(":):):):):):):)") == 1
assert happy_number("):):(") == -2


# ## Problem 2

# Using list comprehensions, implement the function that returns all even numbers from 0 until the given number (exclusive). Return an empty list if the input parameter <= 0.

# In[4]:


# TODO: implement this function
def find_even_nums (n):
    evenNumber = list()
    for x in range(n):
        if x % 2 == 0:
            evenNumber += [x]
    return evenNumber


# In[5]:


# Sample test cases. You should write more test cases to thoroughly test your code
assert find_even_nums(8) == [0, 2, 4, 6]
assert find_even_nums(5) == [0, 2, 4]
assert find_even_nums(2) == [0]
assert find_even_nums(0) == []
# Additional test cases
assert find_even_nums(-10) == []
assert find_even_nums(-2) == []
assert find_even_nums(10) == [0, 2, 4, 6, 8]
assert find_even_nums(3) == [0, 2]


# ## Problem 3

# Implement the function that takes a string and returns the number of vowel letters contained within it. Only consider 'a', 'e', 'i', 'o', and 'u' as vowels (not 'y').
# 

# In[6]:


# TODO: implement this function
def count_vowels (s):
    a = 0
    if "a" or "e" or "i" or "o" or "u" in s:
        counter = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")
        a += counter
    return a


# In[7]:


# Sample test cases. You should write more test cases to thoroughly test your code
assert count_vowels("Celebration") == 5
assert count_vowels("Palm") == 1
assert count_vowels("Prediction") == 4
# Additional test cases
assert count_vowels("aaaaaa") == 6
assert count_vowels("little") == 2
assert count_vowels("hellohello") == 4
assert count_vowels("") == 0


# ## Problem 4

# Implement the function that returns the prime factorization of an integer as a sorted list of tuples. Include the multiplicity of each prime in the tuples:
# - [(prime_0, mult_0), ... , (prime_k, mult_k)]
# - where prime_0 < prime_1 < ... < prime_k
# 
# Please note that 1 is not prime. All inputs will be < 10000.

# In[8]:


# TODO: implement this function
from collections import Counter

def factorize (n):
    x = 2
    primeFactors = list()
    while x < n:
        if n % x:
            x += 1
        else:
            n /= x
            primeFactors.append(x)
    if n > 1:
        primeFactors.append(n)
    primeFactorsMult = list(Counter(primeFactors).items())
    return primeFactorsMult


# In[9]:


# Sample test cases. You should write more test cases to thoroughly test your code
assert factorize(1)  == []
assert factorize(2)  == [(2, 1)]
assert factorize(4)  == [(2, 2)]
assert factorize(10) == [(2, 1), (5, 1)]
assert factorize(60) == [(2, 2), (3, 1), (5, 1)]
# Additional test cases
assert factorize(-10)  == []
assert factorize(0)  == []
assert factorize(36)  == [(2, 2), (3, 2)]
assert factorize(100) == [(2, 2), (5, 2)]


# ## Problem 5

# Implement the function that takes:
# 1. A list of keys.
# 2. A list of values.
# 3. `True`, if key and value should be swapped, else `False`.
# 
# The function returns the constructed dictionary. If input lists are empty or of different sizes, return an empty dictionary. You may assume that keys and values only contain unique values.

# In[10]:


# TODO: implement this function
def swap_d (keys, values, swap):
    keysValuesSwap = dict()
    if keys and values and len(keys) == len(values):
        if swap:
            keysValuesSwap = dict(zip(values, keys))
        else:
            keysValuesSwap = dict(zip(keys, values))
        return keysValuesSwap
    else:
        return keysValuesSwap


# In[11]:


# Sample test cases. You should write more test cases to thoroughly test your code
assert swap_d ([], [1], False) == {}
assert swap_d ([1, 2, 3], ["one", "two", "three"], False) == { 1: "one", 2: "two", 3: "three" }
assert swap_d ([1, 2, 3], ["one", "two", "three"], True) == { "one": 1, "two": 2, "three": 3 }
assert swap_d (["Paris", 3, 4.5], ["France", "is odd", "is half of 9"], True) == { "France": "Paris", "is odd": 3, "is half of 9": 4.5 }
# Additional test cases
assert swap_d ([], [1], True) == {}
assert swap_d ([1, 2, 3], [1, 2, 3, 4], True) == {}
assert swap_d ([1, 2, 3], [1, 2, 3, 4], False) == {}
assert swap_d (["hi", "yo"], ["bye", "goodbye"], False) == {"hi": "bye", "yo": "goodbye"}


# ## Problem 6

# Given an integer `limit` being the upper limit of the range of interest, implement the function that returns the last 15 (or however many if there are not enough) palindromes numbers `<= limit` as a list sorted ascendingly. 
# 
# 

# In[12]:


# TODO: implement this function
def generate_palindromes (limit):
    x = 0
    listOfPalindromes = list()
    for i in range(limit, -1, -1):
        stringI = str(i)
        if x == 15:
            listOfPalindromes.sort()
            return listOfPalindromes
        elif stringI == stringI[::-1]:
            listOfPalindromes.append(i)
            x += 1
    listOfPalindromes.sort()
    return listOfPalindromes


# In[13]:


# Sample test cases. You should write more test cases to thoroughly test your code
assert generate_palindromes(30) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22]

assert generate_palindromes(151) == [11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151]

assert generate_palindromes(600) == [454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595]

assert generate_palindromes(999999) == [985589, 986689, 987789, 988889, 989989,
                                        990099, 991199, 992299, 993399, 994499,
                                        995599, 996699, 997799, 998899, 999999]
# Additional test cases
assert generate_palindromes(5) == [0, 1, 2, 3, 4, 5]
assert generate_palindromes(-1) == []


# ## Problem 7

# Implement the function that generates a bar chart of the popularity of programming Languages and saves it as "popularity.png" to the current directory.
# - The bars should be green
# - The title of the bar chart should be "Popularity of Programming Languages"
# - The x-axis label should be "Programming Languages"
# - The y-axis label should be "Popularity"

# In[14]:


import matplotlib.pyplot as plt

# TODO: implement this function
def bar_chart (languages, popularity):
    # generates and customize your bar chart here
    plt.bar(languages, popularity, color = "g")
    plt.title("Popularity of Programming Languages")
    plt.xlabel("Programming Languages")
    plt.ylabel("Popularity")

    
    
    plt.savefig('popularity.png')
    


# In[15]:


# Sample test cases. You should write more test cases to to generate bar charts with different data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
bar_chart (languages, popularity)

# Additional test cases
# plt.gca().clear()
# languages = ['Java', 'Python', 'PHP', 'JavaScript']
# popularity = [25, 125, 180, 80]
# bar_chart (languages, popularity)

# plt.gca().clear()
# languages = []
# popularity = []
# bar_chart (languages, popularity)

# Now check your current directory to see the bar chart


# In[16]:


# be sure clear each plot before generating the next one
plt.gca().clear()


# ## Problem 8

# Implement the function that generates a scatter plot comparing students' final exam scores in Math and Science and saves it as "scores.png" to the current directory.
# - The dots should be blue
# - The title of the scatter plot should be "Math Scores vs. Science Scores"
# - The x-axis label should be "Math Scores"
# - The y-axis label should be "Science Scores"

# In[17]:


# TODO: implement this function
def scatter_plot (math, science):
    # generates and customize your bar chart here
    plt.scatter(math, science, color = 'b')
    plt.axis("equal")
    plt.title("Math Scores vs. Science Scores")
    plt.xlabel("Math Scores")
    plt.ylabel("Science Scores")
    
    
    
    plt.savefig('scores.png')
    


# In[18]:


# Sample test cases. You should write more test cases to to generate scatter plots with different data
math    = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
scatter_plot (math, science)

# Additional test cases
# plt.gca().clear()
# math    = [150, 220, 200]
# science = [300, 50, 1]
# scatter_plot (math, science)

# plt.gca().clear()
# math    = []
# science = []
# scatter_plot (math, science)


# ## Problem 9

# Recall the matrix transpose operation discussed in class. Now implement the function that returns the transpose of a matrix (represented by a 2-dimensional list).

# In[19]:


# Importing typing annotations for matrix
from typing import List

Matrix = List[List[float]]


# In[20]:


def numColumns (A):
    return len(A[0])

def numRows (A):
    return len(A)

# TODO: implement this function
def transpose (A: Matrix) -> Matrix:
# Initial Attempt (Inefficient but works)
#    x = 0
#    y = 0
#    yList = list()
#    bMatrix = list()
#    while x < len(A[0]):
#        yList = list()
#        for i in range(len(A)):
#            yList.append(A[i][y])
#        y += 1
#        bMatrix.append(yList)
#        x += 1         
#    return bMatrix

    bMatrix = [list(value)for value in zip(*A)]
    return bMatrix


# In[21]:


# Sample test cases. You should write more test cases to thoroughly test your code
A = [[1, 2, 3],
     [4, 5, 6]]

At = [[1, 4],
      [2, 5],
      [3, 6]]

assert transpose (A) == At
assert transpose (At) == A

I = [[1, 0],
     [0, 1]]

assert transpose (I) == I

# Additional test cases

B = [[4, 4, 4, 4, 4, 4, 4], 
     [5, 5, 5, 5, 5, 5, 5], 
     [6, 6, 6, 6, 6, 6, 6]]

Bt = [[4, 5, 6], 
      [4, 5, 6], 
      [4, 5, 6], 
      [4, 5, 6], 
      [4, 5, 6], 
      [4, 5, 6], 
      [4, 5, 6]]

assert transpose (B) == Bt

PO = [[0, 0],
      [0, 0]]

assert transpose (PO) == PO

C = [[]]

assert transpose (C) == []


# ## Problem 10

# Recall the matrix multiplication operation discussed in class. Now implement the function that returns the product of two matrices. if the dimensions of the input matrices are incompatible, print an error message and return `None`.

# In[22]:


def dotProduct(a, b) -> float:
    return sum(a * b for a, b in zip(a, b))

# TODO: implement this function
def matrix_mult (A: Matrix, B: Matrix) -> Matrix:
    if numColumns(A) != numRows(B):
        print("Error Message: Dimensions of the input matrices are incompatible.")
        return None
    else:
        matrixAnswer = [list(dotProduct(aRows, bColumns) for bColumns in zip(*B)) for aRows in A]
    return matrixAnswer


# In[23]:


# Sample test cases. You should write more test cases to thoroughly test your code
A_At = [[14, 32],
        [32, 77]]

At_A = [[17, 22, 27],
        [22, 29, 36],
        [27, 36, 45]]

assert matrix_mult (A, At) == A_At
assert matrix_mult (At, A) == At_A

assert matrix_mult (I, A)  == A
assert matrix_mult (At, I) == At

# Additional test cases
zeroMatrix = [[0, 0],
              [0, 0]]

oneMatrix = [[1, 1],
             [1, 1]]

assert matrix_mult (PO, PO) == zeroMatrix
assert matrix_mult (I, PO) == zeroMatrix
assert matrix_mult (oneMatrix, I) == oneMatrix

# Incompatible dimensions
# Should print error message
assert matrix_mult (At_A, PO) == None

