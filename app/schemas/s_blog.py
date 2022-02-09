from pydantic import BaseModel

from app.schemas.s_user import ShowUser

class Blog(BaseModel):
    title: str
    body: str


class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser
    
    class Config():
        orm_mode = True