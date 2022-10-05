#!/usr/bin/env python3

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

#print(tf.__version__)
mnist = tf.keras.datasets.mnist # 28x28 images of hand-written digits 0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()    # Load data
x_train = tf.keras.utils.normalize(x_train, axis=1)         # Normalize model
x_test = tf.keras.utils.normalize(x_test, axis=1)           # Normalize model

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())                            # Input layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))     # Hidden layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))     # Hidden layer
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))   # Output layer

model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print("Test loss is: ",val_loss)
print("Test accuracy is: ",val_acc)

#plt.imshow(x_train[0], cmap = plt.cm.binary)
#print(x_train[0])
#plt.show()

model.save('epic_num_reader.model')
new_model = tf.keras.models.load_model('epic_num_reader.model')
predictions = new_model.predict([x_test])
print(np.argmax(predictions[0]))
plt.imshow(x_test[0], cmap = plt.cm.binary)
plt.show()
