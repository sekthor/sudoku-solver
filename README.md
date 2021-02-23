# Sudoku Solver

Simple Sudoku Solver written in python.
A fun little project I have wanted to do a while now.

## Usage

Import the module.

```python
from sudoku import *
```

A sudoku is constructed from a 9x9 list containing numbers from `1-9` or `0` for empty fields.

```python
s1 = [ 
        [6,0,9,4,0,0,0,3,0],
        [2,0,0,6,0,0,0,1,0],
        [0,4,0,0,0,2,0,7,0],
        [0,0,4,5,0,0,7,0,0],
        [7,0,0,8,0,9,0,0,6],
        [0,0,5,0,0,3,2,0,0],
        [0,1,0,2,0,0,0,6,0],
        [0,7,0,0,0,6,0,0,8],
        [0,9,0,0,0,4,5,0,3]
	]

sudoku = Sudoku(s1)
```

Instanciate SodukuSolver with Sudoku and call the solve method.

```python
solver = SudokuSolver(sudoku)
solver.solve()
```

