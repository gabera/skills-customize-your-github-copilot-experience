"""
FastAPI REST API Starter Code

This is a template to help you get started building a REST API with FastAPI.
Complete the TODO sections to implement the required functionality.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# TODO: Initialize your FastAPI application
app = FastAPI(
    title="TODO: Add your API title",
    description="TODO: Add your API description",
    version="1.0.0"
)

# TODO: Define your Pydantic models for request/response validation
# Example:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float


# TODO: Create an in-memory data store (e.g., list or dictionary)
# Example:
# items_db = []


@app.get("/")
def read_root():
    """
    TODO: Implement the root endpoint.
    Should return a welcome message or basic API information.
    """
    return {"message": "Welcome to the FastAPI REST API"}


@app.get("/items/")
def read_items():
    """
    TODO: Implement a GET endpoint to retrieve all items.
    Should return a list of items from your data store.
    """
    pass


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    TODO: Implement a GET endpoint to retrieve a single item by ID.
    Should validate that the item exists and return 404 if not found.
    """
    pass


@app.post("/items/")
def create_item(item):
    """
    TODO: Implement a POST endpoint to create a new item.
    Should validate the input using your Pydantic model and store it.
    """
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int, item):
    """
    TODO: Implement a PUT endpoint to update an existing item.
    Should validate that the item exists and return 404 if not found.
    """
    pass


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """
    TODO: Implement a DELETE endpoint to remove an item.
    Should validate that the item exists and return 404 if not found.
    """
    pass


# To run the API locally:
# 1. Install FastAPI and Uvicorn: pip install fastapi uvicorn
# 2. Run the server: uvicorn starter-code:app --reload
# 3. Open the API documentation: http://localhost:8000/docs
