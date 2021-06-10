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


def retrieve_todo_by_id(db: Session, todo_id: int):
    todo = db.query(
        models.todo_model
    ).filter(
        models.todo_model.id == todo_id
    ).first()
    
    return todo


def retrieve_all_todo(db: Session):
    all_todo = db.query(
        models.todo_model
    ).all()
    return all_todo


def delete_by_id(db: Session, todo_id: int):
    del_by_id = db.query(
        models.todo_model
    ).filter(
        models.todo_model.id == todo_id
    ).delete()
    db.commit()
    return del_by_id
    
def delete_all_todo(db: Session):
    del_all_todo = db.query(
        models.todo_model
    ).delete()
    db.commit()
    return del_all_todo
