from fastapi import Request

from app.core.farkle import Farkle


def get_game_state(request: Request) -> Farkle:
    """Dependency that returns the global service instance."""
    return request.app.state.game_state