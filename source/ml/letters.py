import numpy as np
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.models import load_model 

img = cv2.imread('temp.png')
res = cv2.resize(img, dsize=(28, 28))
np_img = np.asarray(res)
np_img = (np_img/255) - 0.4
np_img = np.ceil(np_img).astype(int)
np_img = np_img*255
np_img = abs(np_img - 255)

model = load_model('letters_model')

print(chr(model.predict(np_img[:,:,0].reshape(1, 28, 28, 1)).argmax()+97))

plt.imshow(np_img, cmap='Greys')
plt.show()