import discord
import random
from board import *
from player import *


class tttgame(object):
    def __init__(self, bot, channel, p1, p2):
        self.bot = bot
        self.channel = channel
        self.board = board(bot, channel)
        self.turn = random.randint(0, 1)
        self.player1 = p1
        self.player2 = p2
        self.converter = {1: [0, 0],
                          2: [0, 1],
                          3: [0, 2],
                          4: [1, 0],
                          5: [1, 1],
                          6: [1, 2],
                          7: [2, 0],
                          8: [2, 1],
                          9: [2, 2],
                          }

    def getBoard(self):
        return self.board

    def getTurn(self):
        return self.turn

    async def whoGoesFirst(self):
        if (self.turn == 0):
            await self.bot.send_message(self.channel, self.player1.getName() + 'Goes First!')
        else:
            await self.bot.send_message(self.channel, self.player2.getName() + 'Goes First!')

    async def nextTurn(self):
        if self.turn == 0:
            await self.bot.send_message(self.channel, self.player2.getName() + 'Goes Next!')
            self.turn = 1
        else:
            await self.bot.send_message(self.channel, self.player1.getName() + 'Goes Next!')
            self.turn = 0

    async def move(self, board, player, tile):
        letter = player.getLetter()
        (x, y) = self.converter[int(tile)]
        board.changeTile(x, y, letter)
        await board.drawBoard()
        await self.nextTurn()
        return x, y
