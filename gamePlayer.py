from copy import deepcopy

from game import Game

class TreeNode:
    def __init__(self, grid, player, value = 0, turn = (3,3)):
        self.children = []
        self.value = value
        self.grid = grid
        self.player = player
        self.turn = turn

    def getValue(self):
        return self.value

    def getTurn(self):
        return self.turn
    
    def getNextPlayer(self):
        return self.player

    def getGrid(self):
        return self.grid 

    def getChildren(self):
        return self.children

    def addChild(self, child):
        self.children.append(child)
    
    def printNode(self, short = False):
        game = Game()
        game.forceGridAndPlayer(self.grid, self.player)
        print("Node: next player is player {}".format(self.player))
        if not short:
            game.printGrid()
        print("Value of node = {}".format(self.value))
    
    def printChildren(self, short = False):
        child: TreeNode
        for child in self.children:
            child.printNode(short)
    
    def printTree(self, short = False):
        if len(self.children) == 0:
            return
        self.printChildren(short)
        child: TreeNode
        for child in self.children:
            child.printChildren(short)




class GamePlayer:
    def __init__(self):
        pass

    def buildTreeOfDepthN(self, grid, nextPlayer, N):
        node = TreeNode(deepcopy(grid), nextPlayer)

        self._recursiveAddChildrenToDepthN(node, N)        
        
        #node.printTree()

        return node
    
    def _recursiveAddChildrenToDepthN(self, node: TreeNode, N):
        if N == 0:
            return node
        self._buildChildrenOfNode(node)
        child: TreeNode
        for child in node.getChildren():
            #child.printNode(True)
            self._recursiveAddChildrenToDepthN(child, N - 1)

    
    def _buildChildrenOfNode(self, node: TreeNode):
        grid = deepcopy(node.getGrid())
        nextPlayer = deepcopy(node.getNextPlayer())
        game = Game()
        game.forceGridAndPlayer(grid, nextPlayer)
        playableSquares = game.getPlayableSquares()
        nextPlayer = node.getNextPlayer()

        for square, value in playableSquares:
            game.forceGridAndPlayer(deepcopy(grid), nextPlayer)
            if nextPlayer == 1:
                gainOfSquares = game.play(square[0], square[1])
            else:
                gainOfSquares = -1 * game.play(square[0], square[1])

            newGrid = game.getGrid()
            newPlayer = game.getNextPlayer()
            childNode = TreeNode(newGrid, newPlayer, gainOfSquares, square)
            node.addChild(childNode)
        

"""
game = Game()

grid = game.getGrid()

gamePlayer = GamePlayer()

gamePlayer.buildTreeOfDepthN(grid, 1, 1)

"""