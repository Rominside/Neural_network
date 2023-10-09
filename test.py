import keras.models
from keras.models import Sequential
import pandas as pd
import tensorflow as tf
import numpy as np
from neuron import Neuron


def test():
    x_train = np.array([
        [-2, -1],  # Алиса
        [25, 6],  # Боб
        [17, 4],  # Чарли
        [-15, -6],  # Диана
    ])
    y_train = np.array([
        1,  # Алиса
        0,  # Боб
        0,  # Чарли
        1,  # Диана
    ])

    x_test = np.array([[-7, -3], [20, 2]])
    y_test = np.array([1, 0])

    classifier = Sequential()
    classifier.add(tf.keras.layers.Dense(units=2, activation='relu'))
    classifier.add(tf.keras.layers.Dense(units=1, activation='relu'))

    classifier.compile(optimizer='RMSprop', loss='binary_crossentropy')
    classifier.fit(x=x_train, y=y_train, batch_size=1, epochs=30)

    classifier.save("model_test")
    classifier_loaded = keras.models.load_model("model_test")
    classifier_loaded.evaluate(x_test, y_test)

    y_pred = classifier.predict(x_test)
    print(y_pred)
    y_pred = [1 if y >= 0.5 else 0 for y in y_pred]

    total = 0
    correct = 0
    wrong = 0
    for i in range(len(y_pred)):
        total = total + 1
        if y_test[i] == y_pred[i]:
            correct = correct + 1
        else:
            wrong = wrong + 1

    print("Total " + str(total))
    print("Correct " + str(correct))
    print("Wrong " + str(wrong))


if __name__ == "__main__":
    # test()
    # [[6.510165]
    #  [0.      ]]
    classifier_loaded = keras.models.load_model("model_test")
    print(classifier_loaded.layers[0].weights)
    print(classifier_loaded.summary())

    List_0 = [Neuron(weight=np.array([-0.7069869  ,  -1.0857788 ], dtype=float), porog=0, childs=None),
              Neuron(weight=np.array([  0.43153012,  0.9109777 ], dtype=float), porog=0, childs=None)]

    List_1 = Neuron(weight=np.array([ 0.7933184, -0.1214025], dtype=float), porog=0, childs=List_0)

    print(List_1.getout([-7, -3]))
    print(List_1.getout([20, 2]))
