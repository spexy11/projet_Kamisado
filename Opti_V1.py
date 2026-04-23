import Kamisado_S0 as S0

class Board:
    def __init__(self):
        # S0.BOARD doit être une matrice 8x8 des couleurs de cases
        self.board_colors = S0.BOARD           
        self.current_player = 1        # 1 pour Blanc, -1 pour Noir
        self.active_color = None       # Couleur de la tour imposée
        self.move_history = []         
        
        # Initialisation des positions des pièces
        # (Joueur, Couleur): (ligne, colonne)
        self.piece_positions = self._setup_pieces()
        self.occupied_positions = set(self.piece_positions.values())

    def _setup_pieces(self):
        # Configuration initiale standard du Kamisado
        # Blancs en ligne 0, Noirs en ligne 7
        pos = {}
        for col in range(8):
            color = self.board_colors[0][col]
            pos[(1, color)] = (0, col)
            color_noir = self.board_colors[7][col]
            pos[(-1, color_noir)] = (7, col)
        return pos

    def get_directions(self, player):
        # Blanc (1) descend (vers 7), Noir (-1) monte (vers 0)
        return [(1, 0), (1, 1), (1, -1)] if player == 1 else [(-1, 0), (-1, 1), (-1, -1)]

    def get_legal_moves_for_tower(self, current_pos, player):
        moves = []
        r, c = current_pos
        for dr, dc in self.get_directions(player):
            for dist in range(1, 8):
                nr, nc = r + dr * dist, c + dc * dist
                if 0 <= nr < 8 and 0 <= nc < 8:
                    if (nr, nc) in self.occupied_positions:
                        break
                    moves.append((nr, nc))
                else:
                    break
        return moves

    def get_legal_moves(self):
        # Au premier tour, le blanc choisit n'importe quelle tour
        if self.active_color is None:
            all_moves = []
            for color in range(8):
                pos = self.piece_positions[(self.current_player, color)]
                all_moves.extend([(pos, m) for m in self.get_legal_moves_for_tower(pos, self.current_player)])
            return all_moves
        
        pos = self.piece_positions[(self.current_player, self.active_color)]
        raw_moves = self.get_legal_moves_for_tower(pos, self.current_player)
        return [(pos, m) for m in raw_moves]

    def make_move(self, move):
        origin, dest = move
        # Sauvegarde pour undo
        state = (self.active_color, self.current_player, origin, dest)
        self.move_history.append(state)

        # Trouver quelle pièce est à l'origine
        for (p, c), pos in self.piece_positions.items():
            if pos == origin:
                target_piece = (p, c)
                break
        
        # Mise à jour
        self.piece_positions[target_piece] = dest
        self.occupied_positions.remove(origin)
        self.occupied_positions.add(dest)
        
        # Prochaine couleur active = couleur de la case d'arrivée
        self.active_color = self.board_colors[dest[0]][dest[1]]
        self.current_player *= -1

    def undo_move(self):
        if not self.move_history: return
        act_col, prev_player, origin, dest = self.move_history.pop()
        
        # Trouver la pièce à déplacer en arrière
        for (p, c), pos in self.piece_positions.items():
            if pos == dest:
                target_piece = (p, c)
                break
        
        self.piece_positions[target_piece] = origin
        self.occupied_positions.remove(dest)
        self.occupied_positions.add(origin)
        
        self.active_color = act_col
        self.current_player = prev_player

    def is_winner(self, player):
        goal_row = 7 if player == 1 else 0
        for (p, c), pos in self.piece_positions.items():
            if p == player and pos[0] == goal_row:
                return True
        return False

    def is_game_over(self):
        return self.is_winner(1) or self.is_winner(-1) or len(self.get_legal_moves()) == 0

    def get_distance_to_goal(self, player, color):
        pos = self.piece_positions[(player, color)]
        return abs((7 if player == 1 else 0) - pos[0])

    def preview_distance(self, move):
        # Utilisé pour le tri des coups (Move Ordering)
        return abs((7 if self.current_player == 1 else 0) - move[1][0])

# --- Fonctions de l'IA ---

def evaluate_board(board):
    if board.is_winner(1): return 10000
    if board.is_winner(-1): return -10000
    
    score = 0
    for p, c in board.piece_positions.keys():
        mult = 1 if p == 1 else -1
        # Progression
        dist = board.get_distance_to_goal(p, c)
        score += mult * (7 - dist) * 10
        # Mobilité
        pos = board.piece_positions[(p, c)]
        moves = board.get_legal_moves_for_tower(pos, p)
        score += mult * len(moves) * 2
    
    return score

def negamax(board, depth, alpha, beta, color):
    if depth == 0 or board.is_game_over():
        return color * evaluate_board(board)

    moves = board.get_legal_moves()
    # Tri des coups : on teste les plus profonds d'abord
    moves.sort(key=lambda m: board.preview_distance(m), reverse=True)

    max_eval = -float('inf')
    for move in moves:
        board.make_move(move)
        eval = -negamax(board, depth - 1, -beta, -alpha, -color)
        board.undo_move()
        
        max_eval = max(max_eval, eval)
        alpha = max(alpha, eval)
        if alpha >= beta:
            break
    return max_eval

def get_best_move(board, depth):
    best_move = None
    max_val = -float('inf')
    alpha = -float('inf')
    beta = float('inf')
    
    for move in board.get_legal_moves():
        board.make_move(move)
        val = -negamax(board, depth - 1, -beta, -alpha, -board.current_player)
        board.undo_move()
        if val > max_val:
            max_val = val
            best_move = move
    return best_move