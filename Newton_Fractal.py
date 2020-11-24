import matplotlib.pyplot as plt
import numpy as np
import datetime
from main import func

''''
source: https://computingskillset.com/solving-equations/newton-fractals-explained-examples-and-python-code/
'''

def plot_newton_fractal(func_string, func_roots, interval_size=2.1, timing=False, prec_goal=1.e-11, nmax=500, num_x=1000,
num_y=1000, colour_name='Greys'):
  if timing == True:
    print('Started computation at '+str(datetime.datetime.now()))
  #check if input is correct
  if type(func_roots) == list:
    rootlist = {}
    rootlist[func_string] = func_roots
  else:
    return ValueError("func_root must be of type(list)")
  # define x and y grids of points for computation and plotting the fractal
  bounds = interval_size
  xvals = np.linspace(-bounds, bounds, num = num_x)
  yvals = np.linspace(-bounds, bounds, num = num_y)
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

    # uncomment those in case of doubt
#    print(result_list)
#    print(counter)
#    print(nroot)
    
    # get the data into the proper shape for plotting with matplotlib.pyplot.matshow
  nroot_contour = np.transpose(np.reshape(nroot,(num_x,num_y)))
    
    # timing to see difference in time used between calculation and plotting
  if timing == True:
      print('Finished computation at '+str(datetime.datetime.now()))
    # create an imshow plot 
  fig = plt.figure(frameon=False)
  ax = fig.add_subplot(1,1,1)
  plt.axis('off')
    #label the axes
  #plt.xlabel("$Re(z)$", fontsize=16)
  #plt.ylabel("$Im(z)$", fontsize=16)
    # plots the matrix of data in the current figure. 
  plt.matshow(nroot_contour, fignum=0, interpolation='none', cmap=colour_name)
    #, origin='lower',
    # remove ticks and tick labels from the figure
  plt.tight_layout()
    # save a file of plot.
  plt.savefig('newton-fractal-plot-'+func_string+'.jpg', dpi=200,bbox_inches='tight', pad_inches=0, transparent=True)
        
  plt.close()

    # timing step
  if timing == True:
      print('Finished computation and plotting at '+str(datetime.datetime.now()))
