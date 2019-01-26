"""
Assignment #4 : Added unique element to myUniqueList and rejected data to myLeftovers
"""

#Global list to add unique data
myUniqueList = []
#Global array to add rejected/duplicate data
myLeftovers = []

#Created function addUniqueDataToList() to add unique data to list
def addUniqueDataToList(newData):
    if newData in myUniqueList:
        addDuplicateDataToList(newData)
        return False
    else:
        myUniqueList.append(newData)
        return True
#Created function addDuplicateDataToList() to add rejected data to list
def addDuplicateDataToList(duplicateData):
    return myLeftovers.append(duplicateData)


#Display result

#Add new data 'A' to list myUniqueList and print myUniqueList,myLeftovers
#Output - myUniqueList : ['A'] and myLeftovers : []
addUniqueDataToList('A')
print(myUniqueList)
print(myLeftovers)

#Try to add duplicate data 'A' to list myUniqueList and print myUniqueList,myLeftovers
#Output - myUniqueList : ['A'] and myLeftovers : ['A']
addUniqueDataToList('A')
print(myUniqueList)
print(myLeftovers)

#Add new data 'B' to list myUniqueList and print myUniqueList,myLeftovers
#Output - myUniqueList : ['A','B'] and myLeftovers : ['A']
addUniqueDataToList('B')
print(myUniqueList)
print(myLeftovers)