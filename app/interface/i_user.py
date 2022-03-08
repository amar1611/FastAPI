from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas import s_user
from app.models import User
from app.internal.hashing import Hash

def create_user(request: s_user.User, db:Session):
    hashed_password = Hash.get_password_hash(request.password)

    new_user = User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def show(id:int,db:Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id: {id} not found in database')
    
    return user

def delete_user(id:int,db:Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id: {id} not found in database')
    else:
        db.delete(user)
        db.commit()