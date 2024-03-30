# Equivalences between course functions and my personal functions
## 1.
```python
# Course function:
load_and_prep_image(filename, img_shape=224, scale=True)
# Personnal function:
from utils.data_visualization.prediction_visualization import prepare_image
prepare_image(file_path, img_shape=224, scale=True, channels=3)
```

## 2.
```python
# Course function:
make_confusion_matrix(y_true, y_pred, classes=None, figsize=(10, 10), text_size=15, norm=False, savefig=False)
# Personnal function:
from utils.data_visualization.evaluation_metrics import make_confusion_matrix
make_confusion_matrix(y_true, y_pred, classes=None, figsize=(5, 5), text_size=15, norm=False, savefig=False)
```

## 3.
```python
# Course function:
pred_and_plot(model, filename, class_names):
# Personnal function:
from utils.data_visualization.prediction_visualization import predict_and_display_image
predict_and_display_image(model, file_path, class_names)
```

## 4.
```python
# Course function:
create_tensorboard_callback(dir_name, experiment_name)
# Personnal function:
from utils.training_utilities.model_callbacks import create_tensorboard_callback
create_tensorboard_callback(dir_name, experiment_name, update_freq='epoch')
```

## 5.
```python
# Course function:
plot_loss_curves(history)
# Personnal function:
from utils.data_visualization.model_learning_curves import plot_loss_curves
plot_loss_curves(history)
```

## 6.
```python
# Course function:
compare_historys(original_history, new_history, initial_epochs=5)
# Personnal function:
from utils.data_visualization.model_learning_curves import compare_histories
compare_histories(original_history, new_history, initial_epochs=5)
```

## 7.
```python
# Course function:
unzip_data(filename)
# Personnal function:
from utils.data_acquisition.data_downloader import extract_archive_file
extract_archive_file(file_path, extract_to=None)
```

## 8.
```python
# Course function:
walk_through_dir(dir_path)
# Personnal function:
from utils.data_visualization.image_visualization import walk_through_dir
walk_through_dir(dir_path)
```

## 9.
```python
# Course function:
calculate_results(y_true, y_pred)
# Personnal function:
from utils.data_visualization.evaluation_metrics import evaluate_classification_metrics
evaluate_classification_metrics(y_true, y_pred)
```