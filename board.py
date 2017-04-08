import discord
from tile import *
import numpy


class board(object):
    def __init__(self, bot, channel):
        self.bot = bot
        self.channel = channel
        self.boardState = [[], [], []]
        for i in range(0, 3):
            for j in range(0, 3):
                self.boardState[i].append(tile())

    async def drawBoard(self):
        await self.bot.send_message(self.channel,
                                    self.boardState[0][0].getState() + '|' + self.boardState[0][1].getState() + '|' +
                                    self.boardState[0][2].getState()
                                    + '\n--------\n' +
                                    self.boardState[1][0].getState() + '|' + self.boardState[1][1].getState() + '|' +
                                    self.boardState[1][2].getState()
                                    + '\n--------\n' +
                                    self.boardState[2][0].getState() + '|' + self.boardState[2][1].getState() + '|' +
                                    self.boardState[2][2].getState()
                                    )

    def changeTile(self, x, y, state):
        self.boardState[x][y].changeState(state)

    def isWinner(self, x, y):
        # check if previous move caused a win on vertical line
        if self.boardState[0][y].getState() == self.boardState[1][y].getState() == self.boardState[2][y].getState():
            return True

        # check if previous move caused a win on horizontal line
        if self.boardState[x][0].getState() == self.boardState[x][1].getState() == self.boardState[x][2].getState():
            return True

        # check if previous move was on the main diagonal and caused a win
        if x == y and self.boardState[0][0].getState() == self.boardState[1][1].getState() == self.boardState[2][
            2].getState():
            return True

        # check if previous move was on the secondary diagonal and caused a win
        if x + y == 2 and self.boardState[0][2].getState() == self.boardState[1][1].getState() == self.boardState[2][
            0].getState():
            return True

        return False
