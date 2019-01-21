#Function for checking equalness of two numbers
def checkEq(a,b,c):
    #Checking all pairs of parameters
    if a == b or b == c or a == c:#If one of them True function will return True
        return True
    #If none of conditions was reached 
    else:
        return False

#Modified function to check which check string values of numbers too
def checkEqS(a,b,c):
    #First is converting all params to int
    a=int(a)
    b=int(b)
    c=int(c)
    if a == b or b == c or a == c:
        return True
    else:
        return False
#Testing functions
print(checkEq(4,2,6))#False
print(checkEq(4,2,4))#True
print(checkEq(4,24,24))#True
print(checkEq(767,75,"767"))#False
print(checkEqS(767,75,"767"))#True