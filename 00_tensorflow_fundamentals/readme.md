# 0. Tensorflow fundamentals
## Methods
### 16. Creating your first tensors with TensorFlow and tf.constant()
[Doc: `tf.constant()`](https://www.tensorflow.org/api_docs/python/tf/constant)<br>
```python
tf.constant()
```
### 17. Creating tensors with TensorFlow and tf.Variable()
[Doc: `tf.Variable()`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br>
```python
tf.Variable()
```
### 18. Creating random tensors with TensorFlow
[Doc: `tf.random.Generator.from_seed()`](https://www.tensorflow.org/api_docs/python/tf/random/Generator)<br>
```python
tf.random.Generator.from_seed()
```
### 19. Shuffling the order of tensors
[Doc: `tf.random.shuffle()`](https://www.tensorflow.org/api_docs/python/tf/random/shuffle)<br>
```python
tf.random.shuffle()
```
[Doc: `tf.random.set_seed()`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br>
```python
tf.random.set_seed()
```
[Doc: `tf.ones()`](https://www.tensorflow.org/api_docs/python/tf/ones)<br>
```python
tf.ones()
```
[Doc: `tf.zeros()`](https://www.tensorflow.org/api_docs/python/tf/zeros)<br>
```python
tf.zeros()
```
### 20. Creating tensors from NumPy arrays
None
### 21. Getting information from your tensors (tensor attributes)
[Doc: `tf.size()`](https://www.tensorflow.org/api_docs/python/tf/size)<br>
```python
tf.size()
```
### 22. Indexing and expanding tensors
Doc: `tf.newaxis()`
```python
tf.newaxis()
```
An alternative to `tf.newaxis()`:<br>
[Doc: `tf.expand_dims()`](https://www.tensorflow.org/api_docs/python/tf/expand_dims)<br>
```python
tf.expand_dims()
```
### 23. Manipulating tensors with basic operations
[Doc: `tf.math.multiply()` or `tf.multiply()`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)<br>
```python
tf.math.multiply()
tf.multiply()
```
[Doc: `tf.math.add()` or `tf.add()`]()<br>
```python
tf.math.add()
tf.add()
```
[Doc: `tf.math.subtract()` or `tf.subtract()`](https://www.tensorflow.org/api_docs/python/tf/math/subtract)<br>
```python
tf.math.subtract()
tf.subtract()
```
[Doc: `tf.math.divide()` or `tf.divide()`](https://www.tensorflow.org/api_docs/python/tf/math/divide)<br>
```python
tf.math.divide()
tf.divide()
```
### 24. Matrix multiplication with tensors part 1
[Doc: `tf.linalg.matmul()` or `tf.matmul()`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul)<br>
```python
tf.linalg.matmul()
tf.matmul()
```
### 25. Matrix multiplication with tensors part 2
[Doc: `tf.reshape()`](https://www.tensorflow.org/api_docs/python/tf/reshape)<br>
```python
tf.reshape()
```
[Doc: `tf.transpose()`](https://www.tensorflow.org/api_docs/python/tf/transpose)<br>
```python
tf.transpose()
```
### 26. Matrix multiplication with tensors part 3
[Doc: `tf.linalg.tensordot()` or `tf.tensordot()`](https://www.tensorflow.org/api_docs/python/tf/tensordot)<br>
```python
tf.linalg.tensordot()
tf.tensordot()
```
### 27. Changing the datatype of tensors
[Doc: `Mixed Precision`](https://www.tensorflow.org/guide/mixed_precision?hl=fr)<br>
```python
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import mixed_precision
```
[Doc: `tf.dtypes.cast()` or `tf.cast()`](https://www.tensorflow.org/api_docs/python/tf/cast)<br>
```python
tf.dtypes.cast()
tf.cast()
```
### 28. Tensor aggregation (finding the min, max, mean & more)
[Doc: `tf.math.abs()` or `tf.abs()`](https://www.tensorflow.org/api_docs/python/tf/math/abs)<br>
```python
tf.math.abs()
tf.abs()
```
[Doc: `tf.math.reduce_min()` or `tf.reduce_min()`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_min)<br>
```python
tf.math.reduce_min()
tf.reduce_min()
# NumPy compatibility
np.min()
```
[Doc: `tf.math.reduce_max()` or `tf.reduce_max()`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max)<br>
```python
tf.math.reduce_max()
tf.reduce_max()
# NumPy compatibility
np.max()
```
[Doc: `tf.math.reduce_mean()` or `tf.reduce_mean()`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean)<br>
```python
tf.math.reduce_mean()
tf.reduce_mean()
# NumPy compatibility
np.mean()
```
[Doc: `tf.math.reduce_sum()` or `tf.reduce_sum()`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_sum)<br>
```python
tf.math.reduce_sum()
tf.reduce_sum()
# NumPy compatibility
np.sum()
```
### 29. Tensor troubleshooting example (updating tensor datatypes)
[Doc: `tfp.stats.variance()`](https://www.tensorflow.org/probability/api_docs/python/tfp/stats/variance)<br>
```python
import tensorflow_probability as tfp
tfp.stats.variance()
```
[Doc: `tf.math.reduce_std()`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_std)<br>
```python
tf.math.reduce_std()
```
### 30. Finding the positional minimum and maximum of a tensor (argmin and argmax)
[Doc: `tf.math.argmax()` or `tf.argmax()`](https://www.tensorflow.org/api_docs/python/tf/math/argmax)<br>
```python
tf.math.argmax()
tf.argmax()
```
[Doc: `tf.math.argmin()` or `tf.argmin()`](https://www.tensorflow.org/api_docs/python/tf/math/argmin)<br>
```python
tf.math.argmin()
tf.argmin()
```
### 31. Squeezing a tensor (removing all 1-dimension axes)
[Doc: `tf.squeeze()`](https://www.tensorflow.org/api_docs/python/tf/squeeze)<br>
```python
tf.squeeze()
```
### 32. One-hot encoding tensors
