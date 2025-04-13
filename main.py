# main.py
import pygame
from game_states.mainmenuscreen import MainMenu  # Import the MainMenu class

def main():
    print("Starting game")
    
    # Initialize pygame and create the main menu
    pygame.init()
    menu = MainMenu()
       
    # Run the main menu and get the game state (level)
    menu.run()  # Once this returns, the level will start

if __name__ == "__main__":
    main()
