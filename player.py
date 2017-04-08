import discord


class player(object):
    def __init__(self, name, number, letter):
        self.name = name
        self.number = number
        self.letter = letter

    def setOrder(self, position):
        self.position = position

    def getLetter(self):
        return self.letter

    def getName(self):
        return str(self.name)[:-5]
