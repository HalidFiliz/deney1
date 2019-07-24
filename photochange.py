# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 20:46:18 2019

@author: halid
"""

#%%

import glob
import numpy as np
from scipy.misc import imread, imsave, imresize

aa = glob.glob("pics/*.jpg")

#%%

mx0 = imread(aa[0])

(mx0[:,:,0], mx0[:,:,2]) = (mx0[:,:,2], mx0[:,:,0])

imsave("pics1/moddeer.jpg", mx0)

#%%

mx1 = imread(aa[1])

r, g, b = mx1[:,:,0], mx1[:,:,1], mx1[:,:,2]
gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

mx1[:,:,0], mx1[:,:,1], mx1[:,:,2] = gray, gray, gray

imsave("pics1/moddog.jpg", mx1)

#%%

mx2 = imread(aa[2])

r, g, b = mx2[:,:,0], mx2[:,:,1], mx2[:,:,2]
rm = np.min(r)
gm = np.min(g)
bm = np.min(b)
rma = np.max(r)
gma = np.max(g)
bma = np.max(b)
mx2 = (mx2 - [rm, gm, bm])/[rma-rm, bma-bm, gma-gm]

imsave("pics1/modfox.jpg", mx2)

#%%

mx3 = imread(aa[3])

pix = np.asarray(mx3)
pix = pix.astype('float32')

pix /= 255.0

imsave("pics1/modgoat.jpg", pix)

#%%
mx4 = imread(aa[4])

mx4new = imresize(mx4, (200, 200))

imsave("pics1/modseal.jpg", mx4new)
















