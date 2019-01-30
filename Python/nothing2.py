def draw_board(rows, columns):  
    verticals = columns*2 # real number of elements that define the column
    horizontals = rows*2 # real number of elements that define the row
    for row in range(horizontals-1):
        if row%2 == 0:
            for column in range(1, verticals):
                if column % 2 == 1:
                    if column != verticals-1:
                        print(" ", end = "")
                    else:
                        print(" ")
                else:
                    print("|", end = "")
        else:
            print("-"*(verticals-1))

print(draw_board(5, 7))