class tile(object):
    def __init__(self):
        self.state = " "

    def changeState(self, newState):
        if self.state == " ":
            if newState in ['X', 'x', 'O', 'o']:
                self.state = newState
                return 0
            else:
                return 1
        return 1

    def getState(self):
        return self.state

    def checkState(self, tile):
        res = False
        if (self.state == tile.state):
            res = True
        return res
