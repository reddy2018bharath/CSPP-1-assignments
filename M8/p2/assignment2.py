# Exercise: Assignment-2
""" This function takes in one number and returns one number."""


def sumofdigits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if n == 0:
        return 0
    else:
        rem = n%10
        n = n//10
        return rem + sumofdigits(n)


def main():
    "to find sum of digits of a given no"
    a = input()
    print(sumofdigits(int(a)))  

if __name__ == "__main__":
    main()

