import logging

from flask import Response

from tictactoe import Board, configure_logger, INVALID_MOVE_ERROR_MSG
from tictactoe.model import Model
from tictactoe.view import View


MODEL = Model()
VIEW = View()


logger = logging.getLogger(__name__)
configure_logger()


def get_board_state() -> Response:
    """
    Retrieves the current state of the board.

    Returns
    -------
    Response
        A Flask response object containing the board state as JSON.
    """
    board_state = MODEL.get_board_state() #returns current state of the board from MODEL

    return VIEW.board_state(board_state) #view fromats board_state into a JSON response

def get_winner() -> Response:
    """
    Retrieves the winner of the game, if there is one.

    Returns
    -------
    Response
        A Flask response object containing the winner as JSON.
    """
    winner = MODEL.get_winner() #returns winner from MODEL

    return VIEW.get_winner(winner) #winner gets formatted into a JSON response in VIEW

def validate_index(index: str) -> int:
    """
    Validates the provided index for a move.

    Parameters
    ----------
    index : str
        The index to validate.

    Returns
    -------
    int
        The validated index.

    Raises
    ------
    ValueError
        If the index is not a valid integer or is out of bounds.
    """

    try:
        index = int(index)
    except ValueError:
        raise ValueError(INVALID_MOVE_ERROR_MSG)

    if index < 0 or index > 8:
        raise ValueError(INVALID_MOVE_ERROR_MSG)

    return index

def make_move(index: str) -> Response:
    """
    Makes a move at the specified index.

    Parameters
    ----------
    index : str
        The index at which to make the move.

    Returns
    -------
    Response
        A Flask response object indicating success or failure.
    """
    try:
        index = validate_index(index) #validate if its a possible move e.g 0-8
        MODEL.move(index) #move to the validated index

        return VIEW.board_state(MODEL.get_board_state())  #returns it as JSON

    except ValueError as e:
        logger.error(f"Error making move: {e}")
        return VIEW.error(str(e), 400)