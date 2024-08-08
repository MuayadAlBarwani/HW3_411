import logging
from typing import Optional

from tictactoe import Board, SQUARE_OCCUPIED_ERROR_MSG

logger = logging.getLogger(__name__)

class Model:
    """
    A class to represent the model for the Tic Tac Toe game.

    Attributes
    ----------
    board : Board
        The current state of the Tic Tac Toe board.
    player : str
        The current player ('X' or 'O').
    winner : Optional[str]
        The winner of the game (if any).

    Methods
    -------
    get_current_player() -> str:
        Returns the current player.

    change_player() -> None:
        Switches the current player.

    set_winner() -> None:
        Checks for a winner and sets the winner attribute if there is one.

    get_winner() -> Optional[str]:
        Returns the winner of the game (if any).

    get_board_state() -> list[str]:
        Returns a copy of the current board state.

    move(index: int) -> None:
        Makes a move at the specified index, changes the player, and checks for a winner.
    """

    def __init__(self):
        """
        Initializes the Model with an empty board and sets the starting player to 'X'.
        """  
        logger.info("Initializing Model")
        self.board = Board(['','','','','','','','',''])  # create board from indices 0-8
        self.player = 'X'  # create player and set to 'X'
        self.winner = None  # set winner to none
        logger.debug(f"Initial board state: {self.board.squares}, starting player: {self.player}")

    def get_current_player(self) -> str:
        """
        Returns the current player.

        Returns
        -------
        str
            The current player ('X' or 'O').
        """
        logger.info("Getting current player")
        return self.player

    def change_player(self) -> None:
        """
        Switches the current player from 'X' to 'O' or from 'O' to 'X'.
        """
        logger.info("Changing player")
        self.player = 'O' if self.player == 'X' else 'X'
        logger.debug(f"New current player: {self.player}")

    def set_winner(self) -> None:
        """
        Checks for a winner and sets the winner attribute if there is one.
        """
        logger.info("Setting winner")
        board = self.board.squares
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != '':
                self.winner = board[combo[0]]
                logger.debug(f"Winner found: {self.winner}")
                return
        self.winner = None  # No winner yet
        logger.debug("No winner found")

    def get_winner(self) -> Optional[str]:
        """
        Returns the winner of the game (if any).

        Returns
        -------
        Optional[str]
            The winner of the game, or None if there is no winner yet.
        """
        logger.info("Getting winner")
        return self.winner

    def get_board_state(self) -> list[str]:
        """
        Returns a copy of the current board state.

        Returns
        -------
        list[str]
            A copy of the current board state.
        """
        logger.info("Getting board state")
        board_state = self.board.squares.copy()
        logger.debug(f"Board state: {board_state}")
        return board_state

    def move(self, index: int) -> None:
        """
        Makes a move at the specified index, changes the player, and checks for a winner.

        Parameters
        ----------
        index : int
            The index at which to make the move.

        Raises
        ------
        ValueError
            If the specified index is already occupied.
        """
        logger.info(f"Making move at index: {index}")
        if self.board.squares[index] != '':
            logger.error(f"Move failed at index {index} - square already occupied")
            raise ValueError(SQUARE_OCCUPIED_ERROR_MSG)

        self.board.squares[index] = self.player
        logger.debug(f"Board state after move: {self.board.squares}")
        self.set_winner()
        self.change_player()
