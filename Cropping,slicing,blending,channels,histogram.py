#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Coverting oe file format to another
from PIL import Image
im = Image.open("6.jpg")
print("Image coverted")
im.save("D:/6.png")


# In[11]:


print(im.mode)


# In[9]:


#Cropping image
import cv2
img=cv2.imread("6.jpg")
crop=img[50:200,100:400]
cv2.imshow("ORIGINAL IMAGE",img)
cv2.imshow("CROPPED IMAGE",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[13]:


#ARRAY SLICING
import cv2
from PIL import Image
import numpy as np
im=np.array(Image.open("5.jpg").resize((256,256)))
im1=im[:,:100]
im2=im[:,100:]
cv2.imshow("image 1",im1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("image 2",im2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[7]:


#IMAGE BLENDING
from PIL import Image
im1=Image.open("im1.jpg")
im2=Image.open("im2.jpg")

alpha1=Image.blend(im1,im2,alpha=.4)
alpha2=Image.blend(im1,im2,alpha=.2)

alpha1.show()
alpha2.show()


# In[8]:


#NEGATING AN IMAGE
im = Image.open("6.jpg")
imn=im.point(lambda x:255-x)
imn.show()


# In[53]:


#WRITING TEXT ON AN IMAGE
import cv2
 
image = cv2.imread("5.jpg")
 

new_image = cv2.putText(
  img = image,
  text = "Good Morning",
  org = (200, 200),
  fontFace = cv2.FONT_HERSHEY_DUPLEX,
  fontScale = 3.0,
  color = (125, 246, 55),
  thickness = 3
)
 

cv2.imwrite("New Wallpaper.jpg", new_image)
cv2.imshow("image 2",new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[56]:


#DRAWING ON AN IMAGE
from PIL import Image,ImageDraw
img=Image.open("5.jpg")
draw=ImageDraw.Draw(img)
draw.rectangle(xy=(50,50,150,150),
fill = (0,127,0))
img.show()


# In[41]:


#HISTOGRAM
import matplotlib.pyplot as plt
im = Image.open("6.jpg")
pl=im.histogram()
plt.bar(range(256),pl[:256],color="r",alpha=0.5)
plt.bar(range(256),pl[256:2*256],color="g",alpha=0.4)
plt.bar(range(256),pl[2*256:],color="b",alpha=0.3)


# In[47]:


#RGB CHANNELS
from skimage.io import imread,imshow
import matplotlib.pyplot as plt
img=imread("3.jpg")
imshow(img)
fig,ax=plt.subplots(1,3,figsize=(12,4),sharey=True)
ax[0].imshow(img[:,:,0],cmap="Reds")
ax[0].set_title("RED")
ax[1].imshow(img[:,:,1],cmap="Greens")
ax[1].set_title("GREEN")
ax[2].imshow(img[:,:,2],cmap="Blues")
ax[2].set_title("BLUE")


# In[57]:


#BASIC STATISTICS 
from PIL import Image,ImageStat
im = Image.open("4.jpg")
stat=ImageStat.Stat(im)
print("MEAN:",stat.mean)
print("MEDIAN:",stat.median)
print("STANDARD DEVIATION:",stat.stddev)


# In[10]:


#SLICING
from skimage.io import imread,imshow
import matplotlib.pyplot as plt
image=imread("4.jpg")
imshow(image)
fig,ax=plt.subplots(1,3,figsize=(12,4),sharey=True)
ax[0].imshow(image[:,0:200])
ax[0].set_title('FIRST SPLIT')
ax[1].imshow(image[:,300:400])
ax[1].set_title('SECOND SPLIT')
ax[2].imshow(image[:,420:590])
ax[2].set_title('THIRD SPLIT');


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




