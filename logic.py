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
    #print(mat)
    
    new_mat = []
    for row in mat:
        new_row = []
        for num in row:
            if num != 0:
                new_row.append(num)
        while len(new_row) < 4:
            new_row.append(0)
        new_mat.append(new_row)
        
    #print(new_row)
    for rows in new_mat:
        print(rows)
   
    
    
def merge():
    ...
    
    
def move_left():
    ...
    
    
def reverse():
    ...
    
    
def transpose():
    ...
    
    
def main():
    mat = start_game()
    mat = add_new_2(mat)
    compress(mat)
    
main()