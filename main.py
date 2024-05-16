from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


class Todo(BaseModel):
    id: int
    title: str
    description: str
    writer: str


TODOS = [
    Todo(id=1, title="todo 1", description="this is todo 1", writer="alex"),
    Todo(id=2, title="todo 2", description="this is todo 2", writer="steven"),
    Todo(id=3, title="todo 3", description="this is todo 3", writer="bob"),
]


@app.get("/todos", response_model=List[Todo])
async def get_all_todos() -> List[Todo]:
    return TODOS
