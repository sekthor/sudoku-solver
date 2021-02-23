#!/usr/bin/env python3

import math

class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self._validate()

    def _validate(self):
        if len(self.sudoku) != 9:
            raise Exception("wrong sudoku format: 9x9 list required")

        for line in self.sudoku:
            if len(line) != 9:
                raise Exception("wrong sudoku format: 9x9 list required")
        return

    def get(self, x, y):
        return self.sudoku[x][y]

    def set(self, x, y, value):
        self.sudoku[x][y] = value

    def get_row(self, x):
        return self.sudoku[x]

    def get_col(self, y):
        col = []

        for row in self.sudoku:
            col.append(row[y])
        return col

    # returns all value form the square the given coordinates are in
    def get_sqr(self, x, y):
        sqr = []
        top_x = 3 * math.floor(x / 3)
        top_y = 3 * math.floor(y / 3)

        for i in range(0,3):
            for j in range(0,3):
                sqr.append(self.sudoku[top_x + i][top_y + j])
        return sqr

    def __str__(self):
        s = "+-------+-------+-------+\n"
        for i in range(0,9):
            s += "| "
            for j in range(0,9):
                s += str(self.sudoku[i][j]) + " "
                if (j+1) % 3 == 0:
                    s += "| "
            s += "\n"
            if (i+1) % 3 == 0:
                s += "+-------+-------+-------+\n"
        return s

class SudokuSolver:

    digits = [x for x in range(1,10)]

    def __init__(self, sudoku):
        if not isinstance(sudoku, Sudoku):
            raise Exception("Type Error: Sudoku expected")
        self.sudoku = sudoku

    def solve(self):
        self.log = []

        while not self.is_solved():
            for x in range(0,9):
                for y in range(0,9):
                    self.solve_field(x, y)

    def add_log(self, x, y, value):
        self.log.append((x,y,value))

    def col_possibilities(self, x, y):
        possibilities = []
        col = self.sudoku.get_col(y)

        for digit in self.digits:
            if digit not in col:
                possibilities.append(digit)
        return possibilities

    def row_possibilities(self, x, y):
        possibilities = []
        row = self.sudoku.get_row(x)

        for digit in self.digits:
            if digit not in row:
                possibilities.append(digit)
        return possibilities
        
    def sqr_possibilities(self, x, y):
        possibilities = []
        sqr = self.sudoku.get_sqr(x, y)

        for digit in self.digits:
            if digit not in sqr:
                possibilities.append(digit)
        return possibilities
        
    def possibilities(self, x, y):
        row = self.row_possibilities(x, y)
        col = self.col_possibilities(x, y)
        sqr = self.sqr_possibilities(x, y)

        return set(row) & set(col) & set(sqr)

    def solve_field(self, x, y):
        if self.sudoku.get(x, y) in self.digits:
            return

        pos = list(self.possibilities(x, y))
        if len(pos) == 1:
            value = pos[0]
            self.add_log(x, y, value)
            self.sudoku.set(x, y, value)

    # checks if every cell has been solved
    def is_solved(self):
        for row in self.sudoku.sudoku:
            for digit in row:
                if digit not in self.digits:
                    return False
        return True

