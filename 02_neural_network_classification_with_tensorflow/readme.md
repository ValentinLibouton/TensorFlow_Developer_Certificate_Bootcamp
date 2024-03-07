# 2. Neural Network Classification With Tensorflow
## 74. Creating and viewing classification data to model
[Resource: TensorFlow Playground](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.00227&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)<br>

## 76. Building a not very good classification model with TensorFlow
```python
loss = tf.keras.losses.BinaryCrossentropy()
metrics = tf.keras.metrics.BinaryAccuracy()
```

## 78. Creating a function to view our model's not so good prediction
[Doc: `numpy.meshgrid()`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html)<br>
```python
numpy.meshgrid()
```
[Doc: `numpy.c_[]`](https://numpy.org/doc/stable/reference/generated/numpy.c_.html)<br>
```python
# Translates slice objects to concatenation along the second axis.
np.c_[np.array([1,2,3]), np.array([4,5,6])]
>>> array([[1, 4],
           [2, 5],
           [3, 6]])

np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]
>>> array([[1, 2, 3, ..., 4, 5, 6]])
```
[Doc: `numpy.ravel()`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html)<br>
```python
x = np.array([[1, 2, 3], [4, 5, 6]])

np.ravel(x)
>>> array([1, 2, 3, 4, 5, 6
```

## 84. Non-linearity part 4: Modelling our non-linear data once and for all
```python
activation=tf.keras.activations.sigmoid
# or
activation=["sigmoid"]
```