import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam

def user_input(i):
    return [1, i, i*i]


x_train = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_train = np.array([5*i**2 + 7*i + 9 for i in x_train])
x_train_expanded = np.array([user_input(i) for i in x_train])

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(30, input_shape=(3,), activation='relu'),
    tf.keras.layers.Dense(5, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(loss='mean_squared_error', optimizer=Adam())

model.fit(x_train_expanded, y_train, epochs=100, batch_size=32)


for i in x_train:
    print('For input : ', i, ', Output is : ', round(
        model.predict([user_input(i)])[0][0]))
