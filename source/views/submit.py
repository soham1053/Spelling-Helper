from source import app
import io
from PIL import Image
import base64
import re
import numpy as np
from flask import request, session
import cv2
from tensorflow.keras.models import load_model

model = load_model('letters_model')

@app.route("/submit", methods=["POST"])
def submit():
	image_b64 = request.values['imageBase64']
	image_data = re.sub('^data:image/.+;base64,', '', image_b64)
	image_data = base64.decodestring(image_data.encode())
	image_PIL = Image.open(io.BytesIO(image_data))
	res = image_PIL.resize((28, 28))
	np_img = np.asarray(res)
	np_img = (np_img/255) - 0.4
	np_img = np.ceil(np_img).astype(int)
	np_img = np_img*255
	np_img = abs(np_img - 255)

	pred = chr(model.predict(np_img[:,:,0].reshape(1, 28, 28, 1)).argmax()+97)

	print(f"Predicted Letter: {pred}")

	# print('Image received: {}'.format(image_np.shape)) # Prints out: Image received: (500, 500, 4)
	return pred