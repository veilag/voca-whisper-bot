from .menu import router as menu_router
from .start import router as start_router
from .game import router as game_router
from .assistant import router as assistant_router

__all__ = ["menu_router",
           "start_router",
           "game_router",
           "assistant_router"]
