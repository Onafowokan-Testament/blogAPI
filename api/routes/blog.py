import datetime

from bson import ObjectId
from fastapi import APIRouter

from config.config import blog_collections
from models.blog_model import BlogModel, UpdatedBlogModel
from serializer.blog import DecodeBlog, DecodeBlogs

blog_root = APIRouter(tags=["blog"])


@blog_root.post("/new/blog")
def post_blog(blog: BlogModel):
    blog = dict(blog)
    current_date = datetime.date.today()
    blog["current_date"] = str(current_date)

    new_blog = blog_collections.insert_one(blog)
    doc_id = str(new_blog.inserted_id)

    return {"res": "ok", "message": "blog posted successfully", "id": doc_id}


@blog_root.get("/get/{_id}")
def get_blog_by_id(_id: str):
    res = blog_collections.find_one({"_id": ObjectId(_id)})
    decoded_blog = DecodeBlog(res)
    return {"status": "ok", "data": decoded_blog}


@blog_root.get("/all/blogs")
async def get_all_blogs():
    res = blog_collections.find()
    decoded_blog = DecodeBlogs(res)
    return {"status": "ok", "data": decoded_blog, "other_data": res}


@blog_root.patch("/post/{_id}")
def update_post(_id: str, blog: UpdatedBlogModel):
    req = dict(blog.model_dump(exclude_unset=True))
    blog_collections.find_one_and_update({"_id": ObjectId(_id)}, {"$set": req})
    return {"status": "ok", "message": "Blog updated successfully"}


@blog_root.delete("/posts/{_id}")
def delete_blog(_id: str):
    blog_collections.find_one_and_delete({"_id": ObjectId(_id)})

    return {"status": "ok", "message": "successfuly deleted"}
