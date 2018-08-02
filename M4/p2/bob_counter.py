"""bob"""
def main():
    """bob"""
    str1 = input()
    str2 = "bob"
    str3 = ""
    coun = 0
    for i in range(len(str1)-2):
        str3 = str1[i] + str1[i+1] + str1[i+2]
        if str3 == str2:
            coun = coun+1
    print(coun)
if __name__ == "__main__":
    main()
