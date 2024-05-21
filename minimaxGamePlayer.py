import time
import random
from game import Game
from gamePlayer import GamePlayer
from randomGamePlayer import RandomGamePlayer
from naiveGamePlayer import NaiveGamePlayer

class MinimaxGamePlayer:
    def __init__(self):
        pass

    def playNMinimaxGames(self, N, depth):
        playerOneWins = 0
        playerTwoWins = 0
        draws = 0
        start = time.perf_counter()
        for i in range(N):
            print("Game {}/{}".format(i, N))
            winner = self.playMinimaxGame(depth)
            if winner == 1:
                playerOneWins += 1
            elif winner == 2:
                playerTwoWins += 1
            elif winner == 0:
                draws += 1
            else:
                raise Exception("Unexpected game output")
        end = time.perf_counter()
        print("{} games played: {} wins, {} losses, {} draws, duration: {} seconds per game".format(N, playerOneWins, playerTwoWins, draws, (end - start) / N))
        

    def playMinimaxGame(self, depth, printGrids = False, printValues = False):
        game = Game()
        playTheNextTurn = True
        while playTheNextTurn:
            if game.getNextPlayer() == 1:
                playTheNextTurn = MinimaxGamePlayer.playMinimaxTurn(game, depth, printGrids, printValues)
            else:
                playTheNextTurn = RandomGamePlayer.playRandomTurn(game)
        game.printGrid()
        return game.getWinner()

    @staticmethod
    def playMinimaxTurn(game: Game, depth, printGrid = False, printTurnValue = False):
        playableSquares = game.getPlayableSquares()
        if len(playableSquares) == 0:
            return False
        gamePlayer = GamePlayer()
        node = gamePlayer.buildTreeOfDepthN(game.getGrid(), game.getNextPlayer(), depth)
        node.recGetMinimaxTurn()
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
        #print("len of children is " + str(len(children)))
        bestChild = children[random.choice(bestChildIndexes)]
        bestSquare = bestChild.getTurn()
        game.play(bestSquare[0], bestSquare[1])
        if printGrid:
            game.printGrid()
        return True


gameplayer = MinimaxGamePlayer()


gameplayer.playNMinimaxGames(100, 3)