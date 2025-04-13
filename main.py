# main.py
import pygame
from game_states.mainmenuscreen import MainMenu  # main menu

def main():
    print("Starting game")
    
    # Initializing pygame
    pygame.init()
    menu = MainMenu()
       
    # Run the main menu and get the game state (level)
    menu.run()  

if __name__ == "__main__":
    main()
