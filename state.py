from copy import deepcopy


class State:
    def __init__(self, rows, cols, board) -> None:
        self.rows = rows
        self.cols = cols
        self.board = board

    def __str__(self) -> str:
        result = ""
        for row in self.board:
            for cell in row:
                result += str(cell) + " "
            result += "\n"  
        return result
    def in_board(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols
    def getAttractCoord(self):
        for row in self.board:
            for cell in row:
                if cell.current_type == "attract":
                    return cell.x, cell.y

    def getRepelCoord(self):
        for row in self.board:
            for cell in row:
                if cell.current_type == "repel":
                    return cell.x, cell.y 
    

    def checkWin(self):
        for row in self.board:
            for cell in row:
                if cell.current_type == "road" and cell.is_Solve:
                    return False  
        return True  
    
    def canMove(self, x, y):
        if x < 0:
            return False
        elif x >= self.rows:
            return False
        elif y < 0:
            return False 
        elif y >= self.cols:
            return False 
        elif self.board[x][y].current_type == 'road':
            return True
        else:
            return False

    def canRepelCol(self, x_neigh, x_next, y):
        if self.board[x_neigh][y].current_type == "road":
            if x_next<self.cols and x_next>0:
                if self.board[x_next][y].current_type in ["iron", "attract"]:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
    
    def canRepelRow(self, y_neigh, y_next, x):
        if self.board[x][y_neigh].current_type == "road":
            if y_next<self.rows and y_next>0:
                if self.board[x][y_next].current_type in ["iron", "attract"]:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True


    def moveMagnetCells(self, current_move, i, j, attract_x, attract_y):
        for cell in reversed(current_move.board[i][:j]):
            if cell.current_type in ["iron", "repel"]:
                if current_move.canMove(cell.x, cell.y + 1):
                    current_move.movecell(cell.x, cell.y + 1, cell.x, cell.y)
    
        for cell in current_move.board[i][j + 1:]:
            if cell.current_type in ["iron", "repel"]:
                if current_move.canMove(cell.x, cell.y - 1):
                    current_move.movecell(cell.x, cell.y - 1, cell.x, cell.y)

        for row in reversed(current_move.board[:i]):
            cell = row[j]
            if cell.current_type in ["iron", "repel"]:
                if current_move.canMove(cell.x + 1, cell.y):
                    current_move.movecell(cell.x + 1, cell.y, cell.x, cell.y)
    
        for row in current_move.board[i:]:
            cell = row[j]
            if cell.current_type in ["iron", "repel"]:
                if current_move.canMove(cell.x - 1, cell.y):
                    current_move.movecell(cell.x - 1, cell.y, cell.x, cell.y)

        return current_move

    def moveRepelCells(self, current_move, i, j, repel_x, repel_y):
        for cell in reversed(current_move.board[i][:j]):
            if cell.current_type in ["iron", "attract"]:
                if current_move.canMove(cell.x, cell.y - 1):
                    if current_move.canRepelRow(cell.y + 1, cell.y + 2, cell.x):
                        current_move.movecell(cell.x, cell.y - 1, cell.x, cell.y)

        for cell in current_move.board[i][j + 1:]:
            if cell.current_type in ["iron", "attract"]:
                if current_move.canMove(cell.x, cell.y + 1):
                    if current_move.canRepelRow(cell.y - 1, cell.y - 2, cell.x):
                        current_move.movecell(cell.x, cell.y + 1, cell.x, cell.y)

        for row in current_move.board[:i]:
            cell = row[j]
            if cell.current_type in ["iron", "attract"]:
                if current_move.canMove(cell.x - 1, cell.y):
                    if current_move.canRepelCol(cell.x + 1, cell.x + 2, cell.y):
                        current_move.movecell(cell.x - 1, cell.y, cell.x, cell.y)

        for row in reversed(current_move.board[i:]):
            cell = row[j]
            if cell.current_type in ["iron", "attract"]:
                if current_move.canMove(cell.x + 1, cell.y):
                    if current_move.canRepelCol(cell.x-1, cell.x - 2, cell.y):
                        current_move.movecell(cell.x + 1, cell.y, cell.x, cell.y)

        return current_move


    def possibleMovesAlternative(self):
        moves = []
        attract_coords = self.getAttractCoord()
        repel_coords = self.getRepelCoord()
    
        if attract_coords:
            attract_x, attract_y = attract_coords
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.canMove(i, j):
                        current_move = deepcopy(self)
                        current_move.board[i][j].current_type = current_move.board[attract_x][attract_y].current_type
                        current_move.board[attract_x][attract_y].current_type = 'road'
                        current_move = self.moveMagnetCells(current_move, i, j, attract_x, attract_y)
                        moves.append(current_move)
        if repel_coords:
            repel_x, repel_y = repel_coords
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.canMove(i, j):
                        current_move = deepcopy(self)
                        current_move.board[i][j].current_type = current_move.board[repel_x][repel_y].current_type
                        current_move.board[repel_x][repel_y].current_type = 'road'
                        current_move = self.moveRepelCells(current_move, i, j, repel_x, repel_y)
                        moves.append(current_move)

        return moves


    def movecell(self, x, y, old_x, old_y):
        self.board[x][y].current_type = self.board[old_x][old_y].current_type
        self.board[old_x][old_y].current_type = 'road'