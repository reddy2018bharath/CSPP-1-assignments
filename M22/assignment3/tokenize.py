'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    pass
    matrix=[]
    lines=int(input())
	for i in range(lines):
		lst =[(i) for i in input().split(" ")]
	matrix.append(lst)
	a_1=dict()
	for i in matrix:
		if i not in a_1:
			a_1[i]=a_1.count(i)
		else:
			a_1[i]+=1

            
def main():
	


    pass

if __name__ == '__main__':
    main()
