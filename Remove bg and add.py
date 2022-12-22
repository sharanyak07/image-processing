#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Adding two images and remove bg of first image
from PIL import Image,ImageDraw,ImageFilter
im1=Image.open("i10.jpg")
im2=Image.open("i9.jpg")
mask_im=Image.new("L",im2.size,0)
draw=ImageDraw.Draw(mask_im)
draw.ellipse((90,110,725,770),fill=225)
mask_im_blur=mask_im.filter(ImageFilter.GaussianBlur(5))
back_im=im1.copy()
back_im.paste(im2,(0,0),mask_im_blur)
back_im.show()

