# 3. Computer Vision and Convolutional Neural Networks in TensorFlow
## 109. Becoming One With Data Part 2
```python
import matplotlib.image as mpimg
img = mpimg.imread(os.path.join(target_folder, random_image[0]))
```

## 111. Building an end to end CNN Model
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator()
```
```python
data = datagen.flow_from_directory(directory=train_dir,
                                               batch_size=32,
                                               target_size=(224, 224),
                                               class_mode="binary",
                                               seed=42)
```
```python
tf.keras.layers.Conv2D()
tf.keras.layers.MaxPooling2D()
```

## 112. Using a GPU to run our CNN model 5x faster
[Doc: CNN Explainer](https://poloclub.github.io/cnn-explainer/)<br>

## 113. Trying a non-CNN model on our image data
[Doc: `tf.nn.relu`](https://www.tensorflow.org/api_docs/python/tf/nn/relu)<br>
[Doc: `tf.keras.activations.relu`](https://www.tensorflow.org/api_docs/python/tf/keras/activations/relu)<br>
`tf.keras.activations.relu` is part of the high-level Keras API in TensorFlow, designed for use within Keras model layers and offers additional customization options.<br>
On the other hand, `tf.nn.relu` belongs to TensorFlow's lower-level neural network API, typically used in more custom and granular tensor operations.<br>
While both perform the same basic ReLU operation, `tf.keras.activations.relu` is more suited for standard model building in Keras due to its seamless integration and additional features.
```python
tf.nn.relu
tf.keras.activations.relu
```
## 118. Breaking our CNN model down part 4: Building a baseline CNN model
[https://paperswithcode.com/sota](https://paperswithcode.com/sota)<br>

## 119. Breaking our CNN model down part 5: Looking inside a Conv2D layer
```python
# these two lines are equivalent
tf.keras.layers.Conv2D(filters=10, kernel_size=(3,3), strides=(1, 1), padding="same")
tf.keras.layers.Conv2D(filters=10, kernel_size=3, strides=1, padding="same")

```