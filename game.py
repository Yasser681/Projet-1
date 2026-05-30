# ======================== game.py ========================

import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    PADDLE_SPEED, PADDLE_WIDTH, PADDLE_HEIGHT,
    BALL_SIZE, BALL_SPEED_X, BALL_SPEED_Y,
    BRICKS, ball_dict, paddle_dict
)


# ======================== PARTIE 3.1 ========================
# TODO : Déplacer la balle
# À chaque appel, la balle doit avancer d'un pas dans sa direction actuelle.
#
# - Ajouter « dx » à la position « x » de la balle
# - Ajouter « dy » à la position « y » de la balle

def move_ball():
    ball_dict["x"]+=BALL_SPEED_X
    ball_dict["y"]+=BALL_SPEED_Y


# ======================== PARTIE 3.2 ========================
# TODO : Rebondir sur les murs et le plafond
# La balle doit rebondir lorsqu'elle atteint un bord de l'écran.
#
# - Bord GAUCHE  (x <= 0)         : inverser dx (ball_dict["dx"] *= -1)
# - Bord DROIT   (x + largeur >= SCREEN_WIDTH)  : inverser dx
# - Plafond      (y <= 0)         : inverser dy
#
# Remarque : le sol n'est PAS géré ici (voir check_floor).

def bounce_walls():
    if ball_dict["x"]<=0:
        ball_dict["dx"] *= -1
    if ball_dict["x"]+ BRICK_WIDTH >= SCREEN_WIDTH:
        ball_dict["dx"]*=-1
    if ball_dict["y"]<=0:
        ball_dict["dx"]*=-1
    pass  # À compléter


# ======================== PARTIE 3.3 ========================
# TODO : Détecter si la balle touche le sol
# Si le bas de la balle dépasse le bas de l'écran, retourner True.
# Sinon, retourner False.
#
# Rappel : le bas de la balle = ball_dict["y"] + BALL_SIZE[1]

def check_floor():
    if ball_dict["y"] + BALL_SIZE[1]>SCREEN_HEIGHT:
        return True
    else:
        return False
    
# ======================== PARTIE 3.4 ========================
# TODO : Déplacer la raquette selon les touches pressées
# Utiliser pygame.key.get_pressed() pour détecter les touches maintenues.
#
# - Flèche GAUCHE (pygame.K_LEFT)  : diminuer « x » de PADDLE_SPEED
# - Flèche DROITE (pygame.K_RIGHT) : augmenter « x » de PADDLE_SPEED
#
# La raquette ne doit pas sortir de l'écran :
# - x minimum : 0
# - x maximum : SCREEN_WIDTH - PADDLE_WIDTH
#
# Astuce : utilisez la fonction max() et min() pour clamper la valeur.

def move_paddle():
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_dict["x"]-=PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle_dict["x"]+=PADDLE_SPEED
    paddle_dict["x"]= max(0, min(paddle_dict["x"],SCREEN_WIDTH-PADDLE_WIDTH))
# ======================== PARTIE 4.1 ========================
# TODO : Détecter la collision entre la balle et la raquette
# Si la balle touche la raquette, elle doit rebondir vers le haut.
#
# Pour vérifier la collision :
# 1. Créer un rectangle pour la balle   (ball_dict["x"], ball_dict["y"], BALL_SIZE[0], BALL_SIZE[1])
# 2. Créer un rectangle pour la raquette (paddle_dict["x"], paddle_dict["y"], PADDLE_WIDTH, PADDLE_HEIGHT)
# 3. Utiliser rects_collide(r_balle, r_raquette) pour tester le chevauchement.
#
# Si collision :
# - Inverser dy (ball_dict["dy"] *= -1)
# - S'assurer que dy est bien NÉGATIF après le rebond (dy = -abs(dy))
#   (évite que la balle reste bloquée dans la raquette)

def check_paddle_collision():
    ball_rect = pygame.Rect(ball_dict["x"], ball_dict["y"], BALL_SIZE[0], BALL_SIZE[1])
    paddle_rect = pygame.Rect(paddle_dict["x"], paddle_dict["y"], PADDLE_WIDTH, PADDLE_HEIGHT)
    isColliding = rects_collide(ball_rect, paddle_rect)
    if isColliding:
        ball_dict["dy"] *= -1


# ======================== PARTIE 4.2 ========================
# TODO : Détecter la collision entre la balle et les briques
# Parcourez la liste BRICKS. Pour chaque brique ACTIVE :
#
# 1. Créer un rectangle pour la balle.
# 2. Créer un rectangle pour la brique (brick["x"], brick["y"], brick["width"], brick["height"]).
# 3. Utiliser rects_collide(...) pour tester la collision.
#
# En cas de collision :
# - Marquer la brique comme inactive : brick["active"] = False
# - Ajouter les points de la brique au score : ball_dict["score"] += brick["points"]
# - Inverser dy (ball_dict["dy"] *= -1)
# - Arrêter la boucle (utiliser break) pour ne toucher qu'une brique à la fois
    

def check_brick_collision():
    rect_ball = pygame.Rect(ball_dict["x"], ball_dict["y"], BALL_SIZE[0], BALL_SIZE[1])
    for brick in BRICKS:
        rect_brick = pygame.Rect(brick["x"], brick["y"], brick["width"], brick["height"])
        isColliding = rects_collide(rect_ball, rect_brick)
        if isColliding:
            brick["active"] = False
            ball_dict["score"] += brick["points"]
            ball_dict["dy"] *= -1
            break
    pass  # À compléter


# ======================== PARTIE 4.3 ========================
# TODO : Vérifier si toutes les briques sont détruites
# Retourner True si toutes les briques ont « active == False ».
# Retourner False sinon.
#
# Astuce : utilisez la fonction all() avec une expression génératrice.

def check_win():
    return all(brick["active"] for brick in BRICKS)


# ── Fonction utilitaire (ne pas modifier) ───────────────────
# Vérifie si deux rectangles (x, y, largeur, hauteur) se chevauchent.
def rects_collide(r1, r2):
    return not (
        r1[0] + r1[2] <= r2[0] or r1[0] >= r2[0] + r2[2] or
        r1[1] + r1[3] <= r2[1] or r1[1] >= r2[1] + r2[3]
    )
