#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('6.jpg', cv2.IMREAD_GRAYSCALE)  
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.title('Original Image')
plt.imshow(img,cmap='gray')
plt.axis('off')

blur = cv2.GaussianBlur(img,(7,7),0)
plt.figure(figsize=(10,10))
plt.subplot(2,2,2)
plt.title('Gaussian Blur')
plt.imshow(blur,cmap='gray')
plt.axis('off')

x,threshold = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
plt.figure(figsize=(10,10))
plt.subplot(2,2,3)
plt.title('Binary Threshold')
plt.imshow(threshold ,cmap='gray')
plt.axis('off')

ret2,th2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.title('Otsus Thresholding')
plt.imshow(th2,cmap='gray')
plt.axis('off')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




