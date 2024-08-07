class Board:
    def __init__(self):
        self.generate_board(3,3)
    
    def generate_board(self, lenght, height):
        self.board = []
        for _ in range(height):
            line = []
            for _ in range(lenght):
                line.append("_")
            self.board.append(line)
        return self.board    

    def print_board(self):
        for line in self.board:
            print("|".join(line))

    def valid_range(self, line:int, column:int):
        if not line:
            line = 0
        if not column:
            column=0

        if line < len(self.board) and column < len(self.board[0]):
            return True

    def insert_element(self, element, line_position:int=None, column_position:int=None):
        if not self.valid_range(line_position,column_position):
            return
        
        if not line_position or not column_position:
            if line_position:
                for column in range(len(self.board[line_position])):
                    if self.board[line_position][column] == "_":
                        self.board[line_position][column] = element
                        return True
                
            if column_position:
                for line in range(len(self.board)):
                    if self.board[line][column_position] == "_":
                        self.board[line][column_position] = element
                        return True

            for line in range(len(self.board)):
                for column in range(len(self.board[0])):
                    if self.board[line][column] == "_":
                        self.board[line][column] = element
                        return True
                
        if self.board[line_position][column_position] == "_":
            self.board[line_position][column_position] = element
            return True
    
    def modify_element(self, element, line_position:int, column_position:int):
        if self.valid_range(line_position,column_position):
            return
        if self.board[line_position][column_position] != "_":
            self.board[line_position][column_position] = element