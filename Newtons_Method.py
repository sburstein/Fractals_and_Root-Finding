from scipy.misc import derivative
#from sympy import diff

def NewtonsMethod(f, initial, tolerance = 1e-10, max_iterations = 100, debug = False):
    
    it = 0
    x0 = initial

    while True:
        x1 = x0 - f(x0) / derivative(f, x0)
        difference = abs(x1 - x0)
        if (difference < tolerance) or it >= max_iterations:
            break
        it += 1
        x0 = x1
    return x0

def f(x):
    return x**2 + 1

initial = -2
approx_root = NewtonsMethod(f, initial)

print('x: ', initial)
print('approx root: ', approx_root)
print("f(approx root) = ", (f(approx_root)))