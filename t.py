import cv2
import numpy as np
import pandas as pd

img1 = cv2.imread('z1.jpg')
img2 = cv2.imread('z2.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

image = np.concatenate((gray1, gray2))

df1 = pd.DataFrame(gray1)
df2 = pd.DataFrame(gray2)  # ndarray to data frame
df = pd.concat([df1, df2])
# 纵向连接,横向连接=pd.concat([df1, df2], axis=1)

image = np.array(df)  # dataframe to ndarray

# =============

cv2.imwrite('im.jpg', image)
cv2.imshow('image.jpg', image)
