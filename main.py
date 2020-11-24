import Newton_Fractal
from Newton_Fractal import *
import Box_Count
from Box_Count import *
from functions import *
    
if __name__ == "__main__":

  #plot_newton_fractal('func',[-1, 1, -1j, 1j], scalar=2, interval_size=2.56, timing=True)
  #final timing check
  #print('Finished computation and plotting at '+str(datetime.datetime.now()))

  
  for i in [2,7,9,10]:
    func_name = "npe"+str(i)   #"npe1"
    func_roots = rootlist[func_name]
    plot_newton_fractal(func_name, func_roots, scalar=2, interval_size=2.56, timing=True)


  #image_name = f"newton-fractal-plot-{func_name}.jpg"
  #square_test = "square.jpg"
  #x = box_count(square_test, box_size = 2, print_out = True)

  #print(x)

  

  #box_count(jo, c, b, 3, print_out=True)
  
  #dim = Box_Dim(image_name, graph=True)
  #print(dim)


