import time
import Kamisado_S0 as S0
import inscription as ins

class Board:
    def __init__(self):
        self.board = S0.BOARD          # Plateau 8x8 avec couleurs de cases
        self.piece_positions = {}      # Dictionnaire pour accès rapide aux tours
        self.current_player = 1        # 1 pour Blanc, -1 pour Noir
        self.active_color = None       # La couleur de tour imposée au joueur actuel
        self.move_history = []         # Pour l'undo_move

    def get_tile_color(self):
        if ins.request.get("request") == "play":
            state = ins.request.get('state')
            self.active_color = self.board[state]
        return self.active_color

    def get_legal_moves(self):
        """Retourne les coups possibles pour la tour de couleur self.active_color"""
        # Logique : trouver la tour, vérifier les cases libres devant elle

    def make_move(self, move):
    # 1. Sauvegarder l'état actuel avant modification
        state = {
                'active_color': self.active_color,
                'last_move': move,
                'player': self.current_player
                }
        self.history.append(state)

        # 2. Déplacer la tour dans votre structure de données
        origin, destination = move
        piece = self.board_dict[origin]
        self.board_dict[destination] = piece
        del self.board_dict[origin]

        # 3. Déterminer la prochaine couleur active
        # La couleur de la case d'arrivée impose la tour de l'adversaire
        dest_row, dest_col = destination
        self.active_color = self.board[dest_row][dest_col]
    
        # 4. Changer de joueur
        self.current_player *= -1

    def undo_move(self):
        if not self.history: return
    
        prev_state = self.history.pop()
        move = prev_state['last_move']
        origin, destination = move
    
        # Replacer la pièce
        piece = self.board_dict[destination]
        self.board_dict[origin] = piece
        del self.board_dict[destination]
    
        # Restaurer l'état
        self.active_color = prev_state['active_color']
        self.current_player = prev_state['player']

    def get_distance_to_goal(self, piece):
        """Utile pour l'heuristique"""
        # Retourne le nombre de cases séparant la tour de la ligne de fond adverse
        pass

def evaluate_board(board, color_to_move):
    """
    Heuristique relative : un score positif est bon pour color_to_move.
    """
    score = 0
    opponent = board.get_opponent(color_to_move)

    # 1. Vérification de victoire immédiate
    if board.is_winner(color_to_move): return 99999
    if board.is_winner(opponent): return -99999

    for color in [color_to_move, opponent]:
        multiplier = 1 if color == color_to_move else -1
        
        # Récupération de la tour active pour ce joueur
        tower = board.get_active_tower(color)
        
        # A. Progression (Poids: 20)
        # On favorise les tours proches de la ligne adverse
        dist = board.get_distance_to_goal(tower)
        score += multiplier * (7 - dist) * 20

        # B. Mobilité (Poids: 5)
        # Plus une tour a d'options, plus elle est dangereuse
        moves = board.get_legal_moves(tower)
        score += multiplier * len(moves) * 5

        # C. Danger de blocage (Deadlock)
        # Si la tour n'a aucun mouvement, c'est un malus énorme
        if len(moves) == 0:
            score -= multiplier * 100

    return score

def negamax(board, depth, alpha, beta, color):
    # 1. Cas de base
    if depth == 0 or board.is_game_over():
        # On multiplie par 'color' pour que l'évaluation soit 
        # toujours du point de vue du joueur actuel
        return color * evaluate_board(board, board.current_player)

    # 2. Tri des coups (Move Ordering) pour optimiser le pruning
    moves = board.get_legal_moves()
    # Astuce : Trier les coups par progression pour couper l'arbre plus vite
    moves.sort(key=lambda m: board.preview_distance(m), reverse=True)

    max_eval = -float('inf')

    for move in moves:
        board.make_move(move)
        
        # Appel récursif : on inverse les rôles et les bornes alpha/beta
        eval = -negamax(board, depth - 1, -beta, -alpha, -color)
        
        board.undo_move()

        max_eval = max(max_eval, eval)
        alpha = max(alpha, eval)
        
        # Coupure Alpha-Beta
        if alpha >= beta:
            break
            
    return max_eval