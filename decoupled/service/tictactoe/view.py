import logging

from flask import jsonify, make_response, Response
from tictactoe import Board

logger = logging.getLogger(__name__)

class View:
    """
    A class to represent the view for the Tic Tac Toe game.

    Methods
    -------
    board_state(board: Board) -> Response:
        Returns the current state of the board as a JSON response.

    get_winner(winner: str = None) -> Response:
        Returns the winner of the game as a JSON response.

    error(error: str) -> Response:
        Returns an error message as a JSON response.
    """
    
    def board_state(self, board: Board) -> Response:
        """
        output example:
        {
        "board": ["X", "O", "X", "O", "X", "O", "X", "O", "X"] #based on index, from 0-8, counting from left -> right
        }
        
        """
        """
        Returns the current state of the board as a JSON response.

        Parameters
        ----------
        board : Board
            The current state of the Tic Tac Toe board.

        Returns
        -------
        Response
            A Flask response object containing the board state.
        """
        logger.info("Returning board state")
        response = jsonify({'board': board})
        logger.debug(f"Board state response: {response.get_json()}")
        return response
        
    def get_winner(self, winner: str = None) -> Response:
        """
        output example:
        {
        "winner": null
        or
        "winner": "X"
        }
        """
        """
        Returns the winner of the game as a JSON response.

        Parameters
        ----------
        winner : str, optional
            The winner of the game (default is None).

        Returns
        -------
        Response
            A Flask response object containing the winner.
        """
        logger.info("Returning winner")
        response = jsonify({'winner': winner})
        logger.debug(f"Winner response: {response.get_json()}")
        return response

    def error(self, error: str) -> Response:
        """
        output example:
        {
        "error": "Invalid move"
        }
        """
        """
        Returns an error message as a JSON response.

        Parameters
        ----------
        error : str
            The error message to return.

        Returns
        -------
        Response
            A Flask response object containing the error message.
        """
        logger.error(f"Returning error: {error}")
        response = jsonify({'error': error})
        response.status_code = 400
        logger.debug(f"Error response: {response.get_json()}")
        return response
