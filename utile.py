board = []
player = 0
color = ""

def parse_board(state) :
    board = state["board"]
    player = state["current"]
    color = state["color"]

    return board, player, color

def get_pion_position(board,player, color):
    if player == 0:
        player = "light"
    else : player = "dark"
    pos = board[[1],[color, player]]
    
def get_legal_moves(board, player, color):
    pass

def is_move_legal(board, player, from_pos, to_pos):
    pass

def get_next_color(board, to_pos):
    pass

def is_winning(board, player):
    pass