# Import the necessary libraries
from PIL import Image
from numpy import asarray
import os

directory = 'squares'
images = os.listdir(directory+'/')
print(images)

newdir = os.mkdir('list'+directory+'/')

# load the image and convert into 
# numpy array
for nom in images:
  img = Image.open(f'{directory}/{nom}')
  numpydata = asarray(img)

  completeName = os.path.join(f'list{directory}', nom)
  # data
  data = []
  for i in numpydata:
    for j in i:
      data.append(j[1]/255)
  with open(f'{completeName[:-4]}.txt', 'w') as file:
    file.write(str(data))
