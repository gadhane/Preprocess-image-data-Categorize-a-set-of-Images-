import pandas as pd
import glob
import shutil
import os

# Set the Directoreis
imagepath = 'images/' #Path to the unclassified images

#Path to the lebeled directories
dogPath = "data/dog/"
catPath = "data/cat/"
personPath = "data/person/"
horsePath = "data/horse/"
elephantPath = "data/elephant/"
tigerPath = "data/tiger/"


# Read the CSV file to Dataframe
df2 = pd.read_csv('imgRef.txt') # read txt file and store it in a dataframe
my_columns = df2[["imglebel"]]

imglebel = df2["imglebel"]

# Append the file names in a folder to list and sort them out.
files = []

for r, d, f in os.walk(imagepath):
	for file in f:
		files.append(os.path.join(r, file))
files.sort()

# Traverse through each file and copy to each folder based on CSV file 
# Description.
i = 0
for file in files:
  if imglebel[i] == "dog":
    shutil.copy(file, dogPath, follow_symlinks=True)
  elif imglebel[i] == "cat":
    shutil.copy(file, catPath, follow_symlinks=True)
  elif imglebel[i] == "person":
    shutil.copy(file, person, follow_symlinks=True)
  elif imglebel[i] == "horse":
    shutil.copy(file, horsePath, follow_symlinks=True)
  elif imglebel[i] == "elephant":
    shutil.copy(file, elephantPath, follow_symlinks=True)
  elif imglebel[i] == "tiger":
    shutil.copy(file, tigerPath, follow_symlinks=True)
  i += 1
print("Task Completed")
