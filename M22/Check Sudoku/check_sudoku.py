'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    for i in sudoku:
        for k in i:
            if k not in "1 2 3 4 5 6 7 8 9":
                return False
        return True
def rows(sudoku):
    c=0
    for i in sudoku:
        a=set(i)
        if len(set(i))==9:
            c=c+1
    if c==9:
        return True
    return False
def columns(sudoku):
    transPose =[]
    for i in range(len(sudoku)):
        row=[]
        for j in range(len(sudoku[0])):
            row.append(sudoku[j][i])
        #row =[]
        #for j in range(len(sudoku[0])):
	    #row.append(sudoku[j][i])
        transPose.append(row)
    return rows(transPose)
def grid(sudoku):
    squares=[]
    for i in range(9, step=3):
        for j in range(9, step=3):
          square = list(itertools.chain(row[j:j+3] for row in grid[i:i+3]))
          squares.append(square)
    c==0
    for i in range(9):
        if len(set(squares(i)))==9:
            c=c+1
    if c==9:
        return True
    return False
    
    
def result(sudoku):
    if check_sudoku(sudoku):
        if rows(sudoku):
            if columns(sudoku):
                if grid(sudoku):
                    return True
    return False
        
    
    
            

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
