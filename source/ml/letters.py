import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('temp.png')
res = cv2.resize(img, dsize=(28, 28))
np_img = np.asarray(res)
np_img = (np_img/255) - 0.4
np_img = np.ceil(np_img).astype(int)
np_img = np_img*255

plt.imshow(np_img, cmap='Greys')
plt.show()