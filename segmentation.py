#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Superpixel segmentation
from skimage.segmentation import slic
from skimage.color import label2rgb
import matplotlib.pyplot as plt

face_image=plt.imread("face1.jpg")
segments=slic(face_image,n_segments=400)
segmented_image=label2rgb(segments,face_image,kind='avg')

plt.title("ORIGINAL")
plt.imshow(face_image.astype('uint8'))
plt.show()

plt.title("Segmented image")
plt.imshow(segmented_image.astype('uint8'))
plt.show()


# In[ ]:




