from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.schemas import s_user
from app.internal.database import get_db
from app.interface import i_user

router = APIRouter(
    prefix='/user',
    tags=["Users"]
    )

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=s_user.ShowUser)
def create_user(request: s_user.User, db: Session = Depends(get_db)):
    return i_user.create_user(request, db)

@router.get('/{id}', response_model=s_user.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return i_user.show(id, db)