import uvicorn
from fastapi import FastAPI
from controller import register_routes

app = FastAPI()

if __name__ == "__main__":
    register_routes(app)
    uvicorn.run(app, host='localhost', port=8090)
