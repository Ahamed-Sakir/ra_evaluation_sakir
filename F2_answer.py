import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Input, Dense, Conv2D, ReLU
from tensorflow.keras.models import Model


input1 = np.random.rand(100,100,3) * 255
input2 = np.random.rand(100,100,3) * 255

# First input
input_1 = tf.keras.layers.Input(shape=(128, 128, 3))
conv_d = tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu')(input_1)
relu_x = tf.keras.layers.ReLU()(conv_d)

#Second input
input_2 = tf.keras.layers.Input(shape=(128, 128, 3))
conv_d2 = tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu')(input_2)
relu_y = tf.keras.layers.ReLU()(conv_d2)

# concatenate two layers
add = tf.keras.layers.Add()([relu_x, relu_y])

conv_f = tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu')(add)
relu_z = tf.keras.layers.ReLU()(conv_f)


predictions = Dense(10, activation='softmax')(relu_z)
model = Model(inputs=[input1, input2], outputs=predictions)


model.compile(loss='mean_squared_error', optimizer=Adam())

model.fit(inputs=[input1, input2], outputs=predictions, epochs=100, batch_size=32)

