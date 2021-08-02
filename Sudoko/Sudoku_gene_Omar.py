# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:02:06 2021

@author: USER
"""

  
import numpy as np


def generate_sudoku(mask_rate=0.5):
    while True:
        n = 9
        m = np.zeros((n, n), np.int)
        rg = np.arange(1, n + 1)
        m[0, :] = np.random.choice(rg, n, replace=False)
        try:
            for r in range(1, n):
                for c in range(n):
                    col_rest = np.setdiff1d(rg, m[:r, c])
                    row_rest = np.setdiff1d(rg, m[r, :c])
                    avb1 = np.intersect1d(col_rest, row_rest)
                    sub_r, sub_c = r//3, c//3
                    avb2 = np.setdiff1d(np.arange(0, n+1), m[sub_r*3:(sub_r+1)*3, sub_c*3:(sub_c+1)*3].ravel())
                    avb = np.intersect1d(avb1, avb2)
                    m[r, c] = np.random.choice(avb, size=1)
            break
        except ValueError:
            pass
    mm = m.copy()
    mm[np.random.choice([True, False], size=m.shape, p=[mask_rate, 1 - mask_rate])] = 0
    print("\nMasked anwser:\n", mm)
#   print("Solved_Sudoku:\n", m)    
    return mm
    
generated_sudoku = [np.array(generate_sudoku(mask_rate=0.7))]