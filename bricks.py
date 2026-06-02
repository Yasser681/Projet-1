# ======================== bricks.py ========================

import pygame
from config import (
    BRICK_ROWS, BRICK_COLS, BRICK_WIDTH, BRICK_HEIGHT,
    BRICK_PADDING, BRICK_OFFSET_TOP, BRICK_OFFSET_LEFT,
    BRICK_COLORS, BRICK_POINTS, BRICKS
)

# Chargement et redimensionnement des images de briques (fourni)
# Un dictionnaire associe chaque couleur à son image pygame.
brick_images = {
    color: pygame.transform.scale(
        pygame.image.load(f"assets/brick_{color}.png"),
        (BRICK_WIDTH, BRICK_HEIGHT)
    )
    for color in BRICK_COLORS
}


# ======================== PARTIE 2.1 ========================
# TODO : Générer la grille de briques
#
# Complétez la fonction generate_bricks() qui retourne une liste
# de dictionnaires représentant toutes les briques du jeu.
#
# Chaque dictionnaire de brique doit contenir exactement ces clés :
#   {
#       "x"      : position horizontale de la brique,
#       "y"      : position verticale de la brique,
#       "width"  : largeur (utiliser BRICK_WIDTH),
#       "height" : hauteur (utiliser BRICK_HEIGHT),
#       "color"  : nom de la couleur (ex : "red"),
#       "image"  : image correspondante (depuis brick_images),
#       "active" : True  (la brique est présente au départ),
#       "points" : nombre de points (utiliser BRICK_POINTS[row])
#   }
#
# La grille est organisée en rangées (row) et colonnes (col).
# Utilisez les constantes suivantes pour calculer les positions :
#   - BRICK_OFFSET_LEFT : décalage depuis la gauche de l'écran
#   - BRICK_OFFSET_TOP  : décalage depuis le haut de l'écran
#   - BRICK_PADDING     : espace entre les briques
#
# Formule pour la position x d'une brique :
#   x = BRICK_OFFSET_LEFT + col * (BRICK_WIDTH + BRICK_PADDING)
#
# Formule pour la position y d'une brique :
#   y = BRICK_OFFSET_TOP + row * (BRICK_HEIGHT + BRICK_PADDING)
#
# IMPORTANT : utilisez une compréhension de liste imbriquée
# (double boucle for ... for dans la même expression [ ... ]).

def generate_bricks():
 # À remplacer par une compréhension de liste
    return [
        {
            "x": BRICK_OFFSET_LEFT + col * (BRICK_WIDTH + BRICK_PADDING),
            "y": BRICK_OFFSET_TOP + row * (BRICK_HEIGHT + BRICK_PADDING),
            "width": BRICK_WIDTH,
            "height": BRICK_HEIGHT,
            "color": BRICK_COLORS[row],
            "image": brick_images[BRICK_COLORS[row]],
            "active": True,
            "points": BRICK_POINTS[row]
        }
        for row in range(BRICK_ROWS)
        for col in range(BRICK_COLS)]

