from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import datetime

"""
Module containing functions used to calculate the fractal dimension of a given jpeg image.
"""

def box_count(image_matrix, nrows, ncols, box_size, print_out=False):
  """
  Counts the number of boxes in image matrix that contain fractal

  Assumes the image is in greyscale, no background, with little to no compression issues.
  Takes a box size input and returns the number of boxes of size n that cover the fractal.

  Parameters
  ----------
  image_matrix : np.array
      numpy array of pixel values, with row-major in [row][column]
  nrows : int
      number of rows in the image matrix
  ncols : int
      number of columns in the image_matrix
  box_size : int
      box length in pixels
  print_out : boolean, optional
      True for printout of information regarding boxes counted 
  
  Returns
  -------
  Number of Boxes of (box_size x box_size) that contain the fractal
  """

  pix = image_matrix

  fractalCounter = 0
  for r in range(nrows//box_size):
    for s in range (ncols//box_size):
      oneColorBoxCounter = 0
      topLeftPix = pix[box_size*r, box_size*s]
      for j in range(box_size):
        for k in range(box_size):
          indivPix = pix[box_size*r + j, box_size*s + k]          
          if indivPix == topLeftPix: 
            oneColorBoxCounter += 1
      if oneColorBoxCounter < box_size**2:
        fractalCounter += 1

  if print_out == True:
    print("Box Size = " + str(box_size))
    print("Total # Boxes Counted = " + str(int((nrows/box_size) * (ncols/box_size))))
    print("# Boxes w/ fractal = " + str(fractalCounter))
    print("# Boxes w/o fractal = " + str(int( (nrows/box_size) * (ncols/box_size) - fractalCounter )))
  
  return fractalCounter

def Box_Dim(image_name, start_range = 1,end_range = 10, debug=False, graph=False, timing=False):
  """
  Calculates the dimension of a fractal using Minkowski–Bouligand dimension or box-counting dimension analysis. 
  Assumes the image is greyscale colour square with length 2**k .

  Parameters
  ----------
  image_name : str
      input of image file name in str
  start_range : int, optional
      default is 1, start range for 2**k data points
  end_range : int, optional
      default is 10, end range for 2**k data points
  debug : boolean, optional
     toggles several print statements
  graph : boolean, optional
     graphs the Number of Boxes vs. Box Size if toggled
     asks for predicted dimension from user
     returns guess and calculated dimension if toggled
  timing : boolean, optional
      toggles timing of the computation and prints the total time for the function.
  Returns
  ----------
  slope : float
     the slope of the linear regression model, which is the dimension of the fractal
  guess : float
      returns if graph=True. The user's guess for the dimension of the fractal.
  """

  if timing == True:
    start = datetime.datetime.now()

  im_mat, nrows, ncols = image_convert(image_name)

  n = [2**k for k in range(start_range, end_range)] 
  if debug == True:
    print(f"data points n : {n}")
  
  # computes a list of box counts given sizes in v
  # n is the range of box_sizes, goes up by powers of 2
  box_number = [box_count(im_mat, nrows, ncols, v) for v in n]
  x = np.array(n)
  y = np.array(box_number)
  
  slope, intercept, r_value, p_value, std_err = linregress(np.log10(1/x), np.log10(y))
  
  if debug == True:
    print(f"Linear regression (numpy) variables: {slope}, intercept:{intercept}, r_value:{r_value}, p_value:{p_value}, std_err:{std_err}")

  if graph == True:
    # plot the graph (log-log)
    xfid = np.linspace(-3, 0)
    plt.figure(figsize=(6, 4))
    plt.plot(np.log10(1/x), np.log10(y), '.-k', markersize=12)
    
    #pred_y = slope * x + intercept 
    plt.plot(xfid, xfid*slope+intercept, color = 'green')
    plt.show
    
    # plot a reference line
    res = input("Plot a reference line? (y/n) ")
    
    if res == ("y"):
      guess = input("What is the predicted slope (dimension)? ")
      pred_dim = float(guess) * -1.
      vals = [100*v**(float(pred_dim)) for v in n]
      plt.plot(np.log10(1/x), np.log10(vals), '--r')
      
      # plot decorations, save plot
      plt.title('Box Count vs. Box Size Plot')
      plt.xlabel('$n$')
      plt.ylabel('Box_count')
      plt.savefig('number_vs_count.pdf', bbox_inches='tight')
      plt.show()

      if timing == True:
        end = datetime.datetime.now()
        print('Finished computation at '+str(end))
        elapsed = end - start
        print("Total elapsed time:" +str(elapsed))

      return guess, slope
    
    else:
      # plot decorations, save plot
      plt.xlabel('$n$')
      plt.ylabel('Box_count')
      plt.savefig('number_vs_count.pdf', bbox_inches='tight')
      plt.show()

      if timing == True:
        end = datetime.datetime.now()
        print('Finished computation at '+str(end))
        elapsed = end - start
        print("Total elapsed time:" +str(elapsed))

      return slope
  
  if timing == True:
      end = datetime.datetime.now()
      print('Finished computation at '+str(end))
      elapsed = end - start
      print("Total elapsed time:" +str(elapsed))
  return slope


def image_convert(image_name):
  """
  Converts image to usable matrix 

  Parameters
  ----------
  image_name : string
      file name of image. Must be jpg format.
      
  Returns
  -------
  im_mat : np.array
      numpy array of pixel values, with row-major in [row][column]
  nrows : int
      number of rows in the image matrix
  ncols : int
      number of columns in the image_matrix
  """
  
  image = Image.open(image_name)
  pix = image.load()

  nrows = image.size[1]
  ncols = image.size[0]

  temp = [[[0] for x in range(nrows)] for y in range(ncols)]

  px = [[[0] for x in range(nrows)] for y in range(ncols)]
  for x in range(nrows):
    for y in range(ncols):
      temp[x][y] = pix[x, y]
      px[x][y] = temp[x][y][0]
  
  im_mat = np.array(px)
  
  return im_mat, nrows, ncols
    