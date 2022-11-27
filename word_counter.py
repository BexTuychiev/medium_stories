import nbformat
import re


# Create a function to count the words in a Jupyter Notebook
def word_count(notebook_path):
    """
    Count the words in a Jupyter Notebook.
    """

    # Read the notebook
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    # Count the words
    words = 0
    for cell in nb.cells:
        if cell.cell_type == 'markdown' or cell.cell_type == 'code':
            words += len(re.findall(r'\w+', cell.source))
    return words


if __name__ == '__main__':
    import sys

    print(word_count(sys.argv[1]))
