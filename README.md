# Preprocess-image-data-Categorize-a-set-of-Images-
Categorize a set of images in to their corresponding labels. 

Given a set of images in a folder and their lebel in a text or CSV file (image name and the coressponding lebel). Assuming that there are multiple lebelles, we wanted to copy the image data to each folder based on the lebel of the corrosponding images in the text file and later we wanted to use it for supervised training. This simple python script will automatically copy the images to the correcponding directores.

N.B. we have to create empty folders equal to the number of lebels we wanted to process, and set the directory based on our system and folder location. (or) If you want you can modify the program to check if there is no folder by that name then to automatically create 
the folder.

Lests assume that we have tens of thousand of images of cat, dog, person, horse, elephant, and tiger in one folder. And lets assume there is a CSV/Text file which contains the file name of each image and corresponding lebel. (i.e. if the image is cat, dog, or person....) as follows:

<pre>
<b>filename 		imglebel</b>
00001.png 		tiger
00002.png 		person
00003.png	  	elephant
.......	  		.......
.......	  		.......
....... 			.......
12400.png 		horse
</pre>

This program will first open the CSV file, and put the lebels we wanted in a data frame, and then it will copy the coressponding image into the exact folder. (if the lebel is dog, it will copy to dog folde; if Cat to cat folder and so on)
