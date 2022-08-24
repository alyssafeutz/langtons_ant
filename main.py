ef Start():
    """Get user input to initialize ant object"""
    print("Welcome to Langton’s ant simulation! ")
    # get user input for game parameters
    board_size = int(input("First, please enter a number no larger than 100 for the size of the square board:\n"))
    row_location = int(input("Choose the ant’s starting location, please enter a number as the starting row number (where 0 is the first row from the top):\n"))
    column_location = int(input("Please enter a number as the starting column number (where 0 is the first column from the left):\n"))
    ant_orientation = int(input("Please choose the ant’s starting orientation, 0 for up, 1 for right, 2 for down, 3 for left:\n"))
    number_of_steps = int(input("Please enter the number of steps for the simulation:\n"))
    current_state = "_"
    # use user input to initialize instance of an Ant object
    our_ant = Ant(board_size, row_location, column_location, ant_orientation, number_of_steps, current_state)
    # call "run_simulation" method from Ant class on Ant object
    our_ant.run_simulation()


class Ant:

    """A simulation of Langton's Ant"""

    def __init__(self, board_size, row_location, column_location, ant_orientation, number_of_steps, current_state):
        """Initializes objects for game"""
        self._board_size = board_size
        self._row_location = row_location
        self._column_location = column_location
        self._ant_orientation = ant_orientation
        self._number_of_steps = number_of_steps
        self._current_state = current_state
        self._row = []

    def run_simulation(self):
        """Starts simulation of ant movement"""
        number_of_rounds = 0
        # calls "create gameboard" function to update "row" to reflect gameboard using user's chosen boardsize
        self._row = self.create_gameboard()

        # while loop that continues to run until user's chosen number of steps is reached
        while number_of_rounds != self._number_of_steps:
            if self._current_state == "_":
                # call function to change orientation if white space
                self.change_orientation_white_space()
            # call function to change orientation if space is black
            elif self._current_state == "#":
                self._ant_orientation = self.change_orientation_black_space()
            # call function to change color of former space that ant just left
            self.change_old_space_color()
            # if ant is moving up or down, call function to change row location
            if self._ant_orientation == 0 or self._ant_orientation == 2:
                self._row_location = self.change_row_location()
            # if ant is moving left or right, call function to change column location
            elif self._ant_orientation == 1 or self._ant_orientation == 3:
                self._column_location = self.change_column_location()
            # call function to update current_state to current color
            self._current_state = self.change_current_state()
            # call function to change current space to show ant (represented by "8")
            self._row = self.change_space_to_ant()
            # increase counter for number of rounds that have been completed
            number_of_rounds += 1

        # after while loop has run, call function to print final board
        self.print_board()

    def get_board_size(self):
        """Return board size"""
        return self._board_size

    def get_row_location(self):
        """Return row location"""
        return self._row_location

    def get_column_location(self):
        """Return column location"""
        return self._column_location

    def get_ant_orientation(self):
        """Return ant orientation location"""
        return self._ant_orientation

    def get_number_of_steps(self):
        """Return number of steps location"""
        return self._number_of_steps

    def get_current_state(self):
        """Returns current state"""
        return self._current_state

    def create_gameboard(self):
        """Creates a gameboard based on boardsize"""
        column = []
        # establish a white space for width of board
        for x in range(self._board_size):
            column.append("_")
        # establish a white space for length of board
        for y in range(self._board_size):
            self._row.append([x for x in column])
        return self._row

    def change_orientation_white_space(self):
        """Changes ant orientation if space was white"""
        if 3 > self._ant_orientation >= 0:
            self._ant_orientation += 1
        elif self._ant_orientation == 3:
            self._ant_orientation = 0
        return self._ant_orientation

    def change_orientation_black_space(self):
        """Changes ant orientation if space was black"""
        if self._ant_orientation > 0:
            self._ant_orientation -= 1
        elif self._ant_orientation == 0:
            self._ant_orientation = 3
        return self._ant_orientation

    def change_old_space_color(self):
        """Changes old space color"""
        if self._current_state == "_":
            self._row[self._row_location][self._column_location] = "#"
        elif self._current_state == "#":
            self._row[self._row_location][self._column_location] = "_"
        return self._row

    def change_row_location(self):
        """Changes row location if ant moves up or down"""
        # if ant is facing up
        if self._ant_orientation == 0:
            # if ant is at top of row and facing up, wrap around to bottom
            if self._row_location - 1 < 0:
                self._row_location = self._board_size - 1
            # if ant is facing up, move up one row
            else:
                self._row_location = self._row_location - 1
        elif self._ant_orientation == 2:
            # if ant is at bottom of row and facing down, wrap around to top
            if self._row_location + 1 >= self._board_size:
                self._row_location = 0
            # if ant is facing down, move down one row (or add one to index)
            else:
                self._row_location = self._row_location + 1
        return self._row_location

    def change_column_location(self):
        """Changes column location if ant moves left or right"""
        if self._ant_orientation == 1:
            # if ant is facing right and at rightmost edge of board, wrap
            if self._column_location + 1 >= self._board_size:
                self._column_location = 0
            # if ant is facing right, move one space to the right
            else:
                self._column_location = self._column_location + 1

        elif self._ant_orientation == 3:
            # if ant is facing left and at leftmost edge of board, wrap
            if self._column_location - 1 < 0:
                self._column_location = self._board_size - 1
            # if ant if facing left, move once space to left
            else:
                self._column_location = self._column_location - 1
        return self._column_location

    def change_current_state(self):
        """Changes current state"""
        self._current_state = self._row[self._row_location][self._column_location]
        return self._current_state

    def change_space_to_ant(self):
        """Changes current space to represent ant's presence"""
        self._row[self._row_location][self._column_location] = "8"
        return self._row

    def print_board(self):
        """Prints the final board"""
        for n in self._row:
            print("".join(n))


# call first function
if __name__ == "__main__":
     Start()
