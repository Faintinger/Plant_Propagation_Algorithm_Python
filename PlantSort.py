from operations import sum
from operations import res
from operations import mult

def plantSort(pop, nx, ny):
	m = len(pop)
	n = len(pop[0])
	if ny == 1:
		if n - nx == 1:
			#Sort in Y axis
			lis = []
			lis.append(pop[0])
			for i in range(1,m):
				for j in range(len(lis)):
					if pop[i][nx] < lis[j][nx]:
						lis.insert(j,pop[i])
						break
					else:
						if j == (len(lis) - 1):
							lis.append(pop[i])
			return lis
		else:
			error ('Number of objective functions doesn"t seem to match.')
	else:
		error ('Multi-objective optimisation not supported yet.')
