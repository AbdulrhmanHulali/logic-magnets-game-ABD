from game import Game
from levels import LevelManager

class main:

    level_manager = LevelManager()
    init_state = level_manager.choose_level()

    print("\nChoose Mode:")
    print("1: Play as regular player")
    print("2: Use algorithm (e.g., BFS or DFS)")

    mode_choice = int(input("Enter the number for mode: "))
    if mode_choice == 1:
        print("Starting game in regular player mode.")
        game = Game(init_state)
        game.play()
    elif mode_choice == 2:
        algo = input("Choose algorithm (BFS/DFS): ").upper()
        if algo in ["BFS", "DFS"]:
            print(f"Starting game in {algo} mode.")
            game = Game(init_state)
            game.BFSsearchDFS(algo)
        else:
            print("Invalid algorithm choice. Defaulting to BFS.")
            game = Game(init_state)
            game.BFSsearchDFS("BFS")
    else:
        print("Invalid mode. Starting game in regular player mode by default.")
        game = Game(init_state)
        game.play()
