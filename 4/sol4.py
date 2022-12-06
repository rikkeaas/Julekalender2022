from math import log

def baseConverter(bTo, n):
    numToChar = {i:"0123456789ABCDEF"[i] for i in range(16)}
    power = int(log(n, bTo))

    converted = ""

    for pow in range(power, -1, -1):
        converted += numToChar[n // (bTo**pow)]
        n %= bTo ** pow

    return converted
    

def isPalindrome(s):
    return s == s[::-1]

paliSum = 0


for gi in range(1,10000000):
    paliCount = 0
    listofpali =[]
    for e in range(2,17):
        temp = baseConverter(e,gi)
        if (isPalindrome(str(temp))):
            listofpali.append((e,temp))
            paliCount += 1
        if(paliCount == 3):
            break
    if (paliCount >= 3):
        #print(gi, listofpali)
        paliSum += gi

print("-----")
print(paliSum - 29137)       
print(paliSum)

