#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
image=cv2.imread("2.jpg")
cv2.imshow('To display images',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


cv2.imwrite('C:/Users/User/Desktop/2.jpg',image)


# In[ ]:


#Height and Width of image
from PIL import Image
x="3.jpg"
img =Image.open(x)

width = img.width
height = img.height
print("The height of the image is: ", height)
print("The width of the image is: ", width)


# In[ ]:


#No. of channels from color image
import numpy
image=cv2.imread("5.jpg",0)
print("No. of channels is:"+str(image.ndim))
print("No. of channels is:",image.shape)
cv2.imshow("Channel",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


#No. of channels from gray-scale image
import numpy
image=cv2.imread("5.jpg")
print("No. of channels is:"+str(image.ndim))
print("No. of channels is:",image.shape)
cv2.imshow("Channel",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


#Resize image
from PIL import Image
x="4.jpg"
img =Image.open(x)
new_im=img.resize((200,200))
new_im


# In[ ]:


#Matrix representation of image

import matplotlib.image as image
img=image.imread("5.jpg")
print("The shape of the image is",img.shape)
print("The array of image is")
print(img)


# In[ ]:


#Binary image

import cv2
img=cv2.imread("2.jpg",0)
ret,bw_img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#Converting to its binary form
bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow("BINARY",bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[1]:



import cv2
img=cv2.imread("3.jpg")
B,G,R=cv2.split(img)
print(B)
print(G)
print(R)


# In[2]:


cv2.imshow("Blue",B)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


cv2.imshow("Green",G)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


cv2.imshow("Red",R)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


#Aspect ratio

img=cv2.imread("3.jpg")
new_im=img.resize((400,200))
ar=1*(img.shape[1]/img.shape[0])
print("Aspect ratio")
print(ar)


# In[ ]:


#Mirror image
from PIL import Image
x="4.jpg"
img =Image.open(x)
hori_flip=img.transpose(Image.FLIP_LEFT_RIGHT)

hori_flip.show()

verti_flip=img.transpose(Image.FLIP_TOP_BOTTOM)
verti_flip.show()


# In[ ]:


#Different color spaces

import cv2
img=cv2.imread("6.jpg")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
hls=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
yuv=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

cv2.imshow("GREY",grey)
cv2.imshow("HSV",hsv)
cv2.imshow("LAB",lab)
cv2.imshow("HLS",hls)
cv2.imshow("YUV",yuv)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


import cv2
img1=cv2.imread("im1.jpg")
img2=cv2.imread("im2.jpg")
sum=img1+img2
sub=img1-img2
mul=img1*img2
div=img1/img2
cv2.imshow("SUB:",sub)
cv2.imshow("SUM:",sum)
cv2.imshow("MUL:",mul)
cv2.imshow("DIV:",div)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




