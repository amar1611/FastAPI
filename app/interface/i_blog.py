from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import Blog
from app.schemas import s_blog


def create(request: s_blog.Blog, db: Session):

    new_blog = Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id:int , db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id: {id} not found')

    blog.delete(synchronize_session=False)
    db.commit()
    return {'status': 'done'}

def update(id:int , request: s_blog.Blog, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id: {id} not found')
    
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return 'updated'

def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs


def show(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id: {id} not found')
    return blog