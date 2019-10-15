import random as random
import NewPopulation
import PlantSort
import PlantFitness
import PlantSort
import f
from math import ceil
from operations import sum
from operations import res
from operations import mult
from operations import getColumn

# x0 list [x,y] starting point
# a list [x,y] lower bound
# b list [x,y] upper bound
# ngen number of elements to generate
# nrmax max number of elements
# output bool display or not

def plantPopulation(x0, a, b, ngen, npop, nrmax, output):

	plPop = NewPopulation.newPopulation(x0, a, b, npop)
	phi = plPop[0]
	nx = plPop[1]
	ny = plPop[2]
	nf = plPop[3]
	ninf = plPop[4]
	#print(plPop)
	pop = PlantSort.plantSort(phi, nx, ny)
	#print(pop)
	
	gen = 0
	x = []
	y = []
	while gen < ngen:
		N = PlantFitness.computeFitness(pop, nx, ny, npop)
		N = N[0]
		phi = []
		for i in range(npop):
			phi.append(pop[i])
			# print(N[p])
			nr = ceil(nrmax*(1-N[i])*random.random()) 
			if nr < 1:
				nr = 1
			for j in  range(nr):
				dx = []
				for n in range(nx):
					dx.append(random.random() * nx)
				dx=mult(res(dx,0.5),(2*(1-N[i])))
				x = []
				for k in range(nx):
					x.append(pop[i][k])
				x=sum(x,dx)
				#print("x:"); print(x);
				# reset boundaries
				x = resetBoundaries(x, a, True, b)
				#print("xa:"); print(x);
				x = resetBoundaries(x, b, False, b)
				#print("xb:"); print(x);
				nf = 0
				try:
					nf = nf + 1
					y = f.eval(x)
					for k in range(len(y)):
					 	x.append(y[k])
					phi.append(x)
				except Exception as e:
					ninf = ninf + 1
		pop = PlantSort.plantSort(phi,nx,ny)
		gen = gen + 1

	x = []
	y = []
	#print(pop);
	#stop = input("prompt: ")
	for c in range(len(pop)):
		tX = []
		tY = []
		for i in range(nx):
			tX.append(pop[c][i])
		for j in range(len(pop[0]) - nx):
			tY.append(pop[c][j + (nx)])
		x.append(tX);
		y.append(tY);
		
	return [x ,y, nf, ninf]

def resetBoundaries(mat, boundaries, greater, default):
    resp = []
    l = len(mat)
    if(isinstance(mat[0],list)):
        for i in range(l):
            inside = True
            for j in range(len(boundaries)):
                if(greater):
                    if(boundaries[j] < mat[i][j]):
                        mat[i][j] = default[j];
                else:
                    if(boundaries[j] > mat[i][j]):
                        mat[i][j] = default[j];
    else:
        for j in range(len(boundaries)):
            if(greater):
                if(boundaries[j] < mat[j]):
                    mat[j] = default[j];
            else:
                if(boundaries[j] > mat[j]):
                    mat[j] = default[j];

    return mat;