#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Listing images that ends with .png

import os
from os import listdir
 
# get the path/directory
folder_dir = "D:/images"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".png")):
        print(images)


# In[5]:


#Listing all the images from the directory
import os
from os import listdir

# get the path or directory
folder_dir = "D:/images"
for images in os.listdir(folder_dir):
	print(images)


# In[45]:


#Display all the images from the directory
import cv2 
import os 
import glob 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
 
#Set the path where images are stored 
img_dir = "D:/images" # Enter Directory of all images  
data_path = os.path.join(img_dir,'*g') 
files = glob.glob(data_path) 
data = [] 
for f1 in files: 
    img = plt.imread(f1) 
    data.append(img) 
    plt.figure() 
    plt.imshow(img) 
for f1 in files: 
    img = plt.imread(f1) 
    data.append(img) 
    resize=cv2.resize(img,(500,500))
    plt.figure() 
    plt.imshow(resize)


# In[ ]:




