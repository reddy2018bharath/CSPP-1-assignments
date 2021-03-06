'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    """to remove special characters"""
    str_1 = ""
    for i in string:
        for k in i:
            if k.isalpha() or k.isnumeric():
                str_1 += k
    return str_1

def main():
    """main function"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
