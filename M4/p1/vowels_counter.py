"""To find number of vowels in a string""" 
def main():
    str_ = input()
    coun_ = 0
    for char in str_:
        if char in ('a', 'e', 'i', 'o', 'u'):
            coun_ = coun_ + 1
    print(coun_)
 if __name__ == "__main__":
	main()
