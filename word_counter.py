import json


def word_counter(notebook_path):
    """Count the number of words in a notebook."""
    with open(notebook_path) as f:
        nb = json.load(f)
    words = 0
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown' or cell['cell_type'] == 'code':
            words += len("".join(cell['source']).split())

    return words


if __name__ == '__main__':
    import sys

    print(word_counter(sys.argv[1]))
