# ======================== ball.py ========================

import pygame
from config import BALL_SIZE, BALL_SPEED_X, BALL_SPEED_Y, SCREEN_WIDTH, SCREEN_HEIGHT, LIVES, ball_dict
                                                                                            
# ======================== PARTIE 1.1 ========================
# TODO : Charger l'image de la balle et la redimensionner
# - Utiliser pygame.image.load("chemin/vers/image")
# - Redimensionner avec pygame.transform.scale(image, taille)
# - Stocker le résultat dans la variable « ball_img »
#
# L'image de la balle se trouve dans le dossier assets/ (ball.png).
# La taille finale doit correspondre à la constante BALL_SIZE.



ball_img = pygame.image.load("assets/ball.png")
ball_img = pygame.transform.scale(ball_img, BALL_SIZE)
None  # À remplacer par l'image chargée et redimensionnée
# ======================== PARTIE 1.2 ========================
# TODO : Initialiser les valeurs dans le dictionnaire « ball_dict »
# La balle doit partir du centre de l'écran.
#
# Clés à initialiser :
# - "x"     : position horizontale initiale (centre horizontal de l'écran)
# - "y"     : position verticale initiale (centre vertical de l'écran)
# - "dx"    : vitesse horizontale (utiliser BALL_SPEED_X)
# - "dy"    : vitesse verticale (utiliser BALL_SPEED_Y)
# - "lives" : nombre de vies (utiliser LIVES)
# - "score" : score initial (commence à 0)
ball_dict.update(
    {
        "x": SCREEN_WIDTH / 2,
        "y": SCREEN_HEIGHT / 2,
        "dx": BALL_SPEED_X,
        "dy": BALL_SPEED_Y,
        "lives": LIVES,
        "score": 0
    })