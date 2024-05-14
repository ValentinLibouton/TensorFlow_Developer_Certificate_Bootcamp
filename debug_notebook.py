import nbformat

class NotebookEditor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notebook = self.open_notebook(file_path)

    def open_notebook(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
        return notebook

    def save_notebook(self, file_path=None):
        if file_path is None:
            file_path = self.file_path
        with open(file_path, 'w', encoding='utf-8') as f:
            nbformat.write(self.notebook, f)

    def add_cell_code(self, content=""):
        new_cell = nbformat.v4.new_code_cell(source=content)
        self.notebook['cells'].append(new_cell)

    def add_cell_markdown(self, content=""):
        new_cell = nbformat.v4.new_markdown_cell(source=content)
        self.notebook['cells'].append(new_cell)

if __name__ == "__main__":
    # Initialiser l'éditeur de notebook avec le chemin du fichier
    nb_editor = NotebookEditor(file_path="10_time_series_forecasting_with_tensorflow/Template_Empty.ipynb")

    # Ajouter une cellule de code
    nb_editor.add_cell_code()

    # Ajouter une cellule Markdown
    nb_editor.add_cell_markdown()

    # Sauvegarder le notebook modifié
    nb_editor.save_notebook()
