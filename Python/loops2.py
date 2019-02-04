'''
Python Homework Assignment #6
Advanced Loops 
By: Hieu Nguyen

'''
# Details:
 
# Create a function that takes in two parameters: rows, and columns, both of which are integers. The function should then proceed to draw a playing board (as in the examples from the lectures) the same number of rows and columns as specified. After drawing the board, your function should return True.


# Extra Credit:

# Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping. If someone passes a value greater than either maximum, your function should return False. 


# def gamePlayingBoard(rows, columns)
"""
"""
def draw(rows, coloumns):
    for x in range(0, rows):
        if (x % 2 == 0):
            for y in range(1, coloumns + 1):
                if (y % 2 == 1):
                    if (y != coloumns):
                        print(" ", end='')
                    else:
                        print(" ")

                else:
                    print("|", end='')
        else:
            print("------")

draw(10,5)

