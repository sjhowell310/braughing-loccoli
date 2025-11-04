from fastapi import APIRouter, Depends
from app.core.helpers import get_game_state
from app.schemas.farkle import GameState
from app.core.farkle import Farkle


game_session_router = APIRouter(prefix="/session", tags=["Session"])


@game_session_router.get("/", response_model=GameState)
def get_game_state_endpoint():
    """Get current get state for front end"""
    return get_game_state()


@game_session_router.post("/reset", response_model=GameState)
def reset_game_state_endpoint(game: Farkle = Depends(get_game_state)):
    """Reset game state and return reset game state for front end"""
    game = Farkle()
    return get_game_state()


@game_session_router.post("/setup", response_model=GameState)
def setup_game_state_endpoint(game: Farkle = Depends(get_game_state)):
    """Reset game state and return reset game state for front end"""
    game = Farkle()
    return get_game_state()
