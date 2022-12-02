df = open('dictionary.txt', 'r')
ds = df.readlines()
sDict = {}

for l in ds:
    temp = l.split(',')
    sDict[temp[0].strip()] = temp[1].strip()

def isInDict(word):
    try:
        return sDict[word]
    except:
        return ""

lf = open('letter.txt', 'r')
ls = lf.readline()

def recursion(startPos, translation):
    if (startPos >= len(ls)-1):  
        return translation

    temps = ""

    for i in range(startPos, len(ls)):
        temps += ls[i]
        if (isInDict(temps) != ""):
            rest = recursion(i+1, translation + " " + isInDict(temps))
            if (rest != ""):
                return rest

    return ""

es = recursion(0, "")
print(len(es[1:]))
