# -*- coding: utf-8 -*-
"""This is the first and the last time.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iWwnIzLuFCp2WTEcT5mI9i-Qt-aBdgaI
"""

# import the necessary packages
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K

class MiniVGGNet:
	@staticmethod
	def build(width, height, depth, classes):
		# initialize the model along with the input shape to be
		# "channels last" and the channels dimension itself
		model = Sequential()
		inputShape = (height, width, depth)
		chanDim = -1

		# if we are using "channels first", update the input shape
		# and channels dimension
		if K.image_data_format() == "channels_first":
			inputShape = (depth, height, width)
			chanDim = 1

		# first CONV => RELU => CONV => RELU => POOL layer set
		model.add(Conv2D(32, (3, 3), padding="same",
			input_shape=inputShape))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(32, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dropout(0.25))

		# second CONV => RELU => CONV => RELU => POOL layer set
		model.add(Conv2D(64, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(64, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dropout(0.25))

		# first (and only) set of FC => RELU layers
		model.add(Flatten())
		model.add(Dense(512))
		model.add(Activation("relu"))
		model.add(BatchNormalization())
		model.add(Dropout(0.5))

		# softmax classifier
		model.add(Dense(classes))
		model.add(Activation("softmax"))

		# return the constructed network architecture
		return model

!wget --header='Host: doc-04-64-docs.googleusercontent.com' --header='User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' --header='Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' --header='Accept-Language: en-US,en;q=0.9' --header='Referer: https://drive.google.com/drive/folders/1F2PjpJ_u_iaD-Fs0wwcymRiVVLK34-Fu' --header='Cookie: AUTH_j6r6t3mpuhqufq9pdn0hhhqb488utbpe=09940060955156330516|1554904800000|p91e2kepnv5tareuvv3lc27kgjmkbqg2' --header='Connection: keep-alive' 'https://doc-04-64-docs.googleusercontent.com/docs/securesc/sh1m781e47f6b6t63sunal1qpse70m7t/8njt89g72v0ht67ahoi3rme6u6f2u6l0/1554904800000/13298636624145636532/09940060955156330516/16rGDv7syd_gR5xIBgHvflMehePTBCDmy?e=download' -O 'test_image.pkl' -c



!wget --header='Host: doc-0c-64-docs.googleusercontent.com' --header='User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' --header='Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' --header='Accept-Language: en-US,en;q=0.9' --header='Referer: https://drive.google.com/drive/folders/1F2PjpJ_u_iaD-Fs0wwcymRiVVLK34-Fu' --header='Cookie: AUTH_j6r6t3mpuhqufq9pdn0hhhqb488utbpe_nonce=j5kn34r7b72bs' --header='Connection: keep-alive' 'https://doc-0c-64-docs.googleusercontent.com/docs/securesc/sh1m781e47f6b6t63sunal1qpse70m7t/5uhipmetm9j1eab8thg0mfg8jtaber31/1554904800000/13298636624145636532/09940060955156330516/1ajCMiUI6Wv8QdpYmtbcM--U4RTFVH6zq?e=download&nonce=j5kn34r7b72bs&user=09940060955156330516&hash=v0q87vrie62jrakr8qn4nt8qs6g8spbc' -O 'train_image.pkl' -c

!wget --header='Host: doc-0s-64-docs.googleusercontent.com' --header='User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' --header='Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' --header='Accept-Language: en-US,en;q=0.9' --header='Referer: https://drive.google.com/drive/folders/1F2PjpJ_u_iaD-Fs0wwcymRiVVLK34-Fu' --header='Cookie: AUTH_j6r6t3mpuhqufq9pdn0hhhqb488utbpe=09940060955156330516|1554904800000|p91e2kepnv5tareuvv3lc27kgjmkbqg2' --header='Connection: keep-alive' 'https://doc-0s-64-docs.googleusercontent.com/docs/securesc/sh1m781e47f6b6t63sunal1qpse70m7t/l1hl691cl58n1sksh5cr10q4e60lt4tu/1554904800000/13298636624145636532/09940060955156330516/1CjWhqbqViHgS7ti5dajfiwC36qupwlhw?e=download' -O 'train_label.pkl' -c

from sklearn.utils import shuffle
trainX, y = shuffle(trainX, y, random_state=0)

# USAGE
# python fashion_mnist.py

# set the matplotlib backend so figures can be saved in the background
import matplotlib
matplotlib.use("Agg")

# import the necessary packages
from sklearn.metrics import classification_report
from keras.optimizers import SGD
from keras.datasets import fashion_mnist
from keras.utils import np_utils
from keras import backend as K
from imutils import build_montages
import matplotlib.pyplot as plt
import numpy as np
import cv2

# initialize the number of epochs to train for, base learning rate,
# and batch size
NUM_EPOCHS = 25
INIT_LR = 1e-3
BS = 64

# grab the Fashion MNIST dataset (if this is your first time running
# this the dataset will be automatically downloaded)
# print("[INFO] loading Fashion MNIST...")
# ((trainX, trainY), (testX, testY)) = fashion_mnist.load_data()

import pickle

with open('train_image.pkl', 'rb') as f:
    x = pickle.load(f)
    
with open('train_label.pkl', 'rb') as g:
    y = pickle.load(g)

with open('test_image.pkl', 'rb') as h:
    test = pickle.load(h)    
    
import numpy as np
# np.array(x).shape

trainX = np.array(x)
testX = np.array(test)

from sklearn.utils import shuffle
trainX, y = shuffle(trainX, y, random_state=0)

# if we are using "channels first" ordering, then reshape the design
# matrix such that the matrix is:
# 	num_samples x depth x rows x columns
if K.image_data_format() == "channels_first":
	trainX = trainX.reshape((trainX.shape[0], 1, 28, 28))
	testX = testX.reshape((testX.shape[0], 1, 28, 28))
 
# otherwise, we are using "channels last" ordering, so the design
# matrix shape should be: num_samples x rows x columns x depth
else:
	trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
	testX = testX.reshape((testX.shape[0], 28, 28, 1))
 
# scale data to the range of [0, 1]
trainX = trainX.astype("float32") / 255.0
testX = testX.astype("float32") / 255.0


dic = {0:0, 2:1, 3:2, 6:3}

y_ = [dic.get(n, n) for n in y]

# one-hot encode the training and testing labels
trainY = np_utils.to_categorical(y_, 4)

# initialize the label names
# labelNames = ["top", "trouser", "pullover", "dress", "coat",
# 	"sandal", "shirt", "sneaker", "bag", "ankle boot"]

# initialize the optimizer and model
print("[INFO] compiling model...")
opt = SGD(lr=INIT_LR, momentum=0.9, decay=INIT_LR / NUM_EPOCHS)
model = MiniVGGNet.build(width=28, height=28, depth=1, classes=4)
model.compile(loss="categorical_crossentropy", optimizer=opt,
	metrics=["accuracy"])

# train the network
print("[INFO] training model...")
H = model.fit(trainX, trainY,
	validation_split=0.07,
	batch_size=BS, epochs=NUM_EPOCHS)

# make predictions on the test set
preds = model.predict(testX)

# %matplotlib inline
# show a nicely formatted classification report
# print("[INFO] evaluating network...")
# print(classification_report(testY.argmax(axis=1), preds.argmax(axis=1),
# 	target_names=labelNames))

# plot the training loss and accuracy
N = NUM_EPOCHS
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, N), H.history["acc"], label="train_acc")
plt.plot(np.arange(0, N), H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy on Dataset")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="lower left")

import pandas as pd
probs = model.predict(testX)
prediction = probs.argmax(axis=1)
pd.DataFrame(prediction).shape

submit = pd.DataFrame()
submit['image_index'] = list(range(0,2000))
submit['class']= prediction
submit.head()

submit['class'] = submit['class'].replace({0:0,1:2,2:3,3:6})
submit.head()
submit.groupby('class').size()

submit.to_csv('sumit_tripathi.csv',index=False)

