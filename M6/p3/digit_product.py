'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    a=int_input
    c=1
    if a>0:
        while a>0:
            b=a%10
            c=c*b
            a=a//10
        print(c)
    elif a<0:
        a=-a
        while a>0:
            b=a%10
            c=c*b
            a=a//10
        print(-c)
    
    
    


if __name__ == "__main__":
    main()
