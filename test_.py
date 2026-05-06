import utile
import copy
import evaluation
import AI
import pytest

state2 = {
    "players": ["Les Infernales", "ilyes et benoit contre le reste du monde "],
    "current": 1,
    "color": "orange",
    "board": [
        [
            ["orange", ["pink", "light"]],
            ["blue", ["orange", "light"]],
            ["purple", ["green", "light"]],
            ["pink", ["red", "light"]],
            ["yellow", ["purple", "light"]],
            ["red", ["blue", "light"]],
            ["green", ["brown", "light"]],
            ["brown", ["yellow", "light"]],
        ],
        [
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
        ],
        [
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
        ],
        [
            ["pink", None],
            ["purple", None],
            ["blue", None],
            ["orange", None],
            ["brown", None],
            ["green", None],
            ["red", None],
            ["yellow", None],
        ],
        [
            ["yellow", None],
            ["red", None],
            ["green", None],
            ["brown", None],
            ["orange", None],
            ["blue", None],
            ["purple", None],
            ["pink", None],
        ],
        [
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
        ],
        [
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
        ],
        [
            ["brown", ["yellow", "dark"]],
            ["green", ["green", "dark"]],
            ["red", ["orange", "dark"]],
            ["yellow", ["purple", "dark"]],
            ["pink", ["red", "dark"]],
            ["purple", ["brown", "dark"]],
            ["blue", ["blue", "dark"]],
            ["orange", ["pink", "dark"]],
        ],
    ],
}
state = {
    "players": ["Les Infernales", "ilyes et benoit contre le reste du monde "],
    "current": 1,
    "color": "orange",
    "board": [
        [
            ["orange", ["green", "light"]],
            ["blue", ["red", "light"]],
            ["purple", ["pink", "dark"]],
            ["pink", ["orange", "light"]],
            ["yellow", ["brown", "light"]],
            ["red", ["yellow", "light"]],
            ["green", ["purple", "light"]],
            ["brown", ["blue", "light"]],
        ],
        [
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
        ],
        [
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
        ],
        [
            ["pink", None],
            ["purple", None],
            ["blue", None],
            ["orange", None],
            ["brown", None],
            ["green", None],
            ["red", None],
            ["yellow", None],
        ],
        [
            ["yellow", None],
            ["red", None],
            ["green", ["pink", "light"]],
            ["brown", None],
            ["orange", ["brown", "dark"]],
            ["blue", None],
            ["purple", None],
            ["pink", None],
        ],
        [
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
        ],
        [
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
        ],
        [
            ["brown", ["green", "dark"]],
            ["green", None],
            ["red", ["red", "dark"]],
            ["yellow", ["orange", "dark"]],
            ["pink", None],
            ["purple", ["purple", "dark"]],
            ["blue", ["yellow", "dark"]],
            ["orange", ["blue", "dark"]],
        ],
    ],
}
board = utile.copy_board(state)
player = copy.deepcopy(state["current"])
color = copy.deepcopy(state["color"])

state3 = {
    "players": ["Les Infernales", "ilyes et benoit contre le reste du monde "],
    "current": 0,
    "color": "red",
    "board": [
        [
            ["orange", None],
            ["blue", ["orange", "light"]],
            ["purple", ["green", "light"]],
            ["pink", ["red", "light"]],
            ["yellow", ["purple", "light"]],
            ["red", ["blue", "light"]],
            ["green", ["brown", "light"]],
            ["brown", ["yellow", "light"]],
        ],
        [
            ["red", ["pink", "light"]],
            ["orange", None],
            ["pink", None],
            ["green", None],
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
        ],
        [
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
        ],
        [
            ["pink", None],
            ["purple", None],
            ["blue", None],
            ["orange", None],
            ["brown", None],
            ["green", None],
            ["red", None],
            ["yellow", None],
        ],
        [
            ["yellow", None],
            ["red", None],
            ["green", None],
            ["brown", None],
            ["orange", None],
            ["blue", None],
            ["purple", None],
            ["pink", None],
        ],
        [
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
        ],
        [
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
        ],
        [
            ["brown", ["yellow", "dark"]],
            ["green", ["green", "dark"]],
            ["red", ["orange", "dark"]],
            ["yellow", ["purple", "dark"]],
            ["pink", ["red", "dark"]],
            ["purple", ["brown", "dark"]],
            ["blue", ["blue", "dark"]],
            ["orange", ["pink", "dark"]],
        ],
    ],
}


