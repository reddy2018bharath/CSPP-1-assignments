"""string""" 

def main():
        """string"""
    str_= input()
    coun_= 0
    for char_ in str_:
        if char_ in ('a','e','i','o','u'):
            coun_=coun_+ 1
    print(coun_)

if __name__== "__main__":
	main()
