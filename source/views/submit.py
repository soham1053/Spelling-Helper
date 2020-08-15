from source import app
import io
from PIL import Image
import base64
import re
import numpy as np
import matplotlib.pyplot as plt
from flask import request

@app.route("/submit", methods=["POST"])
def submit():
	image_b64 = request.values['imageBase64']
	image_data = re.sub('^data:image/.+;base64,', '', image_b64)
	image_data = base64.decodestring(image_data.encode())
	image_PIL = Image.open(io.BytesIO(image_data))
	image_PIL.save("temp.png")
	image_np = np.array(image_PIL)
	plt.imshow(image_np, cmap='Greys')

	print('Image received: {}'.format(image_np.shape)) # Prints out: Image received: (500, 500, 4)
	return "done"