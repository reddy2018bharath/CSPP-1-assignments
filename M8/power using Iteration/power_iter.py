""" Exercise: PowerIter"""
# This function takes in two numbers and returns one number.
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    res = 1
    for i in range(1, exp+1):
        res = res*base
    return res
def main():
    """power using iteration"""
    data = input()
    data = data.split()
    print(iterPower(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
