
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List

from app.interface import i_blog
from app.schemas import s_blog, s_user
from app.internal.database import get_db
from app.internal.oauth2 import get_current_user


router = APIRouter(
    prefix='/blog',
    tags=["Blogs"]
    )

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: s_blog.Blog, db: Session = Depends(get_db), get_current_user: s_user.User = Depends(get_current_user)):
    return i_blog.create(request,db)


@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def destroy(id:int , db: Session = Depends(get_db), get_current_user: s_user.User = Depends(get_current_user)):
    return i_blog.destroy(id, db)
    

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: s_blog.Blog, db: Session = Depends(get_db), get_current_user: s_user.User = Depends(get_current_user)):
    return i_blog.update(id,request,db)


@router.get('/', response_model=List[s_blog.ShowBlog])
def all(db: Session = Depends(get_db), get_current_user: s_user.User = Depends(get_current_user)):
    return i_blog.get_all(db)


@router.get('/{id}', status_code=200, response_model=s_blog.ShowBlog)
def show(id: int, db: Session = Depends(get_db), get_current_user: s_user.User = Depends(get_current_user)):
    return i_blog.show(id,db)