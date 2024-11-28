from pydantic import BaseModel


class BlogModel(BaseModel):
    title: str
    subtitle: str
    content: str
    author: str
    tags: list[str]


class UpdatedBlogModel(BaseModel):
    title: str = None
    subtitle: str = None
    content: str = None
    author: str = None
    tags: list[str] = None
