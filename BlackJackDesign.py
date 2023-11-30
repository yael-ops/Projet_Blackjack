import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 1000

# Créer la fenêtre principale
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Blackjack Game")

# Charger l'image de fond
fond = pygame.image.load(r"C:\Users\SLAB65\Downloads\Mockup_575_40x40c_Base_1200x1200.jpg") 
fond = pygame.transform.scale(fond, (largeur_fenetre, 800))

# Charger l'image pour les boutons
interface_boutons = pygame.image.load(r"C:\Users\SLAB65\Downloads\walnut-tree-texture-close-up-260nw-1928448911.jpg")  
interface_boutons = pygame.transform.scale(interface_boutons, (largeur_fenetre, 210))  


# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN :
            if event.key==pygame.K_q:
                continuer= False
            pygame.quit()
            sys.exit
            
    # Afficher l'image de fond
    fenetre.blit(fond, (0,-10))

     # Afficher l'interface des boutons dans la partie inférieure de la fenêtre
    fenetre.blit(interface_boutons, (0, hauteur_fenetre - 210))

    # Mettre à jour l'affichage
    pygame.display.flip()
