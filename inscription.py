import socket
import json
import threading
import struct
import AI
import random
import utile

SERVER_IP = "172.17.10.117"
SERVER_PORT = 3000
MY_PORT = 5050
MY_NAME = "edward"
MATRICULES = ["22011"]
FORMAT = "utf-8"
messages = [
    "eh rentre a la maison",
    "tu va revivre l'exam de thermo",
    "ct mieux gorilliat",
    "ah la rue",
    "recherche de kot pas loin de l'ecam",
    "a tjrs celib benoit",
    "floriant adore les chats",
    "faut laisser les militair gagner, ils savent tirer avec des kalash ",
    "j'ai plus d'inspi",
    "ct bien sans IA",
    "bon bah je rajouterais des trucs quand j'aurais de l'inspi",
]


def send_json(sock, data):
    message = json.dumps(data).encode(FORMAT)
    length = struct.pack("I", len(message))
    sock.sendall(length + message)


def receive_json(sock):

    raw_len = sock.recv(4)
    if not raw_len:
        return None
    msg_len = struct.unpack("I", raw_len)[0]
    data = b""
    while len(data) < msg_len:
        chunk = sock.recv(msg_len - len(data))
        if not chunk:
            break
        data += chunk
    return json.loads(data.decode(FORMAT))


def handle_server_requests():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", MY_PORT))
        s.listen()
        print(f"[*] Écoute sur le port {MY_PORT} pour les requêtes du serveur...")

        while True:
            conn, addr = s.accept()
            with conn:
                request = receive_json(conn)
                if not request:
                    continue

                if request.get("request") == "ping":
                    send_json(conn, {"response": "pong"})

                elif request.get("request") == "play":
                    state = request.get("state")
                    print(f"[!] Match en cours. État : {state}")
                    print(f"les erreur {request.get('errors')}")
                    player = state["current"]
                    _, best_move = AI.negamaxWithPruningIterativeDeepening(
                        state, player
                    )
                    if best_move == None:
                        pos = utile.get_pos(state["board"], player, state["color"])
                        best_move = [pos, pos]
                    print(f"les besst move {best_move}")
                    response = {
                        "response": "move",
                        "move": best_move,
                        "message": messages[random.randint(0, len(messages) - 1)],
                    }
                    send_json(conn, response)


threading.Thread(target=handle_server_requests, daemon=True).start()
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))

    inscription = {
        "request": "subscribe",
        "port": MY_PORT,
        "name": MY_NAME,
        "matricules": MATRICULES,
    }

    print(f"[*] Inscription en cours auprès de {SERVER_IP}...")
    send_json(client, inscription)

    response = receive_json(client)
    print(f"[#] Réponse serveur : {response}")

    client.close()
except Exception as e:
    print(f"[X] Erreur de connexion : {e}")
while True:
    pass