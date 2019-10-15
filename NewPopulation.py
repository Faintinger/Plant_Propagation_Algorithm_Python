import random
import f
from operations import sum as sum
from operations import res as res
from operations import mult as mult


def newPopulation(x0, a, b, npop):
    nx = len(x0);
    nf = 0;
    ninf = 0;
    pop = [];
    n = 0;
    ntries = 0;
    x = x0;	
    while ((n<npop) & ((ntries+1) < 3*npop)):
        vctr = x[:]
        try:
            nf=nf+1;
            y = f.eval(x);
            ny = len(y);
            for i in range(ny):
                vctr.append(y[i])
            pop.append(vctr)
            n=n+1
        except Exception as e:
            ninf=ninf+1
            #print(e)
        r = [] 
        for i in range(nx):
            r.append(random.uniform(0,1));
        x = sum(mult(r,res(b,a)), a)
        #print("n: " + str(n) + " ninf: " + str(ninf) + " x: " + str(x))

    return [pop, nx, ny, nf, ninf]
