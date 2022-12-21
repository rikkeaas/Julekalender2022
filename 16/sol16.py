
import math
import time

rmax = 1000000
alpha = 0.2
gamma = 0.000075
lam = 83
beta = 0.1

def reinStep(prevRein, prevUlv):
    temp = (alpha*prevRein*(rmax - prevRein)) / rmax
    temp2 = gamma*prevUlv*prevRein
    return int(prevRein + (alpha*prevRein*(rmax - prevRein)) / rmax - gamma*prevUlv*prevRein)

def ulvStep(prevRein, prevUlv):
    temp = (gamma * prevUlv * prevRein) / lam
    temp2 = beta*prevUlv
    return int(prevUlv + (gamma * prevUlv * prevRein) / lam - beta*prevUlv)


r = 125000
u = 3500

rs = [125000]
us = [3500]
e = 1




start = time.time()



for i in range(10000000):
    tr = int(r + (0.2*r*(1000000 - r)) / 1000000 - 0.000075*u*r)
    u = int(u + (0.000075 * u * r) / 83 - 0.1*u)
    r = tr
    #if ((i+1) == pow(10,e)):
    #    rs.append(r)
    #    us.append(u)
    #    e += 1
    #    print(e)

end = time.time()
print(((end - start)*100000)/(60*60*24))