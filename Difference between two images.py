#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import module
from PIL import Image, ImageChops
import matplotlib.pyplot as plt

# assign images
img1 = Image.open("1img.jpg")
plt.imshow(img1)
plt.show()
img2 = Image.open("2img.jpg")
plt.imshow(img2)
plt.show()

# finding difference
diff = ImageChops.difference(img1, img2)
plt.imshow(diff)
plt.show()
# showing the difference



# In[ ]:




