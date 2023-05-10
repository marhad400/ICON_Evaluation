import numpy as np
import time


class Game:
    def __init__(self, size=(8,8), seed=None, max_gen=10):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)
        
        # Initialize the board with a random series of 1s and 0s
        self._board = np.random.randint(0,2,size)
        self._gen = 0
        self._max_gen = max_gen

    
    def update(self):
        board = np.copy(self._board)
        
        ''' Insert your code for updating the board based on the rules below '''
        for i in range(self._board.shape[0]):
            for j in range(self._board.shape[1]):
                # Get the sum of alive neighbors
                neighbors = np.sum(self._board[i-1:i+2, j-1:j+2]) - self._board[i][j]
                
                # Game logic
                if self._board[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                    board[i][j] = 0
                elif self._board[i][j] == 1 and (2 <= neighbors <= 3):
                    board[i][j] = 1
                else:
                    if neighbors == 3 and self._board[i][j] == 0:
                        board[i][j] = 1
                    
        self._board = board


    def play(self, delay=.1):
        while self._gen < self._max_gen:
            # Start the generation by drawing the current board
            self.draw()
            
            # Next we update each of the cells according to the rules 
            self.update()

            # Increment the generation and sleep to make the visualization easier
            self._gen += 1
            time.sleep(delay)

    def time_run(self, gens=1000):
        start = time.time()
        for _ in range(gens):
            self.update()
        print(f'Average update time: {(time.time()-start)/gens*1000} ms')

    def draw(self):
        for row in self._board:   
            # Print a full block for each alive cell and an empty one for dead cells bounded by |
            print('|'.join(['▇' if c else ' ' for c in row]))

        print(f'Generation: {self._gen}')


if __name__ == "__main__":
    # If this file is run directly from the command line, run the game
    g = Game()
    g.time_run()
    g.play()  # Uncomment this to see the generational progression