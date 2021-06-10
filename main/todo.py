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

#create todo
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


#retrieve todo by id
@app.post("/api/v1/todo/retrieve/by/id")
def get_todo_by_id(id : int , db: Session = Depends(get_db)):
    try:
        retrieve_todo = crud.retrieve_todo_by_id(
            db,
            todo_id = id
        )
        response = {
            "status": 200,
            "todo_id": retrieve_todo.id,
            "todo_title": retrieve_todo.title,
            "todo_description ": retrieve_todo.discription,
            "created_at": retrieve_todo.created_at,
            "updated_at": retrieve_todo.updated_at
        }
        return response
    except Exception as e:
        response = {
            "status": 404,
            "message": "Something went wrong",
            "reason": e,
        }
        return response

#retrieve all todo
@app.post("/api/v1/todo/retrieve/all/todo")
def get_all_todo(db: Session = Depends(get_db)):
    try:
        all_todo = crud.retrieve_all_todo(db)
        response = []
        for row in all_todo:
            data ={  
                "status": 200,
                "todo_id": row.id,
                "todo_title": row.title,
                "todo_description ": row.discription,
                "created_at": row.created_at,
                "updated_at": row.updated_at
            }
            response.append(data)
        return response
    except Exception as e:
        print(e)
        response = {
            "status": 404,
            "message": "Something went wrong",
            "reason": e,
        }
        return response


#delete todo by id
@app.post("/api/v1/todo/delete/by/id")
def del_todo_by_id(id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_by_id(
            db,
            todo_id=id
        )
        response = {
            "status": 200,
            "message": "Todo record deleted",
            "todo_id": id,
        }
        return response
    except Exception as e:
        response = {
            "status": 404,
            "message": "Something went wrong",
            "reason": e,
        }
        return response
