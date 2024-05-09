from game import Game
import random

class RandomGamePlayer:
    def __init__(self):
        pass

    def playNRandomGames(self, N):
        playerOneWins = 0
        playerTwoWins = 0
        draws = 0
        for i in range(N):
            print("Game {}/{}".format(i, N))
            winner = self.playRandomGame()
            if winner == 1:
                playerOneWins += 1
            elif winner == 2:
                playerTwoWins += 1
            elif winner == 0:
                draws += 1
            else:
                raise Exception("Unexpected game output")
        print("{} games played: {} wins, {} losses, {} draws".format(N, playerOneWins, playerTwoWins, draws))
        
    
    def playRandomGame(self, printTurns = False):
        game = Game()
        playTheNextTurn = True
        while playTheNextTurn:
            playTheNextTurn = RandomGamePlayer.playRandomTurn(game, printTurns)
        return game.getWinner()
    
    @staticmethod
    def playRandomTurn(game: Game, printGrid = False):
        playableSquares = game.getPlayableSquares()
        if len(playableSquares) == 0:
            return False
        randomSquare = playableSquares[random.randint(0, len(playableSquares) - 1)][0]
        game.play(randomSquare[0], randomSquare[1])
        if printGrid:
            game.printGrid()
        return True

"""
gamePlayer = RandomGamePlayer()

gamePlayer.playNRandomGames(1000)

"""