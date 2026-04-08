# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Design and build a complete REST API using FastAPI framework that demonstrates core concepts like routing, request/response handling, data validation, and error management. You will create a functional API that can handle CRUD operations and serves as a solid foundation for web service development.

## 📝 Tasks

### 🛠️ Setup FastAPI Project and Create Basic Routes

#### Description
Initialize a FastAPI project and create the foundational API structure with basic GET and POST routes. You should understand how FastAPI handles HTTP methods and how to define endpoints.

#### Requirements
Completed program should:

- Import FastAPI and create an application instance
- Define at least 2 GET routes (e.g., root endpoint and a resource retrieval endpoint)
- Define at least 1 POST route to accept and process data
- Use appropriate HTTP status codes for responses
- Include descriptive docstrings for each route


### 🛠️ Implement Data Validation and Request/Response Models

#### Description
Create Pydantic models for request and response data to enforce type validation and consistency. This ensures data integrity and provides automatic API documentation.

#### Requirements
Completed program should:

- Define at least 2 Pydantic models (e.g., for request input and response output)
- Use type hints in all function parameters and returns
- Implement validation rules (e.g., min/max lengths, required fields)
- Test that invalid data is rejected with appropriate error messages
- Ensure responses return the correct model structure


### 🛠️ Implement CRUD Operations

#### Description
Develop complete CRUD (Create, Read, Update, Delete) operations for a resource. Use path parameters and query parameters appropriately based on operation type.

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve all resources
- Implement GET endpoint with path parameter to retrieve a single resource
- Implement PUT or PATCH endpoint to update resource data
- Implement DELETE endpoint to remove a resource
- Use in-memory storage (e.g., list or dictionary) to persist data during API runtime
- Return appropriate status codes (200, 201, 204, 404, etc.)


### 🛠️ Add Error Handling and Documentation

#### Description
Implement comprehensive error handling and provide clear API documentation. FastAPI auto-generates Swagger UI documentation, but you should handle edge cases gracefully.

#### Requirements
Completed program should:

- Implement try-except blocks or FastAPI exception handlers for error cases
- Return meaningful error messages with appropriate HTTP status codes
- Handle cases like resource not found (404) and invalid input (400)
- Include the `response_model` parameter in route decorators for automatic documentation
- Add descriptions to route parameters and request body fields
- Test the Swagger UI documentation at `/docs` endpoint
