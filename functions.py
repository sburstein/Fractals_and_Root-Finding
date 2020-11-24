import numpy as np

# initialize a dictionary of list of the roots
rootlist = {}
# function definitions to evaluate f/f' at x. Add your own as needed.
# each function definition must include a list of the roots of this function
# root list can be in any order and restricted to finite number
# example 1: polynomial function with four roots
def npe1(x):
    return (x**2-1)*(x**2+1)/(2*x*(x**2-1)+2*x*(x**2+1))
rootlist['npe1'] = [-1, 1, -1j, 1j]
# example 2: function with three roots on the unit circle
def npe2(x):
    return (x**3-1)/(3*x**2)
rootlist['npe2'] = [-.5-0.8660254037844386j,-.5+0.8660254037844386j, 1]
# example 3: function with twelve roots on the unit circle
def npe3(x):
    return (x**12-1)/(12*x**11)
rootlist['npe3'] = [-.5-0.8660254037844386j,-.5+0.8660254037844386j,.5-0.8660254037844386j,.5+0.8660254037844386j,-.5j-0.8660254037844386,-.5j+0.8660254037844386,.5j-0.8660254037844386,.5j+0.8660254037844386, 1,-1,1.j,-1.j]
# example 7: function with four roots, all real
def npe7(x):
    return (x+2.)*(x+1.5)*(x-0.5)*(x-2.)/((x+1.5)*(x-0.5)*(x-2.) + (x+2.)*(x-0.5)*(x-2.) +(x+2.)*(x+1.5)*(x-2.) + (x+2.)*(x+1.5)*(x-0.5)) 
rootlist['npe7'] = [-2, -1.5, 0.5, 2]
# example 9: function with four roots, one multiple
def npe9(x):
    return (x+2)*(x+1.5)**2*(x-0.5)*(x-2)/((x+1.5)**2*(x-0.5)*(x-2) + 2*(x+2)*(x+1.5)*(x-0.5)*(x-2) +(x+2)*(x+1.5)**2*(x-2) + (x+2)*(x+1.5)**2*(x-0.5) )
rootlist['npe9'] = [-2, -1.5, 0.5, 2]
# example 10: sine function
def npe10(x):
    return np.tan(x)
rootlist['npe10'] = [0]
for i in range(1,10):
    rootlist['npe10'].extend([i*np.pi,-i*np.pi])