import uvicorn
from fastapi import FastAPI
from controller import register_routes

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    register_routes(app)
    uvicorn.run(app, host='localhost', port=8090)
