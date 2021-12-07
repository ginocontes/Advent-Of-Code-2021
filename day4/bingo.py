import random
import re
class BingoGame(object):
    def __init__(self, boards, numbers=list(range(1,100))):
        self.boards = [ Board(board) for board in boards ]
        self.numbers = numbers
        self.index_next_number = 0

    @classmethod
    def parse_game(cls, file_path):
        with open(file_path) as f:
            first_line = f.readline().strip()
            bingo_lines = f.readlines()
            numbers = first_line.split(',')
            boards = cls.parse_board(bingo_lines)
        return numbers, boards

    @classmethod
    def parse_board(cls,bingo_lines):
        bingo_lines = list(filter(lambda line: line!='', map(lambda line: line.strip(), filter(lambda line: line != '/n', bingo_lines))))
        boards = []
        res = []
        for row in bingo_lines:
            board =  row.split(' ')
            board = list(map(int, filter(lambda line: line!='',board)))
            boards += [board]
        for i in range(0, len(boards), 5):
            res += [boards[i:i+5]]

        return res

    def shuffle(self):
        random.shuffle(self.numbers)

    def is_there_a_winning_board(self):
        for board in self.boards:
            if board.is_winning_board():
                return board, True
        return None, False

    def points(self, board, last_number_drawn):
        return sum(set(self.numbers).difference(board.checked_numbers)) * last_number_drawn

    def draw_number(self):
        if self.index_next_number > len(self.numbers) :
            raise IndexError("No more numbers to draw")
        number = self.numbers[self.index_next_number]
        self.index_next_number += 1
        return number

    def play(self):
        for i in range(len(self.numbers)):
            number = self.draw_number()
            for board in self.boards:
                board.check_number(number)
            winning_board, is_there = self.is_there_a_winning_board()
            print(winning_board, is_there)
            if not is_there:
                print(f"No winning board yet!")
            if is_there:
                print(f"Winning board has {self.points(winning_board, number)} points!")
                return self.points(winning_board, number)
        return -1



class Board(object):
    def __init__(self, rows):
        self.matrix_board = rows
        self.checked_numbers = set()

    def is_winning_board(self):
        return self.is_column_filled() or self.is_row_filled()

    def is_column_filled(self):
        is_filled = False
        for i in range(5):
            for row in self.matrix_board:
                if row[i] not in self.checked_numbers:
                    break
                is_filled = True
            if not is_filled:
                continue
            else:
                return is_filled
        return is_filled

    def is_row_filled(self):
        is_filled = False
        for row in self.matrix_board:
            for number in row:
                if number not in self.checked_numbers:
                    break
                is_filled = True
            if not is_filled:
                continue
            else:
                return is_filled
        return is_filled

    def check_number(self, number):
        for row in self.matrix_board:
            if number in row:
                self.checked_numbers.add(number)

if __name__ == '__main__':
    numbers, boards= BingoGame.parse_game('input1.txt')
    bingo = BingoGame(boards, numbers)
    print(bingo.play())
