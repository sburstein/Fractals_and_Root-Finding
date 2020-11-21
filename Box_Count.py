from PIL import Image
#import pylab as pl

#image_name = "newton-fractal-plot-func.jpg"

def box_count(image_name, box_size = 2, print_out=True):

  #image = pl.imread(image_name)
  image = Image.open(image_name)
  pix = image.load()


  #pixList = []
  #pixCount = 0
  monoColCount = 0
  multiColCount = 0

  ncols = image.size[0]
  nrows = image.size[1]

  for i in range(nrows//box_size):
    for j in range (ncols//box_size):
      pix1 = pix[i*box_size, j*box_size]
      pix2 = pix[i*box_size + 1, j*box_size]
      pix3 = pix[i*box_size, j*box_size + 1]
      pix4 = pix[i*box_size + 1, j*box_size + 1]
    #need to create additional checks if box_size > 2

      if pix1 == pix2 == pix3 == pix4:
        monoColCount += 1
      else:
        multiColCount += 1

  if print_out == True:
    print("The image " + image_name + " has pixel dimensions = " + str(image.size))
    print("Box Size = " + str(box_size))
    print("Total # Boxes Counted = " + str(int((nrows/box_size) * (ncols/box_size))))
    print("# Boxes w/ 4 equal pixels (r,g,b) = " + str(monoColCount))
    print("# Boxes w/o 4 equal pixels (r,g,b) = " + str(multiColCount))

  return (monoColCount / (monoColCount + multiColCount))