import matplotlib.pyplot as plt
import numpy as np
import datetime
from functions import *

''''
Module that produces a Newton Fractal image in jpg if given the function and a list of roots.

modified code from source: https://computingskillset.com/solving-equations/newton-fractals-explained-examples-and-python-code/
'''

def plot_newton_fractal(func_string, func_roots, interval_size=2.56, timing=False, prec_goal=1.e-11, nmax=500, num_x=1000, num_y=1000, scalar=1, colour_name='Greys'):
  """
  Produces a Newton Fractal image in jpg format if given the function(x) as string and a list of roots.

  Parameters
  ----------
  func_string : str
      input for name of function
  func_roots : list
      list of roots associated with function 
  interval_size : float, optional
      Scalar which determines number of pixels in image. Image output is a square. The default is 2.56.
  timing : boolean, optional
      Prints the start and end to the computation. The default is False.
  prec_goal : float, optional
      The precision goal for the root-finding algorithm. The default is 1.e-11.
  nmax : int, optional
      The maximim number of iterations. The default is 500.
  num_x : int, optional
      Number of points in x-interval. The default is 1000.
  num_y : int, optional
      Number of points in y-interval. The default is 1000.
  scalar : int, optional
      Scalar value which multiplies dpi and num_x, num_y. Increasing this value will increase the dpi and thus the detail. The default is 1.
  colour_name : str, optional
      The colour map of the fractal image. The default is 'Greys'.

  Returns
  -------
  None.
  """
  
  if timing == True:
    start = datetime.datetime.now()
    print('Started computation at '+str(start))
    
  #check if input is correct
  if type(func_roots) == list:
    rootlist = {}
    rootlist[func_string] = func_roots
  else:
    return ValueError("func_root must be of type(list)")
  
  # define x and y grids of points for computation and plotting the fractal
  bounds = interval_size
  xvals = np.linspace(-bounds, bounds, num = num_x*scalar)
  yvals = np.linspace(-bounds, bounds, num = num_y*scalar)
  
  # define a function that can id a root from the rootlist
  def id_root(zl,rlist):
      findgoal = (prec_goal*1.e-1) * np.ones(len(zl))
      rootid = -1 * np.ones(len(zl))
      for r in rlist:
          # check for closeness to each root in the list
          rootid = np.where(np.abs(zl-r* np.ones(len(zl))) < findgoal, np.ones(len(zl)) * rlist.index(r), rootid)      
      return rootid.astype(int)
      
  # create complex list of points from x and y values
  zlist = [(x + 1j*y) for y in yvals for x in xvals]
    
  # initialize the arrays for results, differences, loop counters  
  result_list = np.array(zlist)
  reldiff = np.ones(len(result_list))
  counter = np.zeros(len(result_list), dtype=int)
  
  # initialize overall counter for controlling the while loop
  overallcounter = 0
  
  # vectorize the precision goal
  prec_goal_list = np.ones(len(result_list)) * prec_goal
  
  # iterate while precision goal is not met - vectorized
  while np.any(reldiff) > prec_goal and overallcounter < nmax:    
    
    # call function as defined above and 
    # compute iteration step, new x_i, and relative difference
        diff = eval(func_string+'(result_list)')
        z1list = result_list - diff
        reldiff = np.abs(diff/result_list)
        
        # reset the iteration
        result_list = z1list
        
        # increase the vectorized counter at each point, or not (if converged)
        counter = counter + np.greater(reldiff, prec_goal_list )
        # increase the control counter
        overallcounter += 1
    
  # get the converged roots matched up with those predefined in the root list
  nroot = id_root(z1list,rootlist[func_string])
  nroot_contour = np.transpose(np.reshape(nroot,(num_x*scalar, num_y*scalar)))
    
  # timing to see difference in time used between calculation and plotting
  if timing == True:
      print('Finished computation at '+str(datetime.datetime.now()))
  
  # create plot 
  fig = plt.figure(frameon=False)
  ax = fig.add_subplot(1,1,1)
  plt.axis('off')

  plt.matshow(nroot_contour, fignum=0, interpolation='none', cmap=colour_name)

  plt.tight_layout()
  
  # save a file of plot.
  plt.savefig('newton-fractal-plot-'+func_string+'.jpg', dpi=200*scalar,bbox_inches='tight', pad_inches=0, transparent=True)
        
  plt.close()

  # timing step
  if timing == True:
      end = datetime.datetime.now()
      print('Finished computation and plotting at '+str(end))
      elapsed = end - start
      print("Total elapsed time:" +str(elapsed))
