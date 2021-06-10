from sqlalchemy.orm import Session
from datetime import datetime
import models

############ 1 ############
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

############ 2 ############
def retrieve_todo_by_id(db: Session, todo_id: int):
    todo = db.query(
        models.todo_model
    ).filter(
        models.todo_model.id == todo_id
    ).first()
    return todo

############ 3 ############
def retrieve_all_todo(db: Session):
    all_todo = db.query(
        models.todo_model
    ).all()
    return all_todo

############ 4 ############
def delete_by_id(db: Session, todo_id: int):
    del_by_id = db.query(
        models.todo_model
    ).filter(
        models.todo_model.id == todo_id
    ).delete()
    db.commit()
    return del_by_id
    
############ 5 ############
def delete_all_todo(db: Session):
    del_all_todo = db.query(
        models.todo_model
    ).delete()
    db.commit()
    return del_all_todo

############ 6 ############
def update_todo(db: Session , todo_id: int, new_title: str, new_discription: str):
    update = db.query(
        models.todo_model
    ).filter(
        models.todo_model.id == todo_id
    ).update({
        models.todo_model.title: new_title,
        models.todo_model.discription: new_discription,
        models.todo_model.updated_at: datetime.now(),
    })
    db.commit()
    todo = db.query(
        models.todo_model
    ).filter(
        models.todo_model.id == todo_id
    ).first()
    return todo
