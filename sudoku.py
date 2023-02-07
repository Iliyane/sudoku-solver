#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python program to solve sudoku with command line tool
#for validating a standard 9x9 Sudoku puzzle
# by Iliyana Kamenova


#Creating the sudoku puzzle

# creating a 2d array and empty boxes are represented as 0
sudoku=[[9,0,4,0,6,0,7,0,1],[0,2,3,4,0,3,0,8,0],[8,0,0,0,0,0,0,0,4],[0,0,1,8,4,9,6,0,0],[0,0,0,0,0,0,0,0,0],[0,0,3,2,5,7,9,0,0],[4,0,0,0,0,0,0,0,7],[0,8,0,6,0,4,0,5,0],[5,0,6,0,8,0,2,0,3]]
#sudoku=[[8,1,0,0,3,0,0,2,7],[0,6,2,0,5,0,0,9,0],[0,7,0,0,0,0,0,0,0],[0,9,0,6,0,0,1,0,0],[1,0,0,0,2,0,0,0,4],[0,0,8,0,0,5,0,7,0],[0,0,0,0,0,0,0,8,0],[0,2,0,0,1,0,7,5,0],[3,8,0,0,7,0,0,4,2]]
def mysudoku(): # creating sudoku
    print ("\n\n\n\n\n")
    for i in range(len(sudoku)): # for every i row
        line=""
        if i ==3 or i==6:
            print ("""----------------------""")
        for j in range (len(sudoku[i])): # for every j-column
            if j ==3 or j==6:
                line+="| "
            line+=str(sudoku[i][j])+" "
        print (line)

# 2) Next step is to create a function that solves the cells

def solve_cell(sudoku): # this function find every row and column number of every empty cell
    for x in range(9):
        for y in range (9): # iterates in the first row, then in the second ...
            if sudoku[x][y]==0:
                return x,y
    return -1, -1

# 3) Validating by entry

def validation(sudoku,i,j,e): # creating a function of an entry e, if its violate the tree main rules
    row=all([e != sudoku[i][x] for x in range(9)]) # if there are not repeating numbers in the i row
    if row: # it checks if there is no repeating number
        column=all([e != sudoku[x][j] for x in range(9)]) # when placed in j-column
        if column: # if there is no repeating number in j column
            numberX,numberY=3*(i//3), 3*(j//3) # when placed in i column
            for x in range(numberX,numberX+3):
                for y in range(numberY,numberY+3):
                    if sudoku[x][y]==e: # if both row and column are true then the lines 6-10 check if the entry fits a certain block
                        return False
            return True # if none of the  3 rules are violated
        return False # otherwise false

# 4) Solving the puzzle

def sudoku_solve(sudoku, i=0, j=0):
    i,j=solve_cell(sudoku)#  the first 3 lines make sure that there is an empty cell
    if i ==-1: # and if it is equal to -1 then is completed
        return True
    for e in range(1,10):
        if validation(sudoku,i,j,e):
            sudoku[i][j]=e
            if sudoku_solve(sudoku,i,j): # if there is an empty cell in i-row andf j-column, it tries to fill all possibles entries from 1-9 into the box
                return True, "Valid: there is solution :-) " # solves under the assumption is valid
            sudoku[i][j]=0 # if not valid it will fill the 0
    return False, 'Invalid: There is no solution'

#call of the functions
print (sudoku_solve(sudoku))
mysudoku()
