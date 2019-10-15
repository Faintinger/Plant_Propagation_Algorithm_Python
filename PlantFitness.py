from operations import sum
from operations import res
from operations import mult
from operations import div
from operations import getColumn

def computeFitness(pop, nx, ny, npop):
	i = len(pop)
	j = len(pop[0])
	fit = 0
	if npop < i:
		i = npop
	if ny == 1:
		if j - nx == 1:
			ymin = pop[0][nx]
			ymax = pop[npop - 1][nx]
			if abs(ymax - ymin) > 0.0001:
				a = getColumn(pop, nx)
				fit = div(res(mult(a,-1),-ymax), (ymax - ymin))
			else:
				fit = []
				for l in range(i):
					fit.append(0.5)
			return [fit, pop]
		else:
			print('Number of objective functions doesn"t seem to match')
	else:
		error ('Multi-objective optimisation not supported yet.')
