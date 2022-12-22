#!/usr/bin/env python
# coding: utf-8

# In[6]:


#text on image
from PIL import Image,ImageDraw,ImageFont
img = Image.open("5.jpg")
draw = ImageDraw.Draw(img)
txt="GOOD MORNING"

font = ImageFont.truetype('ALGER.TTF',90)

draw.text((300,300),txt,font=font)
img.show()


# In[ ]:




