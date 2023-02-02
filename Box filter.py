#!/usr/bin/env python
# coding: utf-8

# In[11]:


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('6.jpg')

blur = cv2.blur(img,(5,5))

cv2.imshow("OI",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.imshow("Blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




