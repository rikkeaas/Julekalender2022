import math
f = open('julebrusmaskiner.txt', 'r')

machines = {}
#temperatur er mellom 95 og 105, vann er mellom 400 og 1500 og kullsyre er mellom 300 og 500.
for l in f.readlines():
    m,tt,tv,tk = l.split(',')
    t = int(tt.split()[1][:-1])
    v = int(tv.split()[1][:-1])
    k =int(tk.split()[1][:-1])
    if (t < 95 or t > 105 or v < 400 or v > 1500 or k < 300 or k > 500):
        continue

    s = v - 100 + math.floor(k / 10)
    if (t >= 100):
        s -= math.floor(s/40)
    # * Vann slik at maskinen kun har 100L vann igjen 
    # * Kullsyre tilsvarende en tiendedel av antall liter kullsyre 
    # * Hvis temperatur er 100 grader eller over, så må du trekke fra en førtidel til slutt, fordi litt brus fordamper. 
    # Regnestykket er ikke perfekt, så vi runder ned for å kompensere.
    try:
        machines[m] = machines[m] + s
    except:
        machines[m] = s        

liters = 0
maxL = 0
maxM = ""
for m,s in machines.items():
    liters += s
    if s > maxL:
        maxM = m
        maxL = s

print(maxM)
print(liters)