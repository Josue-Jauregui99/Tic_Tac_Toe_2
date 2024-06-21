

def check_sector_click(sectors, board, mouse_pos):
    for n in range(9):
        if sectors[n].collidepoint(mouse_pos) and board[n] == '':
            print('Sector clicked!')
            return n
    return None