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
    ans = int_input
    cou=1
    if ans>0:
        while ans>0:
            bat = ans%10
            cou = cou*bat
            ans = ans//10
        print(cou)
    elif ans<0:
        ans = -ans
        while ans>0:
            bat = ans%10
            cou = cou*bat
            ans = ans//10
        print(-cou)
        
if __name__ == "__main__":
    main()
