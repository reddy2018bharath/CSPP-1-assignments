'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    pass
    """sorting a dictionary"""
    list_1 = list(dictionary.keys())
    list_1.sort()
    for i in range(len(list_1)):
        
    for i in range(len(list_1)):
        print(list_1[i], "-", dictionary[list_1[i]]*"#")

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
