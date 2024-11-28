# 1 1 doc


def DecodeBlog(doc) -> dict:
    return {
        "_id": str(doc["_id"]),
        "title": doc["title"],
        "subtitle": doc["subtitle"],
        "content": doc["content"],
        "author": doc["author"],
        "date": doc["current_date"],
    }


# all blogs
def DecodeBlogs(docs) -> list:
    return [DecodeBlog(doc) for doc in docs]
