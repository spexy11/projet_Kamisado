# Matricules
Ilyes Mezned : 24292
Benoît Dauphin : 24010

# Lionel Messi 
Lionel Messi est un Game Client qui utilise l'algorithme negamax pour jouer au jeu kamisado.

# Déroulement 

Le Client attend les requêtes du serveur, s'inscrit dans un premier temps, après il reçoit l'état du jeu et fait les calculs nécessaires pour trouver le meilleur coup à jouer.

# Communication 

Les échanges entre le Client et le serveur se font par des communications réseaux TCP. Le contenu sera toujours des documents JSON. 
Le fichier qui gère les communications est le fichier inscription : 

À partir de la ligne 8, l'utilisateur peut configurer les paramètres essentiels à la connexion au serveur : 'SERVER_IP', 'SERVER_PORT', 'MY_PORT', 'NOM', 'MATRICULES'.

Pour gérer les requêtes serveurs, notre client écoute sur le port 'MY_PORT' et répond à la requête d'inscription dans un premier temps et aux requêtes play par après :
{
    "response": "move", 
    "move": best_move,
    "message": "un message fun"
}. 


# Utile 

Pour avoir un programme bien structuré, on a choisi de mettre toutes les fonctions utiles pour notre IA dans un fichier utile qui définit : 

- **copy board** : une fonction qui fait une deepcopy (state["board"]) pour avoir un plateau où tester nos coups.
- **gameOver** : qui vérifie s'il y a un coup gagnant parmi les coups testés.
- **get_pos** : itère sur le plateau avec en paramètres le plateau, le joueur et la couleur du pion à jouer, et qui renvoie la position du pion dans ce plateau.
- **get_legal_moves** : qui prend en paramètres le plateau, le joueur, la position de départ et la couleur du pion à jouer et qui itère en vertical, diagonale droite et diagonale gauche sur le plateau à partir de la position de départ pour déterminer toutes les cases où le pion peut aller en éliminant le chemin qui présente une collision avec un autre pion. 

- **apply** : qui prend en paramètres le state, les positions de départ, le joueur et le move à jouer et qui renvoie un nouveau state avec le coup joué. 

# Évaluation 
Le cerveau de l'IA : la fonction qui crée un score à chaque coup joué. 
On se base sur différents facteurs pondérés : 
   - **W_PROGRESSION** : plus une pièce est proche de la ligne d'arrivée, plus w_progression augmente exponentiellement.
   - **W_MOBILITY** : la mobilité est très importante pour éviter les états bloqués et donc ce paramètre augmente le score avec le nombre de cases vides où le pion peut se rendre.
   - **W_BLOCK** : si le pion n'a aucun mouvement possible, il est pénalisé.
   - **W_WIN_THREAT** : si une pièce a un coup gagnant parmi ses mouvements futurs possibles, on la récompense.
   - **W_WIN_ACHIEVED** : la victoire acquise qui pèse plus que tous les autres paramètres pour assurer le choix de la victoire. 


# AI
L'algorithme que l'IA utilise est celui de negamax, qui est une variante optimisée et simplifiée de l'algorithme Minimax, il repose sur l'idée que maximiser son propre gain, cela revient au même que de minimiser la perte de l'adversaire. Cette algorithme fonctionne bien si il n'y à pas de contrainte de temps.

Il à été ajouté à negamax une fonction de pruning, généralement appelé élagage alpha-bêta, il sert à accélérer de manière drastique la recherche de la meilleure décision en évitant de parcourir toutes les branches lorsque l'algorithme doit déterminer quel coup jouer en évitant de parcourir une branche si sa valeur de base est plus basse que celles parcourues juste avant. Cet élagage fonctionne grâce à la fonction d'évaluation qui donne une certaine valeur aux coups possibles, la plus grande valeur obtenable sera stocké dans la variable alpha, et correspond à la meilleure valeur que le joueur qui maximise (nous) peut obtenir, et le beta stocke l'inverse, la plus petite valeur que le joueur qui minimise (l'adversaire) peut obtenir.

L'IA fonctionne également avec de l'iterative deepening qui permet de gérer la contrainte de temps imposée de 3 secondes, pour cela nous imposons à l'algorithme de réaliser les calculs dans un certain laps de temps qui une fois écoulé, déclenchera une exception pour sortir de la boucle :
    except TimeOutError:
        print(
            f"Timeout atteint à la profondeur {current_depth}. Renvoi du meilleur coup."
        )

Après l'exception l'algorithme retourne le meilleur score et le meilleur coup qu'il à trouver pour pouvoir l'envoyer au serveur. La limite de temps que nous avons imposés à notre IA est inférieur à 3 seconde pour que qu'elle ait le temps d'envoyer ce qu'elle à trouvé.

# Test 

Un fichier pytest que l'on a utilisé pendant le développement pour vérifier que les fonctions développées étaient bien fonctionnelles et déboguer quand il y avait des problèmes.

# bibliotheque utiliser : 
pytest : pour faire des testes des differents fonctions de du programe .

socket : "Gère les communications réseau bidirectionnelles via des sockets TCP/UDP, permettant une connectivité robuste entre le client et le serveur."

json : "Assure la sérialisation et la désérialisation des données pour un échange d'informations structuré et léger."

threading : "Optimise les performances grâce au multithreading, permettant au serveur de gérer plusieurs connexions simultanées sans blocage."

struct : "Utilisé pour l'empaquetage des données binaires (sérialisation C-style), garantissant une gestion précise de la taille des paquets et de l'endianness."

copy : "Permet la manipulation sécurisée d'objets complexes via des copies profondes (deep copies), évitant ainsi les effets de bord lors de la gestion d'états partagés."