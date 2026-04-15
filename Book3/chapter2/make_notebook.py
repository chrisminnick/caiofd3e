import nbformat as nbf

OUTFILE = "chapter_02_working_with_data.ipynb"

nb = nbf.v4.new_notebook()
cells = []

def add_example(title, code):
    cells.append(nbf.v4.new_markdown_cell(f"## {title}"))
    cells.append(nbf.v4.new_code_cell(code.strip("\n")))

# --- NumPy: The Foundation of Data Science in Python ---

add_example(
    "Arrays vs. Lists",
    """import numpy as np

# Python list approach — requires a loop
values = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in values]

# NumPy approach — operates on the whole array at once
arr = np.array([1, 2, 3, 4, 5])
doubled = arr * 2
print(doubled)

# Output: [ 2  4  6  8 10]"""
)

add_example(
    "Creating NumPy Arrays",
    """import numpy as np

# 1-D array
temps = np.array([72.1, 68.4, 74.5, 70.2, 69.8])

# 2-D array (3 rows, 4 columns)
grid = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

print(grid.shape)   # (3, 4) — 3 rows, 4 columns
print(grid.dtype)   # int64 — all elements are integers
print(grid.size)    # 12 — total number of elements"""
)

add_example(
    "NumPy Array Creation Shortcuts",
    """np.zeros((3, 3))      # 3x3 array of zeros
np.ones((2, 5))       # 2x5 array of ones
np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)  # [0.0, 0.25, 0.5, 0.75, 1.0]"""
)

add_example(
    "Basic Array Math",
    """import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr.mean())  # 30.0
print(arr.sum())   # 150
print(arr.min())   # 10
print(arr.max())   # 50
print(arr.std())   # Standard deviation: 14.14..."""
)

# --- pandas: Working with Tabular Data ---

add_example(
    "Creating a DataFrame",
    """import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Carol', 'Dave'],
    'age': [25, 32, 28, 45],
    'score': [88.5, 92.0, 79.5, 85.0]
}

df = pd.DataFrame(data)
print(df)"""
)

# --- Validating Your Data ---

add_example(
    "Getting the Lay of the Land",
    """import pandas as pd

# Load the built-in Titanic dataset for these examples
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.shape)      # (891, 12) — 891 rows, 12 columns"""
)

nb.cells = cells
with open(OUTFILE, 'w') as f:
    nbf.write(nb, f)
