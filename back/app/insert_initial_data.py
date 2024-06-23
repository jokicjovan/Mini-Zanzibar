from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas import UserCreate, BoardCreate
import app.crud as crud


def insert_initial_data():
    db: Session = SessionLocal()
    try:
        # Create users
        user1 = UserCreate(name="John", surname="Doe", email="john@example.com", password="password123")
        user2 = UserCreate(name="Jane", surname="Smith", email="jane@example.com", password="password123")

        db_user1 = crud.create_user(db, user1)
        db_user2 = crud.create_user(db, user2)

        # Create boards
        board1 = BoardCreate(name="Board 1", owner_id=db_user1.id, content={"description": "This is board 1"})
        board2 = BoardCreate(name="Board 2", owner_id=db_user2.id, content={"description": "This is board 2"})

        crud.create_board(db, board1)
        crud.create_board(db, board2)
    finally:
        db.close()