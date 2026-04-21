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