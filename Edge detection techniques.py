#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Canny Edge Detection
import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")

loaded_image=cv2.imread("apple.jpg")
loaded_image=cv2.cvtColor(loaded_image,cv2.COLOR_BGR2RGB)

gray_image=cv2.cvtColor(loaded_image,cv2.COLOR_BGR2GRAY)

edged_image=cv2.Canny(gray_image,threshold1=280,threshold2=280)

plt.figure(figsize=(20,20))
plt.subplot(1,3,1)
plt.imshow(loaded_image,cmap="gray")
plt.title("Original image")
plt.axis("off")
plt.subplot(1,3,2)
plt.imshow(gray_image,cmap="gray")
plt.axis("off")
plt.title("Grayscale image")
plt.subplot(1,3,3)
plt.imshow(edged_image,cmap="gray")
plt.axis("off")
plt.title("Canny edge detected image")
plt.show()


# In[28]:


#Laplacian and Sobel Edge detecting methods
import cv2
import numpy as np
import matplotlib.pyplot as plt

img0=cv2.imread("apple.jpg")
gray=cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
img=cv2.GaussianBlur(gray,(3,3),0)

laplacian=cv2.Laplacian(img,cv2.CV_64F)
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap="gray")
plt.title("Original"),plt.xticks([]),plt.yticks([])

plt.subplot(2,2,2),plt.imshow(laplacian,cmap="gray")
plt.title("Laplacian"),plt.xticks([]),plt.yticks([])

plt.subplot(2,2,3),plt.imshow(sobelx,cmap="gray")
plt.title("Sobel X"),plt.xticks([]),plt.yticks([])

plt.subplot(2,2,4),plt.imshow(sobely,cmap="gray")
plt.title("Sobel Y"),plt.xticks([]),plt.yticks([])

plt.show()


# In[30]:


#Edge detection using Prewitt operator
import cv2
import numpy as np
import matplotlib.pyplot as plt

img0=cv2.imread("apple.jpg")
gray=cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)
img=cv2.GaussianBlur(gray,(3,3),0)

kernelx=np.array([[1,1,1,],[0,0,0],[-1,-1,-1]])
kernely=np.array([[-1,0,1,],[-1,0,1],[-1,0,1]])
img_prewttx=cv2.filter2D(img,-1,kernelx)
img_prewtty=cv2.filter2D(img,-1,kernely)

cv2.imshow("Original image",img0)
cv2.imshow("Prewitt X",img_prewttx)
cv2.imshow("Prewitt Y",img_prewtty)
cv2.imshow("Prewitt",img_prewttx+img_prewtty)
cv2.waitKey()
cv2.destroyAllWindows()


# In[32]:


#Roberts edge detection-Roberts cross drtection
#Roberts Edge Detection- Roberts cross operator
import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt
roberts_cross_v = np.array( [[1, 0 ],[0,-1]])

roberts_cross_h =np.array( [[0, 1 ],[-1,0]])
img = cv2.imread("apple.jpg",0) .astype( 'float64')
img/=255.0

vertical = ndimage.convolve( img, roberts_cross_v )
horizontal = ndimage.convolve( img, roberts_cross_h )

edged_img =np.sqrt(np.square(horizontal) + np.square(vertical))
edged_img*=255
cv2.imwrite("output.jpg",edged_img)
cv2.imshow("OutputImage",edged_img)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:




