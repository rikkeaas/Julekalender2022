
def baseConverter(bTo, n):
    newNumb = ""
    while n > 0:
        n, r = divmod(n, bTo) 
        newNumb = str(r) + newNumb

    return newNumb

def isPalindrome(s):
    return s == s[::-1]

paliSum = 0


for gi in range(0,1000):
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
        print(gi, listofpali)
        paliSum += gi

print("-----")
print(paliSum - 29137)       
print(paliSum)

