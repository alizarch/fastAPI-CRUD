from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/v1/todo/create")
def create_todo(title: str, discription: str, db: Session = Depends(get_db)):
    try:
        insert_todo = crud.create_todo(
            db,
            title=title,
            discription=discription
        )
        response = {
            "status": 200,
            "message": "TODO created successfully",
            "todo_id": insert_todo.id,
            "todo_title": insert_todo.title,
            "todo_description ": insert_todo.discription,
        }
        return response
    except Exception as e:
        response = {
            "status": 404,
            "message": "Something went wrong",
            "reason": e,
        }
        return response