def test_copy_board():
    assert utile.copy_board(state) == [
        [
            ["orange", ["green", "light"]],
            ["blue", ["red", "light"]],
            ["purple", ["pink", "dark"]],
            ["pink", ["orange", "light"]],
            ["yellow", ["brown", "light"]],
            ["red", ["yellow", "light"]],
            ["green", ["purple", "light"]],
            ["brown", ["blue", "light"]],
        ],
        [
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
        ],
        [
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
        ],
        [
            ["pink", None],
            ["purple", None],
            ["blue", None],
            ["orange", None],
            ["brown", None],
            ["green", None],
            ["red", None],
            ["yellow", None],
        ],
        [
            ["yellow", None],
            ["red", None],
            ["green", ["pink", "light"]],
            ["brown", None],
            ["orange", ["brown", "dark"]],
            ["blue", None],
            ["purple", None],
            ["pink", None],
        ],
        [
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
        ],
        [
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
        ],
        [
            ["brown", ["green", "dark"]],
            ["green", None],
            ["red", ["red", "dark"]],
            ["yellow", ["orange", "dark"]],
            ["pink", None],
            ["purple", ["purple", "dark"]],
            ["blue", ["yellow", "dark"]],
            ["orange", ["blue", "dark"]],
        ],
    ]


def test_eval1():
    assert evaluation.evaluation_kamisado(state, 0) == -498225


def test_eval2():
    assert evaluation.evaluation_kamisado(state, 0) == evaluation.evaluation_kamisado(
        state, 1
    )


def test_gameOver():
    assert utile.gameOver(state)


def test_get_pos():
    assert utile.get_pos(board, player, color) == [0, 3]


def test_get_legal_moves():
    assert utile.get_legal_moves(state2["board"], 0, 7, 4, "red") == [
        (6, 3, "blue"),
        (6, 4, "green"),
        (6, 5, "pink"),
        (5, 2, "brown"),
        (5, 4, "red"),
        (5, 6, "pink"),
        (4, 1, "red"),
        (4, 4, "orange"),
        (4, 7, "pink"),
        (3, 0, "pink"),
        (3, 4, "brown"),
        (2, 4, "purple"),
        (1, 4, "blue"),
    ]


def test_aplly():
    starting_l, starting_c = 0, 0
    player = 1
    move = 1, 0, "red"
    assert utile.apply(state2, starting_l, starting_c, player, move) == state3


def test_TimeOutError():
    with pytest.raises(TimeoutError, match="Exception"):
        raise TimeoutError(Exception)


def test_board_to_key():
    assert AI.board_to_key(state3["board"]) == (
        (
            ("orange", None),
            ("blue", ("orange", "light")),
            ("purple", ("green", "light")),
            ("pink", ("red", "light")),
            ("yellow", ("purple", "light")),
            ("red", ("blue", "light")),
            ("green", ("brown", "light")),
            ("brown", ("yellow", "light")),
        ),
        (
            ("red", ("pink", "light")),
            ("orange", None),
            ("pink", None),
            ("green", None),
            ("blue", None),
            ("yellow", None),
            ("brown", None),
            ("purple", None),
        ),
        (
            ("green", None),
            ("pink", None),
            ("orange", None),
            ("red", None),
            ("purple", None),
            ("brown", None),
            ("yellow", None),
            ("blue", None),
        ),
        (
            ("pink", None),
            ("purple", None),
            ("blue", None),
            ("orange", None),
            ("brown", None),
            ("green", None),
            ("red", None),
            ("yellow", None),
        ),
        (
            ("yellow", None),
            ("red", None),
            ("green", None),
            ("brown", None),
            ("orange", None),
            ("blue", None),
            ("purple", None),
            ("pink", None),
        ),
        (
            ("blue", None),
            ("yellow", None),
            ("brown", None),
            ("purple", None),
            ("red", None),
            ("orange", None),
            ("pink", None),
            ("green", None),
        ),
        (
            ("purple", None),
            ("brown", None),
            ("yellow", None),
            ("blue", None),
            ("green", None),
            ("pink", None),
            ("orange", None),
            ("red", None),
        ),
        (
            ("brown", ("yellow", "dark")),
            ("green", ("green", "dark")),
            ("red", ("orange", "dark")),
            ("yellow", ("purple", "dark")),
            ("pink", ("red", "dark")),
            ("purple", ("brown", "dark")),
            ("blue", ("blue", "dark")),
            ("orange", ("pink", "dark")),
        ),
    )


