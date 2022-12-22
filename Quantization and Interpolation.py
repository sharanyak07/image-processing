#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Quantization
from PIL import Image
import PIL
img1=Image.open("3.jpg")
img1=img1.quantize(10)
img1.show()


# In[7]:


#interpolation
import cv2
import numpy as np

img=cv2.imread("s3.png")
near_img=cv2.resize(img,None,fx=5,fy=5,interpolation=cv2.INTER_NEAREST)
cv2.imshow('Near',near_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img=cv2.imread("s3.png")
bilinear_img = cv2.resize(img,None, fx = 5, fy = 5, interpolation = cv2.INTER_LINEAR)
cv2.imshow('Bilinear',bilinear_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


img=cv2.imread("s3.png")
bicubic_img = cv2.resize(img,None, fx = 5, fy = 5, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Bicubic",bicubic_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# In[ ]:




