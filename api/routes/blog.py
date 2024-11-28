import datetime

from fastapi import APIRouter

from config.config import blog_collections
from models.blog_model import BlogModel

blog_root = APIRouter(tags=["blog"])


@blog_root.post("/new/blog")
def post_blog(blog: BlogModel):
    blog = dict(blog)
    current_date = datetime.date.today()
    blog["current_date"] = str(current_date)

    new_blog = blog_collections.insert_one(blog)
    doc_id = str(new_blog.inserted_id)

    return {"res": "ok", "message": "blog posted successfully", "id": doc_id}