def test_state_to_key():
    assert AI.state_to_key(state3) == (
        (
            (
                ("orange", None),
                ("blue", ("orange", "light")),
                ("purple", ("green", "light")),
                ("pink", ("red", "light")),
                ("yellow", ("purple", "light")),
                ("red", ("blue", "light")),
                ("green", ("brown", "light")),
                ("brown", ("yellow", "light")),
            ),
            (
                ("red", ("pink", "light")),
                ("orange", None),
                ("pink", None),
                ("green", None),
                ("blue", None),
                ("yellow", None),
                ("brown", None),
                ("purple", None),
            ),
            (
                ("green", None),
                ("pink", None),
                ("orange", None),
                ("red", None),
                ("purple", None),
                ("brown", None),
                ("yellow", None),
                ("blue", None),
            ),
            (
                ("pink", None),
                ("purple", None),
                ("blue", None),
                ("orange", None),
                ("brown", None),
                ("green", None),
                ("red", None),
                ("yellow", None),
            ),
            (
                ("yellow", None),
                ("red", None),
                ("green", None),
                ("brown", None),
                ("orange", None),
                ("blue", None),
                ("purple", None),
                ("pink", None),
            ),
            (
                ("blue", None),
                ("yellow", None),
                ("brown", None),
                ("purple", None),
                ("red", None),
                ("orange", None),
                ("pink", None),
                ("green", None),
            ),
            (
                ("purple", None),
                ("brown", None),
                ("yellow", None),
                ("blue", None),
                ("green", None),
                ("pink", None),
                ("orange", None),
                ("red", None),
            ),
            (
                ("brown", ("yellow", "dark")),
                ("green", ("green", "dark")),
                ("red", ("orange", "dark")),
                ("yellow", ("purple", "dark")),
                ("pink", ("red", "dark")),
                ("purple", ("brown", "dark")),
                ("blue", ("blue", "dark")),
                ("orange", ("pink", "dark")),
            ),
        ),
        0,
        "red",
    )


def test_AI():
    assert AI.negamaxWithPruningIterativeDeepening(state3, state3["current"]) == (
        2590,
        [[7, 4], [1, 4]],
    )


def test_send_json():
    pass


def test_simulation_serveur_bloquage_total():
    board = [
        [
            ["orange", ["pink", "light"]],
            ["blue", None],
            ["purple", None],
            ["pink", None],
            ["yellow", ["purple", "light"]],
            ["red", ["blue", "light"]],
            ["green", ["brown", "light"]],
            ["brown", ["yellow", "light"]],
        ],
        [
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
        ],
        [
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
            ["purple", None],
            ["brown", None],
            ["yellow", None],
            ["blue", None],
        ],
        [
            ["pink", None],
            ["purple", None],
            ["blue", None],
            ["orange", None],
            ["brown", None],
            ["green", None],
            ["red", None],
            ["yellow", None],
        ],
        [
            ["yellow", None],
            ["red", None],
            ["green", None],
            ["brown", None],
            ["orange", None],
            ["blue", None],
            ["purple", None],
            ["pink", None],
        ],
        [
            ["blue", None],
            ["yellow", None],
            ["brown", None],
            ["purple", None],
            ["red", None],
            ["orange", None],
            ["pink", None],
            ["green", None],
        ],
        [
            ["purple", None],
            ["brown", ["green", "light"]],
            ["yellow", ["orange", "light"]],
            ["blue", ["red", "light"]],
            ["green", None],
            ["pink", None],
            ["orange", None],
            ["red", None],
        ],
        [
            ["brown", ["yellow", "dark"]],
            ["green", ["green", "dark"]],
            ["red", ["orange", "dark"]],
            ["yellow", ["purple", "dark"]],
            ["pink", ["red", "dark"]],
            ["purple", ["brown", "dark"]],
            ["blue", ["blue", "dark"]],
            ["orange", ["pink", "dark"]],
        ],
    ]

    state_prison = {
        "players": ["Adversaire", "Mon IA"],
        "current": 1,
        "color": "orange",
        "board": board,
    }

    player = state_prison["current"]
    color = state_prison["color"]

    _, best_move = AI.negamaxWithPruningIterativeDeepening(state_prison, player)

    if best_move is None:
        pos = utile.get_pos(state_prison["board"], player, color)
        best_move = [pos, pos]
    print(f"Position trouvée pour orange : {pos}")
    print(f"Mouvement final envoyé au serveur : {best_move}")
    print(best_move)
    print(pos)

    assert best_move == [[6, 2], [6, 2]], "bon"
