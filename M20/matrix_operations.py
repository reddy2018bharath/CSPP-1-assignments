def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = []
    if (len(m1[0]) == len(m2)):
        for i in range(len(m1)):
            resTemp = []
            for j in range(len(m2[0])):
                res = 0
                for k in range(len(m2)):
                    res += m1[i][k]*m2[k][j]
                resTemp.append(res)
            result.append(resTemp)
        return result
    else:
        print("Error: Matrix shapes invalid for mult")
        return None

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    pass
    if len(m1) != len(m2):
        print("Error: Matrix shapes invalid for addition")
        return
    for i,j in zip(m1,m2):
        if len(i) != len(j):
            print("Error: Matrix shapes invalid for addition")
            return
    result = []
    for i,j in zip(m1,m2):
        row = []
        for p,q in zip(i,j):
            row.append(p+q)
        result.append(row)
    return result
        
                
                

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows,columns = [int(i) for i in input().split(",")]
    matrix = []
    for i in range(rows):
        lst = [int(i) for i in input().split(" ")]
        if len(lst) != columns:
            print("Error: Invalid input for the matrix")
            return None
        matrix.append(lst)
    return matrix
   
    

def main():
    # read matrix 1
    m1 = read_matrix()

    # read matrix 2
    m2 = read_matrix()
    if (m1 != None and m2 != None):
        print(add_matrix(m1, m2))
        print(mult_matrix(m1,m2))
        

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()
