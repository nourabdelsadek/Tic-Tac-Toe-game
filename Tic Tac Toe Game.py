#Player's data
class Player:
    def __init__(self , name , symbol):
        self.__name = name
        self.__symbol = symbol
    # make only getters without setters to make them unchangeable
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
#####################################################################################
#Game's board
class Board:
    def __init__(self):
        self.a = [[i*3 + j +1 for j in range(3)] for i in range(3)]
    def print_board(self):
        print('_____')
        for i in self.a:
            for j in range(0,2):
                print(i[j],end='|')
            print(i[2])
            print('_____')
    def change(self , idx , player):
        row = int((idx-1) / 3)
        col = (idx-1) % 3
        self.a[row][col] = player.symbol
#####################################################################################
#Whole Game
class Game:
    def __init__(self):
        while self.choose():
            self.start()
            self.round()
    def start(self):
        name1 = input('enter first player\'s name : ')
        sym1 = input('enter first player\'s symbol : ')
        name2 = input('enter second player\'s name : ')
        sym2 = input('enter second player\'s symbol : ')
        self.players = [Player(name1, sym1) , Player(name2, sym2)]
        self.board = Board()
        self.player = 0
        self.vis = list()
    def choose(self):
        x = int(input('to exit the program choose 0 \nto start a game choose 1\nChoice: '))
        if x == 0:
            exit()
        else:
            return True
    def round(self):
        chck = False
        for turn in range(9):
            self.board.print_board()
            while True:
                idx = int(input(f'choose index {self.players[self.player].name} : '))
                if idx < 1 or idx > 9:
                    print("Number must be between 1-9!")
                elif idx in self.vis:
                    print("Position already taken!")
                else:
                    self.vis.append(idx)
                    break
            self.board.change(idx , self.players[self.player])
            if self.check(self.players[self.player]):
                chck = True
                self.board.print_board()
                print(f'congratulations!\n{self.players[self.player].name} won!')
                break
            self.switch_player()
        if not chck:
            print('draw 🤝')
    def check(self , player):
        tar = [player.symbol for j in range(3)]
        #rows check
        for row in range(3):
            if self.board.a[row]==tar:
                return True
        #columns check
        for column in range(3):
            if all(self.board.a[row][column] == player.symbol for row in range(3)):
                return True
        #first diagonal
        first_dig = [self.board.a[i][i] for i in range(3)]
        if first_dig == tar:
            return True
        #second diagonal
        second_dig = [self.board.a[i][2-i] for i in range(3)]
        if second_dig == tar:
            return True
    def switch_player(self):
        self.player = 1 - self.player
#####################################################################################
a = Game()
