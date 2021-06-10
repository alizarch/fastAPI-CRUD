from sqlalchemy.orm import Session
import models

def create_todo(db: Session, title: str, discription: str):
    todo = models.todo_model(
        title=title,
        discription=discription,
        status=1
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
