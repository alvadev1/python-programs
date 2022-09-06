from os import system


class Game:
    def __init__(self) -> None:
        self.player = "x"
        self.table = [" "," "," "," "," "," "," "," "," "]
        self.winner = False


    def show_table(self) -> None:
        print(f"""{self.table[0]}|{self.table[1]}|{self.table[2]}\n{self.table[3]}|{self.table[4]}|{self.table[5]}\n{self.table[6]}|{self.table[7]}|{self.table[8]}""")

    def user_input(self) -> int:
        while True:
            try:
                opt = int(input("input an number[1-9]: "))
                if opt not in range(1, 10):
                    print("numero invalido.")
                    continue
                return opt
            except ValueError:
                print("opcao invalida.")
                continue

    def switch_player(self) -> None:
        if self.player == "x": self.player = "o"
        else: self.player = "x"


    def insert_play_on_table(self) -> bool:
        input_user = self.user_input()
        if self.table[input_user-1] != " ":
            return False
        self.table[input_user-1] = self.player
        return True

    def verify_winner(self) -> bool:
        if self.table[0] == self.player and \
            self.table[1] == self.player and \
            self.table[2] == self.player:
            self.winner = True
        elif self.table[3] == self.player and \
            self.table[4] == self.player and \
            self.table[5] == self.player:
            self.winner = True 
        elif self.table[6] == self.player and \
            self.table[7] == self.player and \
            self.table[8] == self.player:
            self.winner = True
        elif self.table[0] == self.player and \
            self.table[3] == self.player and \
            self.table[6] == self.player:
            self.winner = True
        elif self.table[1] == self.player and \
            self.table[4] == self.player and \
            self.table[7] == self.player:
            self.winner = True
        elif self.table[2] == self.player and \
            self.table[5] == self.player and \
            self.table[8] == self.player:
            self.winner = True
        elif self.table[0] == self.player and \
            self.table[4] == self.player and \
            self.table[8] == self.player:
            self.winner = True
        elif self.table[2] == self.player and \
            self.table[4] == self.player and \
            self.table[6] == self.player:
            self.winner = True

        return self.winner

    def verify_draw(self) -> bool:
        if self.winner:
            return False

        for slot in self.table:
            if slot == " ":
                return False

        return True



if __name__ == '__main__':
    tic_tac_toe = Game()
    system("clear")
    while not tic_tac_toe.winner:
        tic_tac_toe.show_table()
        print(f"{tic_tac_toe.player} sua vez.")
        if not tic_tac_toe.insert_play_on_table():
            system("clear")
            print("jogada invalida ou esse espaco ja foi preenchido.")
            continue
        if tic_tac_toe.verify_winner():
            system("clear")
            print(f"{tic_tac_toe.player} voce ganhou.")
            tic_tac_toe.show_table()
            break
        if tic_tac_toe.verify_draw():
            system("clear")
            print("deu velha.")
            tic_tac_toe.show_table()
            break
        tic_tac_toe.switch_player()
        system("clear")
