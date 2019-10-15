#F Script
from math import exp
from math import cos
from math import sin
from math import pi
from math import sqrt
#Script that contains the function defined and return its evaluation

def eval(x):
    #return [-20.*exp(-0.2*sqrt(0.5*(x[0]**2+x[1]**2)))-exp(0.5*(cos(2*pi*x[0])+cos(2*pi*x[1])))];
    return [100*(((x[0]**2)-x[1])**2)+((x[0]-1)**2)];