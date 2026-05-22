import logic

mat = logic.start_game()

while True:
    for rows in mat:
        print(rows)
    
    x = input("Press a key (W/A/S/D): ")
    
    if x == 'w' or x == 'W':
        mat = logic.move_up(mat)
    elif x == 's' or x == 'S':
        mat = logic.move_down(mat)
    elif x == 'a' or x == 'A':
        mat = logic.move_left(mat)
    elif x == 'd' or x == 'D':
        mat = logic.move_right(mat)
    else:
        print("Invalid Key")
        
    check = logic.get_current_state(mat)
    if check == 'WON':
        print("You Win!")
        break
    elif check == 'LOST':
        print("Game Over!")
        break
    else:
        mat = logic.add_new_2(mat)