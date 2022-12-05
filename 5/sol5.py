
def outShuffle(cards):
    l = len(cards)
    shuffledCards = [None]*l
    shuffledCards[::2] = cards[:int(l/2)]
    shuffledCards[1::2] = cards[int(l/2):]
    return shuffledCards

i = 2
while True:
    i += 2
    ls = list(range(1,i+1))
    less = False
    for j in range(12):
        ls = outShuffle(ls)
        if (ls == list(range(1,i+1))):
            less = True
            break
            #print("less with", i, "needed", j+1, "shuffles")
    ls = outShuffle(ls)
    if ls == list(range(1,i+1)) and (not less):
        print("Success with " + str(i))
        break
    #else:
    #    print("More with", i)

