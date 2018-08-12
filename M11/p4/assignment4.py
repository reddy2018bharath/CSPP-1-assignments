"""calculate hand"""
def calculatehandlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    sum_1 = 0
    for i in hand:
        sum_1 = sum_1+hand[i]
        i = i
    return sum_1
def main():
    """calculate hand"""
    n_1 = input()
    adict = {}
    for i in range(int(n_1)):
        data = input()
        i = i
        l_1 = data.split()
        adict[l_1[0]] = int(l_1[1])
    print(calculatehandlen(adict))
if __name__ == "__main__":
    main()
