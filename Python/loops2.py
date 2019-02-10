'''
Python Homework Assignment #6
Advanced Loops 
By: Hieu Nguyen

'''
# Details:
 
# Create a function that takes in two parameters: rows, and columns, both of which are integers. The function should then proceed to draw a playing board (as in the examples from the lectures) the same number of rows and columns as specified. After drawing the board, your function should return True.


# Extra Credit:

# Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping. If someone passes a value greater than either maximum, your function should return False. 
#Create function to display playing board
# Start Global rows and columns at 0 because positive numbers.
rows = 0
columns = 0
def GridBoard(rows,columns):
    if rows <=100 and columns <=100:
        for r in range(1, rows + 1):
            if r % 2 != 0:
                for c in range(columns):
                    if c%2 == 0:
                        if c != columns - 1:
                            print(" ",end="")
                    else:
                            print("|",end="")
                else:
                    print("")
            else:
                print("-" * columns)

        print(True)
    else:
        print(False)#Otherwise 

GridBoard(21,21)#True
GridBoard(90,101)#False
GridBoard(50,100)#True
GridBoard(90,101)#False
GridBoard(100,100)#True
GridBoard(90,101)#False