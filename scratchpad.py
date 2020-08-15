import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open("temp.png")
np_img = np.asarray(image)

plt.imshow(np_img, cmap='Greys')
plt.show()