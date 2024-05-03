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
        return self.playRandomTurn(game, printTurns)

    def playRandomTurn(self, game: Game, printGrid = False):
        while True:
            playableSquares = game.getPlayableSquares()
            if len(playableSquares) == 0:
                break
            randomSquare = playableSquares[random.randint(0, len(playableSquares) - 1)][0]
            game.play(randomSquare[0], randomSquare[1])
            if printGrid:
                game.printGrid()
        return game.getWinner()


gamePlayer = RandomGamePlayer()

gamePlayer.playNRandomGames(1000)