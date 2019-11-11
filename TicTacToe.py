#Create class to store player info

class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

#Create a class to handle the screen and board

class ScreenBoard:

    def __init__(self):
        self.board = ['','','','','','','','','']

    def initialise_board(self):
        for i in self.board:
            i = ''

    def draw_board(self):
        print(" " + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + " ")
        print("--------")
        print(" " + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + " ")
        print("--------")
        print(" " + self.board[6] + " | " + self.board[7] + " | " + self.board[8] + " ")

    def check_move(self, move):
        if ((move >= 0) and (move < 9)):
            if self.board[move] == '':
                return True
            else:
                return False
        else:
            return False

    def update_board(self, move, symbol):
        self.board[move] = symbol

    def check_more_moves_left(self):
        movesLeft = 0
        for i in self.board:
            if i == '':
                movesLeft += 1
        if movesLeft == 0:
            return False
        else:
            return True

    def check_win(self):
        # Check horizontal
        if self.board[0] == self.board[1] == self.board[2] != '':
            return True
        if self.board[3] == self.board[4] == self.board[5] != '':            
            return True
        if self.board[6] == self.board[7] == self.board[8] != '':            
            return True

        # Check vertical
        if self.board[0] == self.board[3] == self.board[6] != '':            
            return True
        if self.board[1] == self.board[4] == self.board[7] != '':            
            return True
        if self.board[2] == self.board[5] == self.board[8] != '':            
            return True

        # Check Diagonal
        if self.board[0] == self.board[4] == self.board[8] != '':            
            return True
        if self.board[2] == self.board[4] == self.board[6] != '':           
            return True

        return False

#Main Program Code now that classes are created (methods tested during creation)

name1 = input("Player 1 , please enter your name: ")
name2 = input("Player 2 , please enter your name: ")

p1 = Player(name1, 'x')
p2 = Player(name2, 'o')

playing = True

#Set the current Player for the first turn, this will be p1
currentPlayer = "P1"
currentPlayerName = p1.name
currentSymbol = p1.symbol

gameBoard = ScreenBoard()


#Start Game Loop
while playing == True:

    gameBoard.draw_board()

    legalMove = False
    while legalMove == False:
        thisMove = int(input(currentPlayerName + " please enter your move (0 - 8): "))
        if gameBoard.check_move(thisMove) == True:
            legalMove = True
            gameBoard.update_board(thisMove, currentSymbol)
        else:
            print("That move is illegal!")

    if gameBoard.check_win() == True:
        print(currentPlayerName + " has won the game")
        playing = False

    
    if ((gameBoard.check_more_moves_left() == False) and (playing == True)):
        print("There are no more moves left to be played")
        playing = False


    #Set the player to the other player
    if currentPlayer == "P1":
        currentPlayer = "P2"
        currentPlayerName = p2.name
        currentSymbol = p2.symbol
    else:
        currentPlayer = "P1"
        currentPlayerName = p1.name
        currentSymbol = p1.symbol
        
        

   
        
        
            
        
        
    

    

    
        
