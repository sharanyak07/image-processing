#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread("wt.png")
plt.imshow(img)
plt.show()

alpha = 2.0
beta = -160

new = alpha * img + beta
new = np.clip(new, 0, 255).astype(np.uint8)
plt.show()
plt.imshow(new)

cv2.imshow('To display image',new)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




