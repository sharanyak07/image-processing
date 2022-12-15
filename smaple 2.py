#!/usr/bin/env python
# coding: utf-8

# In[5]:


#BITWISE OPERATORS
import cv2 as cv

img1 = cv.imread('im1.jpg')
img2 = cv.imread('im2.jpg')
bitwise_AND = cv.bitwise_and(img1, img2)
bitwise_OR = cv.bitwise_or(img1, img2)
bitwise_NOT = cv.bitwise_not(img1)
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('AND',bitwise_AND)
cv.imshow('OR',bitwise_OR)
cv.imshow('NOT',bitwise_NOT)
cv.waitKey(0)  
cv.destroyAllWindows()


# In[4]:


#MERGING
# import PIL module
from PIL import Image
import cv2
  
# Front Image
filename = 'img1.png'
  
# Back Image
filename1 = 'img2.png'
  
# Open Front Image
frontImage = Image.open(filename)
  
# Open Background Image
background = Image.open(filename1)
  
# Convert image to RGBA
frontImage = frontImage.convert("RGBA")
  
# Convert image to RGBA
background = background.convert("RGBA")
  
# Calculate width to be at the center
width = (background.width - frontImage.width) // 2
  
# Calculate height to be at the center
height = (background.height - frontImage.height) // 2
  
# Paste the frontImage at (width, height)
background.paste(frontImage, (width, height), frontImage)
  
# Save this image
background.save("newimg.png", format="png")


# In[5]:


from PIL import Image,ImageDraw,ImageFilter
im1=Image.open('img1.png')
im2=Image.open('img2.png')
back_im=im1.copy()
back_im.paste(im2,(100,100))
back_im.show()


# In[15]:


#MEDIAN FILTERING
import cv2
import numpy as np
img_noisy1=cv2.imread("filter.png",0)
m,n=img_noisy1.shape
img_new1=np.zeros([m,n])
for i in range(1,m-1):
    for j in range(1,n-1):
        temp=[img_noisy1[i-1,j-1],img_noisy1[i-1,j],img_noisy1[i-1,j-1],img_noisy1[i-1,j+1],img_noisy1[i,j-1],img_noisy1[i,j],img_noisy1[i,j+1],img_noisy1[i+1,j-1],img_noisy1[i+1,j],img_noisy1[i+1,j+1]]
        temp=sorted(temp)
        img_new1[i,j]=temp[4]
        img_new1=img_new1.astype(np.uint8)
cv2.imshow("MEDIAN FILTERED IMAGE",img_new1)
cv2.waitKey(0)  
cv2.destroyAllWindows()        


# In[ ]:




