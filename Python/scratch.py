# # """
# # 	Homework Assignment #4
# # 	Lists
# # 	Add unique elements to list
# # 								"""

# # myUniqueList = [] # New unique elements will be added to this list
# # myLeftovers = [] # Duplicate of existing elements of myUniqueList will be added here

# # def addToList(member):
# # 	if member not in myUniqueList: # Adds unique elements to myUniqueList and returns True
# # 		myUniqueList.append(member)
# # 		return True
# # 	else:
# # 		myLeftovers.append(member) # Rejected elements will be added to myLeftovers and returns False
# # 		return False

# # # Let's add elements

# # addToList(3)
# # addToList('littleBuddha')
# # addToList(None)
# # addToList(3)
# # addToList(None)
# # addToList([])
# # addToList('Yogi')
# # addToList(True)
# # addToList(False)
# # addToList('Yogi')
# # addToList('1')
# # addToList([])
# # addToList(True)

# # # Results

# # print('myUniqueList:', myUniqueList)
# # print('myLeftovers:', myLeftovers)
# # myUniqueList = []
# # myLeftOvers = []

# # """
# # Add any thing to my list.  As long
# # as it is unique
# # """
# # def addToMyList(valueToAdd):
# #     if valueToAdd in myUniqueList:
# #         myLeftOvers.append(valueToAdd) #value exists, add to Left Overs
# #         return False
# #     else:
# #         myUniqueList.append(valueToAdd) #value does not exist, add it
# #         return True


# # # Add stuff to the list

# # addToMyList("Rodney")
# # addToMyList("Oliver")
# # addToMyList("Children")
# # addToMyList(["Emilee", "Aidan"])
# # addToMyList("Rodney")
# # addToMyList([16, 12])
# # addToMyList(["Emilee", "Aidan"])
# # addToMyList(12)

# # print(myUniqueList[3])
# # print(myUniqueList[3:])
# # print(myUniqueList[4][-1])
# # print(myUniqueList)

# # print("\n===The Left Overs===")
# # print(myLeftOvers)


# """
# Assignment #4 : Added unique element to myUniqueList and rejected data to myLeftovers
# """

# #Global list to add unique data
# myUniqueList = []
# #Global array to add rejected/duplicate data
# myLeftovers = []

# #Created function addUniqueDataToList() to add unique data to list
# def addUniqueDataToList(newData):
#     if newData in myUniqueList:
#         addDuplicateDataToList(newData)
#         return False
#     else:
#         myUniqueList.append(newData)
#         return True
# #Created function addDuplicateDataToList() to add rejected data to list
# def addDuplicateDataToList(duplicateData):
#     return myLeftovers.append(duplicateData)


# #Display result

# #Add new data 'A' to list myUniqueList and print myUniqueList,myLeftovers
# #Output - myUniqueList : ['A'] and myLeftovers : []
# addUniqueDataToList('A')
# print(myUniqueList)
# print(myLeftovers)

# #Try to add duplicate data 'A' to list myUniqueList and print myUniqueList,myLeftovers
# #Output - myUniqueList : ['A'] and myLeftovers : ['A']
# addUniqueDataToList('A')
# print(myUniqueList)
# print(myLeftovers)

# #Add new data 'B' to list myUniqueList and print myUniqueList,myLeftovers
# #Output - myUniqueList : ['A','B'] and myLeftovers : ['A']
# addUniqueDataToList('B')
# print(myUniqueList)
# print(myLeftovers)

"""
assignment no4
Lists
"""
#making empty list
myUniqueList=[]
myLeftovers=[]
#making function
def Uniqueness(number):
    if number not in myUniqueList:          #Action
        myUniqueList.append(number)
        return 'True'
    elif number in myUniqueList:
        myLeftovers.append(number)
        return 'False'
#calling and printing function
print(Uniqueness("fuck"))
print(Uniqueness("fuck"))
print(Uniqueness(0))
print(Uniqueness(8))
print(Uniqueness(0))
print(Uniqueness(1))
print(Uniqueness(2))
print(Uniqueness(3))
print(myUniqueList)
print(myLeftovers)