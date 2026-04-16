def get_moves(board, r, c, camp):

    moves = []
    direction = 1 if camp == "light" else -1

    vectors = [
        (direction, 0),
        (direction, -1),
        (direction, +1),
    ]

    for dr, dc in vectors:
        for i in range(1, 8):
            new_r = r + dr * i
            new_c = c + dc * i

            if not (0 <= new_r <= 7 and 0 <= new_c <= 7):
                break

            if board[new_r][new_c][1] is not None:
                break

            dest_color = board[new_r][new_c][0]
            moves.append((new_r, new_c, dest_color))

    return moves


def evaluation_kamisado(etat, mon_index):
    board = etat["board"]
    mon_camp = "light" if mon_index == 0 else "dark"

    score = 0

    W_PROGRESSION = 20
    W_MOBILITY = 5
    W_BLOCK = 150
    W_WIN_THREAT = 800
    W_WIN_ACHIEVED = 10000

    for r in range(8):
        for c in range(8):
            piece = board[r][c][1]
            if piece is None:
                continue

            p_color, p_camp = piece
            dist_parcourue = r if p_camp == "light" else 7 - r
            valeur_piece = dist_parcourue * W_PROGRESSION

            if (p_camp == "light" and r == 7) or (p_camp == "dark" and r == 0):
                valeur_piece += W_WIN_ACHIEVED
            else:
                moves = get_moves(board, r, c, p_camp)
                nb_moves = len(moves)

                if nb_moves == 0:
                    valeur_piece -= W_BLOCK
                else:
                    valeur_piece += nb_moves * W_MOBILITY
                    for move_r, _ in moves:
                        if (p_camp == "light" and move_r == 7) or (
                            p_camp == "dark" and move_r == 0
                        ):
                            valeur_piece += W_WIN_THREAT
                            break

            score += valeur_piece if p_camp == mon_camp else -valeur_piece

    if etat["current"] == mon_index and etat["color"] is not None:
        ma_piece_coincee = True
        found = False
        for r in range(8):
            for c in range(8):
                p = board[r][c][1]
                if p and p[1] == mon_camp and p[0] == etat["color"]:
                    if len(get_moves(board, r, c, mon_camp)) > 0:
                        ma_piece_coincee = False
                    found = True
                    break
            if found:
                break

        if ma_piece_coincee:
            score -= 500

    return score
