from tensorflow import keras
import numpy as np

def init_nn(input_dim, output_dim){
    input_dim = 16

    originNet = keras.Sequential([
        keras.layers.Flatten(input_shape=(input_dim,)),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(4, activation='softmax')
    ])

    destinyNet = keras.Sequential([
        keras.layers.Flatten(input_shape=(input_dim,)),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(4, activation='softmax')
    ])

    originNet.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    destinyNet.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    return input_dim, output_dim
}