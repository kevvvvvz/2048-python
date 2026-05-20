import random
import sys

def start_game():
    
    mat = []
    for i in range(4):
        mat.append([0] * 4)

    r = random.randint(0, 3)
    c = random.randint(0, 3)
    mat[r][c] = 2
    
    #for rows in mat:
        #print(rows)
    return mat

def add_new_2(mat):
    while True:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        if mat[r][c] == 0:
            mat[r][c] = 2
            #for rows in mat:
                #print(rows)
            break
    return mat
    
    
def compress(mat):
    
    new_mat = []
    for row in mat:
        new_row = []
        for num in row:
            if num != 0:
                new_row.append(num)
        while len(new_row) < 4:
            new_row.append(0)
        new_mat.append(new_row)
        
    return new_mat
    #for rows in new_mat:
        #print(rows)
   
    
def merge(mat):
    for rows in mat:
        for i in range(0, 3):
            if rows[i] == rows[i+1]:
                new = rows[i] * 2
                rows[i] = new
                rows[i+1] = 0

    #for rows in mat:
        #print(rows)
    
    return mat
    
def move_left(mat):
    mat = compress(mat)
    mat = merge(mat)
    mat = compress(mat)
    
    #for rows in mat:
        #print(rows)
    
    return mat
    
    
def reverse():
    ...
    
    
def transpose():
    ...
    
    
def main():
    mat = start_game()
    mat = add_new_2(mat)
    move_left(mat)
    
main()