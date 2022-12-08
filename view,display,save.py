#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
image=cv2.imread("2.jpg")
cv2.imshow('To display images',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


cv2.imwrite('C:/Users/User/Desktop/2.jpg',image)


# In[8]:


#Height and Width of image
from PIL import Image
x="3.jpg"
img =Image.open(x)

width = img.width
height = img.height
print("The height of the image is: ", height)
print("The width of the image is: ", width)


# In[11]:


#No. of channels from color image
import numpy
image=cv2.imread("5.jpg",0)
print("No. of channels is:"+str(image.ndim))
print("No. of channels is:",image.shape)
cv2.imshow("Channel",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


#No. of channels from gray-scale image
import numpy
image=cv2.imread("5.jpg")
print("No. of channels is:"+str(image.ndim))
print("No. of channels is:",image.shape)
cv2.imshow("Channel",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[14]:


#Resize image
from PIL import Image
x="4.jpg"
img =Image.open(x)
new_im=img.resize((200,200))
new_im


# In[15]:


#Matrix representation of image

import matplotlib.image as image
img=image.imread("5.jpg")
print("The shape of the image is",img.shape)
print("The array of image is")
print(img)


# In[37]:


#Binary image

import cv2
img=cv2.imread("2.jpg",0)
ret,bw_img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#Converting to its binary form
bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow("BINARY",bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[44]:



import cv2
img=cv2.imread("3.jpg")
B,G,R=cv2.split(img)
print(B)
print(G)
print(R)


# In[39]:


cv2.imshow("Blue",B)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[40]:


cv2.imshow("Green",G)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[41]:


cv2.imshow("Red",R)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[45]:


#Aspect ratio

img=cv2.imread("3.jpg")
new_im=img.resize((400,200))
ar=1*(img.shape[1]/img.shape[0])
print("Aspect ratio")
print(ar)


# In[ ]:




