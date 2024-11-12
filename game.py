import copy

from state import State


class Game:
    def __init__(self, init_state) -> None:
        self.state = init_state
        self.current_state = copy.deepcopy(init_state)
        self.states = []
        self.states.append(init_state)
        self.possible_moves = []
        self.possible_moves.append(init_state)
        self.visited_states = []
        self.visited_states.append(init_state)


    def BFSsearchDFS(self, algo):
        while self.possible_moves:
            if(algo == 'BFS'):
                self.current_state = self.possible_moves.pop(0)
            else:
                self.current_state = self.possible_moves.pop()
            if self.current_state.checkWin():
                self.visited_states.append(self.current_state)
                for visited in self.visited_states:
                    print(visited)
                break
            if self.current_state not in self.visited_states:
                self.visited_states.append(self.current_state)
            moves = self.current_state.possibleMovesAlternative()
            for move in moves:
               if move not in self.visited_states:
                   self.possible_moves.append(move) 

    def move(self, state, x, y, old_x, old_y, magnet_type):
        new_state = copy.deepcopy(state)
        new_state.board[old_x][old_y].current_type = 'road'
    
        if magnet_type == "repel":
            new_state.board[x][y].current_type = 'repel'
        else:
            new_state.board[x][y].current_type = magnet_type

        if new_state.board[x][y].initial_type == 'solve':
            new_state.board[x][y].current_type = 'repel'

        return new_state


    def attract(self, state, x, y):
        new_state = copy.deepcopy(state)

        for i in range(x - 1, -1, -1):
            if new_state.board[i][y].current_type == "iron":
                new_state.board[i][y].current_type = 'road'
                new_state.board[i + 1][y].current_type = 'iron'
            elif new_state.board[i][y].current_type == "repel":
                new_state.board[i][y].current_type = 'road'
                new_state.board[i + 1][y].current_type = 'repel'
                break
            elif new_state.board[i][y].current_type != "road":
                break

        for i in range(x + 1, new_state.rows):
            if new_state.board[i][y].current_type == "iron":
                new_state.board[i][y].current_type = 'road'
                new_state.board[i - 1][y].current_type = 'iron'
            elif new_state.board[i][y].current_type == "repel":
                new_state.board[i][y].current_type = 'road'
                new_state.board[i - 1][y].current_type = 'repel'
                break
            elif new_state.board[i][y].current_type != "road":
                break

        for j in range(y - 1, -1, -1):
            if new_state.board[x][j].current_type == "iron":
                new_state.board[x][j].current_type = 'road'
                new_state.board[x][j + 1].current_type = 'iron'
            elif new_state.board[x][j].current_type == "repel":
                new_state.board[x][j].current_type = 'road'
                new_state.board[x][j + 1].current_type = 'repel'
                break
            elif new_state.board[x][j].current_type != "road":
                break

        for j in range(y + 1, new_state.cols):
            if new_state.board[x][j].current_type == "iron":
                new_state.board[x][j].current_type = 'road'
                new_state.board[x][j - 1].current_type = 'iron'
            elif new_state.board[x][j].current_type == "repel":
                new_state.board[x][j].current_type = 'road'
                new_state.board[x][j - 1].current_type = 'repel'
                break
            elif new_state.board[x][j].current_type != "road":
                break

        return new_state  

    def repel(self, state, x, y, description):
        new_state = copy.deepcopy(state)

        for j in range(y - 1, -1, -1):
            if new_state.board[x][j].current_type == "iron":
                if j > 0 and new_state.board[x][j - 1].current_type == "iron":
                    if new_state.in_board(x, j - 2) and new_state.board[x][j - 2].current_type in ["road", "solve"]:
                        new_state.board[x][j - 2].current_type = "iron"
                        new_state.board[x][j - 1].current_type = "iron"
                        new_state.board[x][j].current_type = "road"
                    break
                elif new_state.in_board(x, j - 1) and new_state.board[x][j - 1].current_type in ["road", "solve"]:
                    new_state.board[x][j - 1].current_type = "iron"
                    new_state.board[x][j].current_type = "road"
                break
            elif new_state.board[x][j].current_type == "attract":
                if new_state.in_board(x, j - 1) and new_state.board[x][j - 1].current_type in ["road", "solve"]:
                    new_state.board[x][j - 1].current_type = "attract"
                    new_state.board[x][j].current_type = "road"
                break

        for j in range(y + 1, new_state.cols):
            if new_state.board[x][j].current_type == "iron":
                if j < new_state.cols - 1 and new_state.board[x][j + 1].current_type == "iron":
                    if new_state.in_board(x, j + 2) and new_state.board[x][j + 2].current_type in ["road", "solve"]:
                        new_state.board[x][j + 2].current_type = "iron"
                        new_state.board[x][j + 1].current_type = "iron"
                        new_state.board[x][j].current_type = "road"
                    break
                elif new_state.in_board(x, j + 1) and new_state.board[x][j + 1].current_type in ["road", "solve"]:
                    new_state.board[x][j + 1].current_type = "iron"
                    new_state.board[x][j].current_type = "road"
                break
            elif new_state.board[x][j].current_type == "attract":
                if new_state.in_board(x, j + 1) and new_state.board[x][j + 1].current_type in ["road", "solve"]:
                    new_state.board[x][j + 1].current_type = "attract"
                    new_state.board[x][j].current_type = "road"
                break

        for i in range(x - 1, -1, -1):
            if new_state.board[i][y].current_type == "iron":
                if i > 0 and new_state.board[i - 1][y].current_type == "iron":
                    if new_state.in_board(i - 2, y) and new_state.board[i - 2][y].current_type in ["road", "solve"]:
                        new_state.board[i - 2][y].current_type = "iron"
                        new_state.board[i - 1][y].current_type = "iron"
                        new_state.board[i][y].current_type = "road"
                    break
                elif new_state.in_board(i - 1, y) and new_state.board[i - 1][y].current_type in ["road", "solve"]:
                    new_state.board[i - 1][y].current_type = "iron"
                    new_state.board[i][y].current_type = "road"
                break
            elif new_state.board[i][y].current_type == "attract":
                if new_state.in_board(i - 1, y) and new_state.board[i - 1][y].current_type in ["road", "solve"]:
                    new_state.board[i - 1][y].current_type = "attract"
                    new_state.board[i][y].current_type = "road"
                break

        for i in range(x + 1, new_state.rows):
            if new_state.board[i][y].current_type == "iron":
                if i < new_state.rows - 1 and new_state.board[i + 1][y].current_type == "iron":
                    if new_state.in_board(i + 2, y) and new_state.board[i + 2][y].current_type in ["road", "solve"]:
                        new_state.board[i + 2][y].current_type = "iron"
                        new_state.board[i + 1][y].current_type = "iron"
                        new_state.board[i][y].current_type = "road"
                    break
                elif new_state.in_board(i + 1, y) and new_state.board[i + 1][y].current_type in ["road", "solve"]:
                    new_state.board[i + 1][y].current_type = "iron"
                    new_state.board[i][y].current_type = "road"
                break
            elif new_state.board[i][y].current_type == "attract":
                if new_state.in_board(i + 1, y) and new_state.board[i + 1][y].current_type in ["road", "solve"]:
                    new_state.board[i + 1][y].current_type = "attract"
                    new_state.board[i][y].current_type = "road"
                break

        return new_state

    def moveCell(self, x, y, old_x, old_y):
        self.current_state.board[x][y].type = self.current_state.board[old_x][old_y].type
        self.current_state.board[old_x][old_y].type = 'road'

    def moveAttract(self, x, y):
        attract_x, attract_y = self.state.getAttractCoord()
        if attract_x is not None and attract_y is not None and self.state.canMove(x, y):
                self.state = self.move(self.state, x, y, attract_x, attract_y, "attract")
                self.state = self.attract(self.state, x, y)  
        else:
                print('Invalid move for attract magnet!')

    def moveRepel(self, x, y):
        repel_x, repel_y = self.state.getRepelCoord()
        if repel_x is not None and repel_y is not None and State.canMove(self.state, x, y):
            self.state = self.move(self.state, x, y, repel_x, repel_y, "repel")
            self.state = self.repel(self.state, x, y, "Repel move")  # Pass a description
        else:
            print('Invalid move for repel magnet!')


    def play(self):
        while True:
            print(str(self.state))
            if self.state.checkWin():
                print("Congratulations! You've won the game!")
                break

            move_type = input("Enter 'attract' to move the red magnet or 'repel' to move the purple magnet: ")
            new_x = int(input("Enter the new x-coordinate for the magnet: "))
            new_y = int(input("Enter the new y-coordinate for the magnet: "))

            if move_type == 'attract':
                self.moveAttract(new_x, new_y)
            elif move_type == 'repel':
                self.moveRepel(new_x, new_y)
            else:
                print("Invalid input. Please enter 'attract' or 'repel'.")
