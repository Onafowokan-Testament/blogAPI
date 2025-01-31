# Blog API with FastAPI and MongoDB 📝

Welcome to the **Blog API**! This FastAPI-based application allows users to create, read, update, and delete blog posts. It integrates with **MongoDB** for data storage and provides a simple yet powerful interface for managing blog content.

---

## Features

- **Create Blog Posts**: Add new blog posts with a title, content, and publication date.
- **Fetch Blog Posts**: Retrieve a single blog post by its ID or all blog posts.
- **Update Blog Posts**: Modify existing blog posts.
- **Delete Blog Posts**: Remove blog posts from the database.
- **MongoDB Integration**: Uses MongoDB for efficient and scalable data storage.

---

## How It Works

1. **Create a Blog Post**: Send a POST request to `/new/blog` with the blog details.
2. **Fetch a Blog Post**: Send a GET request to `/get/{_id}` to retrieve a specific blog post.
3. **Fetch All Blog Posts**: Send a GET request to `/all/blogs` to retrieve all blog posts.
4. **Update a Blog Post**: Send a PATCH request to `/post/{_id}` with the updated fields.
5. **Delete a Blog Post**: Send a DELETE request to `/posts/{_id}` to remove a blog post.

---

## Installation

To run this API locally, follow these steps:

### Prerequisites

- Python 3.8 or higher
- FastAPI
- MongoDB
- Uvicorn (for running the FastAPI server)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/blog-api.git
   cd blog-api
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MongoDB**:
   - Ensure MongoDB is installed and running.
   - Update the `blog_collections` configuration in `config/config.py` to point to your MongoDB instance.

4. **Run the FastAPI server**:
   ```bash
   uvicorn app:blog_root --reload
   ```

---

## API Endpoints

### Create a Blog Post
- **Endpoint**: `POST /new/blog`
- **Request Body**:
  ```json
  {
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post."
  }
  ```
- **Response**:
  ```json
  {
    "res": "ok",
    "message": "blog posted successfully",
    "id": "65f4c1e2b4f4d7e8f4d7e8f4"
  }
  ```

### Fetch a Blog Post by ID
- **Endpoint**: `GET /get/{_id}`
- **Response**:
  ```json
  {
    "status": "ok",
    "data": {
      "_id": "65f4c1e2b4f4d7e8f4d7e8f4",
      "title": "My First Blog Post",
      "content": "This is the content of my first blog post.",
      "current_date": "2023-10-15"
    }
  }
  ```

### Fetch All Blog Posts
- **Endpoint**: `GET /all/blogs`
- **Response**:
  ```json
  {
    "status": "ok",
    "data": [
      {
        "_id": "65f4c1e2b4f4d7e8f4d7e8f4",
        "title": "My First Blog Post",
        "content": "This is the content of my first blog post.",
        "current_date": "2023-10-15"
      }
    ]
  }
  ```

### Update a Blog Post
- **Endpoint**: `PATCH /post/{_id}`
- **Request Body**:
  ```json
  {
    "title": "Updated Blog Post Title"
  }
  ```
- **Response**:
  ```json
  {
    "status": "ok",
    "message": "Blog updated successfully"
  }
  ```

### Delete a Blog Post
- **Endpoint**: `DELETE /posts/{_id}`
- **Response**:
  ```json
  {
    "status": "ok",
    "message": "successfuly deleted"
  }
  ```

---

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the modern and fast web framework.
- [MongoDB](https://www.mongodb.com/) for the scalable NoSQL database.
- [Uvicorn](https://www.uvicorn.org/) for the ASGI server.

---

Build and manage your blog with ease using the Blog API! 🚀📚
