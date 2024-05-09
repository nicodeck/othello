import random
from game import Game
from gamePlayer import GamePlayer
from randomGamePlayer import RandomGamePlayer

class NaiveGamePlayer:
    def __init__(self):
        pass

    def playNNaiveGames(self, N):
        playerOneWins = 0
        playerTwoWins = 0
        draws = 0
        for i in range(N):
            print("Game {}/{}".format(i, N))
            winner = self.playNaiveGame()
            if winner == 1:
                playerOneWins += 1
            elif winner == 2:
                playerTwoWins += 1
            elif winner == 0:
                draws += 1
            else:
                raise Exception("Unexpected game output")
        print("{} games played: {} wins, {} losses, {} draws".format(N, playerOneWins, playerTwoWins, draws))
        

    def playNaiveGame(self, printGrids = False, printValues = False):
        game = Game()
        playTheNextTurn = True
        while playTheNextTurn:
            if game.getNextPlayer() == 1:
                playTheNextTurn = self.playNaiveTurn(game, printGrids, printValues)
            else:
                playTheNextTurn = RandomGamePlayer.playRandomTurn(game, printGrids)
        return game.getWinner()


    def playNaiveTurn(self, game: Game, printGrid = False, printTurnValue = False):
        playableSquares = game.getPlayableSquares()
        if len(playableSquares) == 0:
            return False
        gamePlayer = GamePlayer()
        node = gamePlayer.buildTreeOfDepthN(game.getGrid(), game.getNextPlayer(), 1)
        children = node.getChildren()
        bestChildIndexes = [0]
        bestScore = 0
        for childIndex in range(len(children)):
            childScore = children[childIndex].getValue()
            if childScore > bestScore:
                bestChildIndexes = [childIndex]
                bestScore = childScore
            elif childScore == bestScore:
                bestChildIndexes.append(childIndex)
        bestChild = children[random.choice(bestChildIndexes)]
        bestSquare = bestChild.getTurn()
        game.play(bestSquare[0], bestSquare[1])
        if printGrid:
            game.printGrid()
        return True


gameplayer = NaiveGamePlayer()


gameplayer.playNNaiveGames(1000)