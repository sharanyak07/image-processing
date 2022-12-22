#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Upsampling
from matplotlib import pyplot as plt
import cv2
img1 = cv2.imread('i1.jpg')
cv2.imshow('Image before pyrUp',img1)
img1=cv2.pyrUp(img1)
cv2.imshow('Image after pyrUp',img1)
plt.imshow(img1)
cv2.waitKey(0)  
cv2.destroyAllWindows()


# In[4]:


#Downsampling
from matplotlib import pyplot as plt
import cv2
img1 = cv2.imread('i1.jpg')
cv2.imshow('Image before pyrDown',img1)
img1=cv2.pyrDown(img1)
cv2.imshow('Image after pyrDown',img1)
plt.imshow(img1)
cv2.waitKey(0)  
cv2.destroyAllWindows()


# In[ ]:




