#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BITWISE OPERATORS
import cv2 as cv

img1 = cv.imread('im1.jpg')
img2 = cv.imread('im2.jpg')
bitwise_AND = cv.bitwise_and(img1, img2)
bitwise_OR = cv.bitwise_or(img1, img2)
bitwise_NOT = cv.bitwise_not(img1)

cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('AND',bitwise_AND)
cv.imshow('OR',bitwise_OR)
cv.imshow('NOT',bitwise_NOT)
cv.waitKey(0)  
cv.destroyAllWindows()

