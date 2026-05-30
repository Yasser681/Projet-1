# ======================== paddle.py ========================

import pygame 
from config import PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_Y, SCREEN_WIDTH, paddle_dict

# ======================== PARTIE 1.3 ========================
# TODO : Charger l'image de la raquette et la redimensionner
# - L'image se trouve dans assets/paddle.png
# - Redimensionner avec pygame.transform.scale(image, (PADDLE_WIDTH, PADDLE_HEIGHT))
# - Stocker le résultat dans la variable « paddle_img »

paddle_img = pygame.image.load("assets/paddle.png")
paddle_img = pygame.transform.scale(paddle_img, (PADDLE_WIDTH, PADDLE_HEIGHT))
# ======================== PARTIE 1.4 ========================
# TODO : Initialiser les valeurs dans le dictionnaire « paddle_dict »
# La raquette doit apparaître centrée horizontalement, en bas de l'écran.
#
# Clés à initialiser :
# - "x" : position horizontale (centrée dans l'écran)
# - "y" : position verticale fixe (utiliser PADDLE_Y)
paddle_dict.update(
    {
        "x" : (SCREEN_WIDTH - PADDLE_WIDTH) // 2,
        "y" : PADDLE_Y
    })
