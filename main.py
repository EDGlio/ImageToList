# Import the necessary libraries
from PIL import Image
from numpy import asarray
  

# load the image and convert into 
# numpy array
img = Image.open('insert file here.png')
numpydata = asarray(img)
  
# data
data = []
for i in numpydata:
  for j in i:
    data.append(j[1]/255)
print(data)
