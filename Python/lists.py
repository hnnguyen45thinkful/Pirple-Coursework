'''
Python Homework Assignment #4
Lists 
By: Hieu Nguyen

'''

# Creating and making an empty list from the given variable names (separate global array).
"""
Details:
 
Create a global variable called myUniqueList. It should be an empty list to start.

Next, create a function that allows you to add things to that list. Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList. If the value doesn't exist already, it should be added and the function should return True. If the value does exist, it should not be added, and the function should return False;

Finally, add some code below your function that tests it out. It should add a few different elements, showcasing the different scenarios, and then finally it should print the value of myUniqueList to show that it worked.


Extra Credit:

Add another function that pushes all the rejected inputs into a separate global array called myLeftovers. If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.
"""
myUniqueList = []
# Extra Credit create another separate global array 
myLeftovers = []

# Defining and Creating a function one true and false with creating an added values/integers/input and strings
# First one here is a function to add the "myUniqueList" with the statement needing to be if the value does exist, it should not be added, and the function should return False
def addmyUniqueList(insertData)
	if insertData in myUniqueList:
		addmyUniqueListData(insertData)
		return False
	else:
		myUniqueList.append(insertData)
		return True
