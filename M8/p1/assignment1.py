# Exercise: Assignment-1
"""This function takes in one number and returns one number."""
def factorial(n_2):
    """factorial of n"""
    if n_2 == 1:
        return 1
    return n_2*factorial(n_2 - 1)
def main():
    """ to find factorial of a given number"""
    a_1 = input()
    print(factorial(int(a_1)))
if __name__ == "__main__":
    main()
