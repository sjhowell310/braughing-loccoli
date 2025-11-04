from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.farkle import Farkle
from app.routes import game_session

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.game_state = Farkle()
    yield
    # Optionally clean up resources here

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include Routers ---
app.include_router(game_session.game_session_router, prefix=settings.API_PREFIX)

# --- Root + Health ---
@app.get("/", tags=["Root"])
def root():
    return {"message": f"🚀 {settings.PROJECT_NAME} is now running!"}

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}

# --- Entry Point for Local Run ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=True)
