from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

#image_name = "newton-fractal-plot-func.jpg"

def box_count(image_matrix, nrows, ncols, box_size, print_out=False):
  """
  Assumes the image is in greyscale, no background, with little to no compression issues.
  Takes a box size input and returns the number of boxes of size n that cover the fractal.
  Return:
  Number of Boxes of Size N that contain the fractal
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

def Box_Dim(image_name, start_range = 1, end_range = 10, debug=False, graph=False):
  """
  Arguments:
  image_name = input of image file in str
  debug = toggles several print statements
  graph = graphs the Number of Boxes vs. Box Size if toggled
  
  Returns:
  modline.coef_ = the slope of the linear regression model, which is the dimension of the fractal
  """
  im_mat, nrows, ncols = image_convert(image_name)
  # TODO:
  # calculate the maximim box_size for image
  # calculate a good step size for the range
  n = [2**k for k in range(start_range, end_range)] 
  # computes a list of box counts given sizes in v
  # dummy variable n is the range of box_sizes, goes up by powers of 2
  box_number = [box_count(im_mat, nrows, ncols, v) for v in n]
  x = np.array(n)
  y = np.array(box_number)
  
  #modline = np.polyfit(np.log10(x), np.log10(y), 1)
  slope, intercept, r_value, p_value, std_err = linregress(np.log10(1/x), np.log10(y))
  #calc_dim = slope * -1.
  

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
      return guess, slope
    else:
      # plot decorations, save plot
      plt.xlabel('$n$')
      plt.ylabel('Box_count')
      plt.savefig('number_vs_count.pdf', bbox_inches='tight')
      plt.show()

      return slope
  return slope


def image_convert(image_name):
  image = Image.open(image_name)
  pix = image.load()

  nrows = image.size[1]
  ncols = image.size[0]

  temp = [[[0] for x in range(nrows)] for y in range(ncols)]
  #temp = np.zeros(nrows, ncols)
  px = [[[0] for x in range(nrows)] for y in range(ncols)]
  for x in range(nrows):
    for y in range(ncols):
      temp[x][y] = pix[x, y]
      px[x][y] = temp[x][y][0]
  
  im_mat = np.array(px)
  
  return im_mat, nrows, ncols
    