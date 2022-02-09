from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

from app.models import User
from app.internal.hashing import Hash
from app.internal.jwttoken import create_access_token


def login(request: OAuth2PasswordRequestForm, db:Session):

    user = db.query(User).filter(User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid password')

    # Generate JWT token
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}