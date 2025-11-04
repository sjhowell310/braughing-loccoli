from pydantic import BaseModel, ConfigDict, Field


class Player(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    score: int = 0


class GameState(BaseModel):
    model_config = ConfigDict(extra="forbid")
    players: dict[str, Player] = Field(default_factory=dict)
    current_player: str | None = None
    next_player: str | None = None

class GameSettings(BaseModel):
    model_config = ConfigDict(extra="forbid")
    num_players: int = 2
    order_dice: bool = False
    score_limit: int = 10000
    score_threshold: int = 500
    player_specify_set: bool = False
