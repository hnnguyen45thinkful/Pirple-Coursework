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
# First one here is a function to add the "myUniqueList" with the statement needing to be if the value does exist, it should not be added, and the function should return False.
def addmyUniqueListData(insertData):
    if insertData in myUniqueList:
        addmyDuplicateListData(insertData)
        return False
    else:
        myUniqueList.append(insertData)
        return True
# Lastly create another function to add data to reject from the list that exist

# Next I am creating a function called addDuplicateDataToList() to add rejected data to list
def addmyDuplicateListData(sameData):
    return myLeftovers.append(sameData)

# Testing all datas and strings to the existing two functions.

addmyUniqueListData("Python")
addmyUniqueListData(33)
addmyUniqueListData("Developer")
addmyUniqueListData("45")
print(myUniqueList)
print(myLeftovers)
# Results so adding works and leftovers is empty perfect now testing and taking away from list below
# ['Python', 33, 'Developer', '45']
# []
addmyDuplicateListData(33)
addmyDuplicateListData("45")
print(myUniqueList)
print(myLeftovers)
# Results so leftovers I took out 33 and "45"
# ['Python', 33, 'Developer', '45']
# [33, '45']

# Lastly
addmyUniqueListData("professional")
addmyUniqueListData(65)
addmyDuplicateListData("professional")
addmyDuplicateListData(65)
print(myUniqueList)
print(myLeftovers)
# Results overall it works after testing many parts.
# ['Python', 33, 'Developer', '45', 'professional', 65]
# [33, '45', 'professional', 65]






