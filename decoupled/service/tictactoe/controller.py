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
    logger.info("Retrieving board state")
    board_state = MODEL.get_board_state()  # returns current state of the board from MODEL
    logger.debug(f"Board state: {board_state}")

    return VIEW.board_state(board_state)  # view formats board_state into a JSON response


def get_winner() -> Response:
    """
    Retrieves the winner of the game, if there is one.

    Returns
    -------
    Response
        A Flask response object containing the winner as JSON.
    """
    logger.info("Retrieving winner")
    winner = MODEL.get_winner()  # returns winner from MODEL
    logger.debug(f"Winner: {winner}")

    return VIEW.get_winner(winner)  # winner gets formatted into a JSON response in VIEW


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
    logger.info(f"Validating index: {index}")
    try:
        index = int(index)
    except ValueError:
        logger.error(f"Invalid index: {index}")
        raise ValueError(INVALID_MOVE_ERROR_MSG)

    if index < 0 or index > 8:
        logger.error(f"Index out of bounds: {index}")
        raise ValueError(INVALID_MOVE_ERROR_MSG)

    logger.debug(f"Validated index: {index}")
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
    logger.info(f"Making move at index: {index}")
    try:
        index = validate_index(index)  # validate if it's a possible move e.g 0-8
        MODEL.move(index)  # move to the validated index
        logger.debug(f"Move made at index: {index}")

        return VIEW.board_state(MODEL.get_board_state())  # returns it as JSON

    except ValueError as e:
        logger.error(f"Error making move: {e}")
        return VIEW.error(str(e), 400)
