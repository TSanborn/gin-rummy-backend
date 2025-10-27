from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://gin-rummy-frontend-mtogwoe2p-tylers-projects-0e8a6c28.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/detail/{game_id}")
def get_detail(game_id: int):
    return {
        "game_id": game_id,
        "status": "waiting",
        "players": ["Player 1", "Player 2"]
    }

@app.get("/")
def root():
    return {"message": "Gin Rummy backend is running!"}
