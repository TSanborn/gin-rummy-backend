from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your frontend
origins = [
    "http://localhost:3000",  # For local testing
    "https://tccc-gin-rummy.onrender.com/"  # Replace with your Vercel frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test route
@app.get("/detail/{game_id}")
async def get_detail(game_id: int):
    return {
        "game_id": game_id,
        "status": "waiting",
        "players": ["Player 1", "Player 2"]
    }

@app.get("/")
async def root():
    return {"message": "Gin Rummy backend running!"}
