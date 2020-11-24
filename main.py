import Newton_Fractal
from Newton_Fractal import *
import Box_Count
from Box_Count import *

def func(x):
    return (x**2-1)*(x**2+1)/(2*x*(x**2-1)+2*x*(x**2+1))
    
if __name__ == "__main__":

  #plot_newton_fractal('func',[-1, 1, -1j, 1j], timing=True)
  # final timing check
  #print('Finished computation and plotting at '+str(datetime.datetime.now()))

  image_name = "newton-fractal-plot-func.jpg"
  square_test = "square2.jpg"
  #x = box_count(square_test, box_size = 2, print_out = True)

  #print(x)

  jo, c, b = image_convert(square_test)
  print(jo)

  box_count(jo, c, b, 3, print_out=True)
  
  dim, guess = Box_Dim(square_test, graph=True)
  print(dim)


