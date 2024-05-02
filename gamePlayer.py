from game import Game
import random

class GamePlayer:
    def __init__(self):
        pass
    
    def playRandomGame(self):
        game = Game()
        self._playRandomTurn(game)

    def _playRandomTurn(self, game: Game):
        while True:
            playableSquares = game.getPlayableSquares()
            if len(playableSquares) == 0:
                break
            randomSquare = playableSquares[random.randint(0, len(playableSquares) - 1)][0]
            game.play(randomSquare[0], randomSquare[1])
            game.printGrid()


gamePlayer = GamePlayer()

gamePlayer.playRandomGame()