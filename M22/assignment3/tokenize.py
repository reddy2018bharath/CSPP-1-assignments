'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    a_1 = dict()
    for i in string:
	    if i not in a_1:
		    a_1[i] = a_1.count(i)
	    else:
		    a_1[i] += 1
    return a_1

            
def main():
	matrix=[]
    lines=int(input())
    for i in range(lines):
	    lst = [i for i in input().split(" ")]
    matrix.append(lst)
	print(tokenize(matrix))
	


if __name__ == '__main__':
    main()
