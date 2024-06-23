import pygame as pg

class ComputerPlayer:
    def __init__(self, player):
        self.player = player

    def get_move(self, board):
        for i in range(9):
            if board[i] == '':
                return i
        return -1