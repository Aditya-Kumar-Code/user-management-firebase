# user-management-firebase




Sure, here's a Postman collection for your FastAPI-based API, along with brief descriptions of each endpoint. You can import this collection into Postman to interact with your API.

### Postman Collection: FastAPI Firebase Auth

[Download Postman Collection](https://example.com/your-fastapi-collection-link)

#### Endpoints

**1. Sign Up**
- URL: `POST http://localhost:8000/signup`
- Description: Create a new user account.
- Request Body (JSON):
  ```json
  {
    "username": "user123",
    "email": "user123@example.com",
    "full_name": "User One",
    "created_at": "2023-11-07T12:00:00",
    "password": "password123"
  }
  ```
- Expected Response (Status 201 Created):
  ```json
  {
    "message": "User account created successfully for user user123"
  }
  ```

**2. Log In**
- URL: `POST http://localhost:8000/login`
- Description: Authenticate and obtain an access token.
- Request Body (JSON):
  ```json
  {
    "email": "user123@example.com",
    "password": "password123"
  }
  ```
- Expected Response (Status 200 OK):
  ```json
  {
    "token": "your_access_token"
  }
  ```

**3. Update User Profile**
- URL: `PUT http://localhost:8000/user/{user_id}`
- Description: Update a user's profile by providing a user ID in the URL.
- Request Body (JSON):
  Provide the fields you want to update (excluding password).
  ```json
  {
    "full_name": "Updated Name",
    "created_at": "2023-11-07T13:00:00"
  }
  ```
- Expected Response (Status 200 OK):
  Updated user object.

**4. Delete User Account**
- URL: `DELETE http://localhost:8000/user/{user_id}`
- Description: Delete a user's account by providing a user ID in the URL.
- Expected Response (Status 200 OK):
  ```json
  {
    "message": "User account deleted"
  }
  ```

**5. Validate Token**
- URL: `POST http://localhost:8000/ping`
- Description: Validate an access token by providing it in the `Authorization` header.
- Request Headers:
  - `Authorization: Bearer your_access_token`
- Expected Response (Status 200 OK):
  User's `user_id`.

#### Instructions:

1. **Sign Up**: Use this endpoint to create a new user account. Provide the required user data in the request body, including the username, email, full name, creation date, and password.

2. **Log In**: Authenticate and obtain an access token by providing the user's email and password. The access token will be returned in the response.

3. **Update User Profile**: Update a user's profile by sending a `PUT` request with the user's ID in the URL. Provide the fields you want to update in the request body.

4. **Delete User Account**: Delete a user's account by sending a `DELETE` request with the user's ID in the URL.

5. **Validate Token**: Validate an access token by sending a `POST` request with the token in the `Authorization` header. The user's `user_id` will be returned.

Please ensure you have the FastAPI server running locally on `http://localhost:8000` before using these endpoints. You should also replace the placeholder `"your_access_token"` with a valid access token obtained from the Log In endpoint.

I hope this Postman collection helps you interact with your FastAPI-based API.
