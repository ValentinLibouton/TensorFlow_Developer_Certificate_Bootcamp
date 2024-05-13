import nbformat
file_path="10_time_series_forecasting_with_tensorflow/10.1_time_series_forecasting_with_tensorflow_video.ipynb"
# Charger le notebook
with open(file_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Parcourir toutes les cellules et ajouter 'execution_count' si manquant
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        if 'execution_count' not in cell:
            cell['execution_count'] = None

# Sauvegarder les modifications
with open(file_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
