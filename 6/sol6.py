
f = open('slemmehandlinger.txt', 'r')
ls = f.readlines()

d = {}
for l in ls:
    temp = l.split(':')
    d[temp[0]] = float(temp[1])

f2 = open('stemmer.txt', 'r')
ls2 = f2.readlines()

stemmer = {"julenissen":0, "alvekongen":0, "sneglulf":0}

def getWeight(h):
    try:
        return d[h]
    except:
        return 1.0

for l in ls2:
    h,v = l.strip().split(':')
    hs = h.split(',')
    minW = 1.0
    for hh in hs:
        w = getWeight(hh)
        if w < minW:
            minW = w
    stemmer[v] = stemmer[v] + minW

print(stemmer)
