# Assignment-3
'''

Fill in the code for isValidWord in ps4a.py and be sure.
'''

def isvalid_word1(word, hand, word_list1):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    for i in word:
        if i not in hand:
            return False
        i = i
    return word in word_list1


def main():
    """word is valis or not"""
    word = input()
    n_1 = int(input())
    adict = {}
    for i_1 in range(n_1):
        data = input()
        l_1 = data.split()
        adict[l_1[0]] = int(l_1[1])
        i_1 = i_1
    l_2 = input().split()
    print(isvalid_word1(word, adict, l_2))
if __name__ == "__main__":
    main()
