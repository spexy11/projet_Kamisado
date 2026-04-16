import socket
import json
import threading
import struct


SERVER_IP = "172.17.10.46"
SERVER_PORT = 3000
MY_PORT = 5050
MY_NAME = "ilyes et benoit contre le reste du monde "
MATRICULES = ["22001"]
FORMAT = "utf-8"


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
                    print(f"[!] Match en cours. État : {request.get('state')}")
                    response = {
                        "response": "move",
                        "move": 0,
                        "message": "Je vais gagner !",
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
