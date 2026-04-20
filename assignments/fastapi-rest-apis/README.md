# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI and Python. By completing this assignment, you will learn how to create endpoints, validate request data, and return structured JSON responses.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Set up a FastAPI project and create the base API with a health check route and one resource collection.

#### Requirements
Completed program should:

- Create a FastAPI app that runs locally with Uvicorn.
- Add a `GET /health` endpoint that returns a JSON status message.
- Add a `GET /items` endpoint that returns a list of sample items.

### 🛠️ Add CRUD Endpoints with Validation

#### Description
Expand your API to support creating, reading, updating, and deleting items using request validation.

#### Requirements
Completed program should:

- Define a Pydantic model for item data validation.
- Add `POST /items` to create a new item and return the created object.
- Add `GET /items/{item_id}` to retrieve a single item by ID.
- Add `PUT /items/{item_id}` to update an existing item.
- Add `DELETE /items/{item_id}` to remove an item and return a confirmation message.
