# Exercise: Assignment-2
""" This function takes in one number and returns one number."""

def sumofdigits(n_1):
    '''
    n_1 is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if n_1 == 0:
        return 0
    rem = n_1%10
    n_1 = n_1//10
    return rem + sumofdigits(n_1)

def main():
    "to find sum of digits of a given no"
    a_1 = input()
    print(sumofdigits(int(a_1)))

if __name__ == "__main__":
    main()
