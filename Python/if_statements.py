'''
Python Homework Assignment #3
Creating If-Statements
By: Hieu Nguyen

'''

# Goal is to check for at least two numbers that ARE the SAME!!!
# Defining all numbers chosen number 1 to 3
def EqualNumbersIntegers(number_1,number_2,number_3):
    if number_1 == number_2 or number_2 == number_3 or number_1 == number_3:
    # Transition Property number 1 = number 2, number 2 = number 3, then number 1 = number 3 same time 
    # implies to a = b, b = c, then a = c.
        return True
    # Otherwise if the results don't work then its goes false.
    else:
        return False

#Modified function to check which check string values of numbers too
def EqualNumbersStrings(number_1,number_2,number_3):
# After testing it with numbers and strings numbers I have to use int to convert the numbers to integers on all numbers.
    number_1 = int(number_1)
    number_2 = int(number_2)
    number_3 = int(number_3)
    # Same transition property from above number 1 = number 2, number 2 = number 3, then number 1 = number 3 same time 
    # implies to a = b, b = c, then a = c. 
    if number_1 == number_2 or number_2 == number_3 or number_1 == number_3:
        return True
    # Otherwise if the results don't work then its goes false.    
    else:
        return False
# Using numbers and string numbers to see if the functions are working. Results on the side.
# Random Numbers not matching each other.
print(EqualNumbersIntegers(4,2,6)) # False
# Numbers with one of them being the same.
print(EqualNumbersIntegers(4,2,4)) # True
# Numbers with one of them being the same from above but next to each other ex (1,2,2).
print(EqualNumbersIntegers(4,24,24)) # True
# Now testing the numbers with a string number with two random numbers.
print(EqualNumbersIntegers(10,25,"67")) # False
# Now testing the numbers with the same one of each integer and string integer and another number.
print(EqualNumbersStrings(65,75,"65")) # True
# Now testing the numbers with two number strings and another number randomly.
print(EqualNumbersStrings(25,"25","75")) # True
# Now testing with two strings numbers and also random numbers.
print(EqualNumbersStrings(25,"76","75")) # False
# Now testing with three strings numbers.
print(EqualNumbersStrings("25","76","75")) # False
# Now testing with three strings numbers two are the same.
print(EqualNumbersStrings("25","25","75")) # False
