'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num = int(input("enter a number: "))
    for i in range(1,num+1):
        if i%15==0:
            print("fizz")
            print("buzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)

if __name__ == "__main__":
    main()
