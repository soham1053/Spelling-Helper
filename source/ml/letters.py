import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D

X = np.load('letters_X.npy')
y = np.load('letters_y.npy')

print(f'X-shape, y-shape: {X.shape}, {y.shape}')
print(f'X example shape, y example shape: {X[0].shape}, {y[0].shape}')

def idx2char(idx):
    return chr(idx+97)
def char2idx(char):
    return ord(char) - 96

ex = np.random.choice(np.arange(X.shape[0]))
plt.imshow(X[ex], cmap='Greys')
idx2char(y[ex])

X = (X/255) - 0.4
X = np.ceil(X).astype(int)

plt.clf()
plt.imshow(X[ex], cmap='Greys')
idx2char(y[ex])

X = X.reshape(X.shape[0], 28, 28, 1)
X = X.astype('float32')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=324)

model = Sequential()
model.add(Conv2D(16, (3, 3), input_shape=(28, 28, 1)))
model.add(Conv2D(8, (3, 3)))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(26, activation='softmax'))

model.compile('adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10)

model.evaluate(X_test, y_test)

model.save('letters_model')