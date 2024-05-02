DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

class Game:
    def __init__(self):
        self.grid = [[0 for i in range(8)] for j in range(8)]
        self.grid[3][3] = 1
        self.grid[4][4] = 1
        self.grid[3][4] = 2
        self.grid[4][3] = 2
        self.nextPlayer = 1
        self.winner = -1

    def printGrid(self):
        for row in self.grid:
            tmpOutput = ""
            for square in row:
                tmpOutput += str(square) + " "
            print(tmpOutput)
        print("\n")
    
    def getGrid(self):
        return self.grid
    
    def play(self, row, col):
        if self.winner > -1:
            return 0
        gainOfSquares = 0
        for direction in DIRECTIONS:
            gainOfSquares += self._playLineFromSquareInDirection(row, col, direction)
        if gainOfSquares == 0:
            raise Exception("this position is not valid")
        gainOfSquares += 1
        self.grid[row][col] = self.nextPlayer
        self.nextPlayer = 3 - self.nextPlayer # 1 -> 2 or 2 -> 1
        if len(self.getPlayableSquares()) == 0:
            self._endGame()
        return gainOfSquares

    def getPlayableSquares(self): # returns playable squares as an array of tuples as (coordinates, gain of squares)
        playableSquares = []
        for square in self._squaresWithAnOccupiedSquareAround():
            lengthInDirections = []
            for direction in DIRECTIONS:
                lengthInDirections.append(self._lengthOfLineFromSquareToDirection(square[0], square[1], direction))
            totalGainOfSquares = sum(lengthInDirections)
            if totalGainOfSquares > 0:
                playableSquares.append((square, totalGainOfSquares))
        return playableSquares
        
        

    def _squaresWithAnOccupiedSquareAround(self): # TODO can be optimized with memory
        result = set()
        for row in range(8):
            for col in range(8):
                if self.grid[row][col] > 0:
                    continue
                if self._hasAnOccupiedSquareAround(row, col):
                    result.add((row, col))
        return result
    
    def _hasAnOccupiedSquareAround(self, row, col):
        for i,j in DIRECTIONS:
                testRow = row + i
                testCol = col + j
                if not self._coordinatesAreValid(testRow, testCol):
                    continue
                if self.grid[testRow][testCol] > 0:
                    return True
        return False
    
    def _lengthOfLineFromSquareToDirection(self, row, col, direction):
        length = 0
        testRow = row
        testCol = col
        while True:
            testRow += direction[0]
            testCol += direction[1]
            if not self._coordinatesAreValid(testRow, testCol):
                return False
            if self.grid[testRow][testCol] == 3 - self.nextPlayer:
                length += 1
                continue
            if self.grid[testRow][testCol] == self.nextPlayer:
                if length == 0:
                    return 0
                return length
            return 0 # if test square is empty
            
    
    def _coordinatesAreValid(self, row, col):
        return row > -1 and row < 8 and col > -1 and col < 8
    
    def _playLineFromSquareInDirection(self, row, col, direction):
        lengthOfLine = self._lengthOfLineFromSquareToDirection(row, col, direction)
        for i in range(lengthOfLine):
            currentRow = row + (i + 1) * direction[0]
            currentCol = col + (i + 1) * direction[1]
            self.grid[currentRow][currentCol] = self.nextPlayer
        return lengthOfLine
    
    def _endGame(self):
        playerOneCounter = 0
        playerTwoCounter = 0
        for row in range(8):
            for col in range(8):
                squareValue = self.grid[row][col]
                if squareValue == 1:
                    playerOneCounter += 1
                    continue
                if squareValue == 2:
                    playerTwoCounter += 1
        if playerOneCounter > playerTwoCounter:
            self.winner = 1
            print("Player 1 wins!")
        elif playerOneCounter < playerTwoCounter:
            self.winner = 2
            print("Player 2 wins!")
        else:
            self.winner = 0
            print("Draw!")