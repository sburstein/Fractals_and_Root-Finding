import Newton_Fractal
from Newton_Fractal import *
import Box_Count
from Box_Count import *
from functions import *
    
if __name__ == "__main__":

  '''
  Mathematical foundation for box counting method as it pertains to image size:
    
    The image should have (n x m) dimensions such that n = m. 
    Image should also be compressed as a .jpg

    f(x) = log2(2.56 * 200 * x)
    2^(f(a)) = n in (n x n) dimension size in pixel count

    Usable scalar values for box counting method:
    a=1 -> 512 x 512 pixel image [Poor quality fractal image, not enough pixels]
    a=2 -> 1024 x 1024 pixel image [Ideal for most Newton fractals, approx. 8 min runtime]
    a=4 -> 2048 x 2048 pixel image [Most precise, approx. 24 min runtime]
  '''

  #-----------------------------------------------------------------------
  '''
  Plot newton fractal for npe2: (x**3-1)/(3*x**2) which has 3 roots on the unit circle
  roots = [-.5-0.8660254037844386j,-.5+0.8660254037844386j, 1]
  scalar = 2
  '''

  #func_name = "npe2"
  #func_roots = rootlist[func_name]
  #plot_newton_fractal(func_name, func_roots, scalar=2, interval_size=2.56, timing=True)
  #final timing check
  #print('Finished computation and plotting at '+str(datetime.datetime.now()))

  #-----------------------------------------------------------------------

  #-----------------------------------------------------------------------
  '''
  Example of Box Counting method and subsequent dimension calculation for an 
  1024 x 1024 pixel image of a square.
  for box size of 2x2 pixels, Calculated Dimension = 1.023804290783397
  The real value is 1 for this box counting method, since only pixels on the 
  border of the square are calculated, which is concurrent with the dimension of 
  a straight line, which has an actual dimension = 1.
  Error = |1 - 1.0238| = 0.0238
  '''

  #square_test = "square3.jpg"
  #guess, actual = Box_Dim(square_test, graph=True, timing=True, debug=True)
  #print(f"Predicted Dimension: {guess} \n Calculated Dimension: {actual}")
  
  #-----------------------------------------------------------------------
  
  #-----------------------------------------------------------------------
  '''
  Dimension Calculation and Log-Log plot for a Sierpinski Carpet.
  Given the size of this image (2048 x 2048 pixels)
  Calculated Dimension: 1.9313677056499783
  The actual Hausdorff dimension of the carpet is log(8)/log(3) ≈ 1.8928
  Error = |1.8928 - 1.9314| = 0.0386
  '''

  #sierpinski_carpet = "Sierpinski_carpet.jpg"
  #guess, actual = Box_Dim(sierpinski_carpet, graph=True)
  #print(f"Predicted Dimension: {guess} \n Calculated Dimension: {actual}")

  #-----------------------------------------------------------------------

  #-----------------------------------------------------------------------
  '''
  Dimension Calculation for npe1: (x**2-1)*(x**2+1)/(2*x*(x**2-1)+2*x*(x**2+1))
  roots = [-1, 1, -1j, 1j]
  scalar = 4
  Fractal dimension determined from slope of linear regression with 10 data points.
  Calculated Dimension: 1.6559432188212682
  '''

  #func_name = 'npe1'
  #image_name = f"newton-fractal-plot-{func_name}.jpg"
  #actual = Box_Dim(image_name, graph=False, end_range=11)
  #print(f"Calculated Dimension: {actual}")

  #-----------------------------------------------------------------------