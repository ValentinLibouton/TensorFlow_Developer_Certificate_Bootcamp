# 1. Neural Network Regression With Tensorflow
## Methods
### 44. The major steps in modelling with TensorFlow
[Doc: `tf.keras.Sequential()`](https://www.tensorflow.org/api_docs/python/tf/keras/Sequential)<br>
```python
tf.keras.Sequential()
```
[Doc: about **model.compile**, **model.fit**, etc. &rarr; `tf.keras.Model()`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)<br>
```python
model.compile()
model.fit()
model.predict()
model.summary()
```
[Doc: `tf.keras.layers.Dense()`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)<br>
```python
tf.keras.layers.Dense()
```
[Doc: `tf.keras.losses.MeanAbsoluteError()`](https://www.tensorflow.org/api_docs/python/tf/keras/losses/MeanAbsoluteError)<br>
```python
tf.keras.losses.MeanAbsoluteError()
```
[Doc: `tf.keras.optimizers.SGD()`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/experimental/SGD)<br>
```python
tf.keras.optimizers.SGD()
# or
'sgd'
```
[Doc: `tf.keras.metrics.MeanAbsoluteError()`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics/MeanAbsoluteError)<br>
```python
tf.keras.metrics.MeanAbsoluteError()
# or
'mean_absolute_error'
# or 
'mae'
```
### 45. Steps in improving a model with TensorFlow part 1

### 51. Evaluating a TensorFlow model part 4 (visualising a model's layers)
[Doc: `tf.keras.utils.plot_model()`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/plot_model)<br>
```python
from tensorflow.keras.utils import plot_model

plot_model(model=model, show_shapes=True)
```
### 59. How to save a TensorFlow model
```python
# Save model using the SavedModel format
model.save(filepath="best_model_SavedModel_format")

# Save model using the HDF5 format
model.save("best_model_HDF5_format.h5")
```
### 60. How to load and use a saved TensorFlow model
```python
# Load in the SavedModel format model
loaded_SavedModel_format = tf.keras.models.load_model("best_model_SavedModel_format")

# Load in a model using the .h5 format
loaded_h5_model = tf.keras.models.load_model("best_model_HDF5_format.h5")
```

### 61. How to save and download files from Google Colab
```python
# Download a file from Google Colab
from google.colab import files
files.download("best_model_HDF5_format.h5")
# or
# Save a file from Google Colab to Google Drive (requires mounting Google Drive)
!cp /content/best_model_HDF5_format.h5 /content/drive/MyDrive/TensorFlowDeveloperCertificateBootcamp/01_neural_network_regression_with_tensorflow_video
```
### 62. Putting together what we've learned part 1 (preparing a dataset)

```python
import pandas as pd
pd.get_dummies()
```

[Doc: `sklearn.model_selection.train_test_split()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)<br>
```python
# Create training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
### 66. Preprocessing data with feature scaling part 2 (normalising our data)
```python
sklearn.compose.make_column_transformer()
sklearn.preprocessing.MinMaxScaler()
sklearn.preprocessing.OneHotEncoder()
```
