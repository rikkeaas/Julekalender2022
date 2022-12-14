import matplotlib.pyplot as plot

f = open("encrypted.txt", 'r')
xs = []
ys = []

for i,l in enumerate(f.readlines()):
    for j,n in enumerate(l.split()):
        bs = bin(int(n))
        ones = list(filter(lambda x: (x == '1'), bs))

        if (len(ones)%2 == 0):
            ys.append(i)
            xs.append(j)

plot.scatter(xs, ys)
plot.show()