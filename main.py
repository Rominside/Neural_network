from keras.models import Sequential
import pandas as pd
import tensorflow as tf
import numpy as np


def test_network():
    dataset_train = pd.read_csv("Train.txt", sep=",", header=None)
    dataset_test = pd.read_csv("Test.txt", sep=",", header=None)

    dataset_train = dataset_train.drop(columns=dataset_train.iloc[:, 9:41])
    dataset_train = dataset_train.drop(columns=42)
    dataset_test = dataset_test.drop(columns=dataset_test.iloc[:, 9:41])
    dataset_test = dataset_test.drop(columns=42)

    dataset_train.loc[(dataset_train[41] == "normal", 41)] = 0
    dataset_train.loc[(dataset_train[41] != 0, 41)] = 1

    dataset_test.loc[(dataset_test[41] == "normal", 41)] = 0
    dataset_test.loc[(dataset_test[41] != 0, 41)] = 1

    y_train = dataset_train.iloc[:, 9:10]
    x_train = dataset_train.iloc[:, 0:9]
    x_test = dataset_test.iloc[:, 0:9]
    y_test = dataset_test.iloc[:, 9:10]

    print(pd.unique(y_train[41]))
    print(y_train.values)

    classifier = Sequential()
    classifier.add(tf.keras.layers.Dense(units=9, activation='sigmoid', input_dim=9))
    classifier.add(tf.keras.layers.Dense(units=9, activation='sigmoid'))
    classifier.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

    classifier.compile(optimizer='rmsprop', loss='binary_crossentropy')
    y_train = y_train.values.astype(float)
    # x_train = x_train.values.astype(float)
    classifier.fit(x=y_train, y=y_train, batch_size=1, epochs=10)

    y_pred = classifier.predict(x_test)
    y_pred = [1 if y >= 0.5 else 0 for y in y_pred]

    total = 0
    correct = 0
    wrong = 0
    for i in range(len(y_pred)):
        total = total + 1
        if y_test.at[i, 1] == y_pred[i]:
            correct = correct + 1
        else:
            wrong = wrong + 1

    print("Total " + str(total))
    print("Correct " + str(correct))
    print("Wrong " + str(wrong))


if __name__ == "__main__":
    test_network()
