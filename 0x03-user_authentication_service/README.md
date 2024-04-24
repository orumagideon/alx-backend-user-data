# User Authentication Service

This project implements a user authentication service with various functionalities such as user registration, login, password reset, session management, and more. Below are the tasks and their corresponding implementations:

## Task 0: User Model

- Implemented a SQLAlchemy model named `User` for the `users` table with attributes such as `id`, `email`, `hashed_password`, `session_id`, and `reset_token`.

## Task 1: Create User

- Implemented the `add_user` method in the `DB` class to add a user to the database with email and hashed password.

## Task 2: Find User

- Implemented the `find_user_by` method in the `DB` class to find a user by arbitrary keyword arguments.

## Task 3: Update User

- Implemented the `update_user` method in the `DB` class to update a user's attributes in the database.

## Task 4: Hash Password

- Defined the `_hash_password` method in the `auth` module to hash a password using bcrypt.

## Task 5: Register User

- Implemented the `register_user` method in the `Auth` class to register a new user, hash the password, and save the user to the database.

## Task 6: Basic Flask App

- Created a basic Flask app with a single GET route ("/") returning a JSON payload.

## Task 7: Register User (Endpoint)

- Implemented the POST `/users` endpoint to register a user and respond with appropriate JSON payloads.

## Task 8: Credentials Validation

- Implemented the `valid_login` method in the `Auth` class to validate user credentials.

## Task 9: Generate UUIDs

- Implemented the `_generate_uuid` function in the `auth` module to generate UUIDs.

## Task 10: Get Session ID

- Implemented the `create_session` method in the `Auth` class to create a session ID for a user.

## Task 11: Log In

- Implemented the POST `/sessions` endpoint to handle user login and session creation.

## Task 12: Find User by Session ID

- Implemented the `get_user_from_session_id` method in the `Auth` class to find a user by session ID.

## Task 13: Destroy Session

- Implemented the `destroy_session` method in the `Auth` class to destroy a user's session.

## Task 14: Log Out

- Implemented the DELETE `/sessions` endpoint to handle user logout.

## Task 15: User Profile

- Implemented the GET `/profile` endpoint to retrieve a user's profile information.

## Task 16: Generate Reset Password Token

- Implemented the `get_reset_password_token` method in the `Auth` class to generate a reset password token.

## Task 17: Get Reset Password Token (Endpoint)

- Implemented the POST `/reset_password` endpoint to handle password reset token generation.

## Task 18: Update Password

- Implemented the `update_password` method in the `Auth` class to update a user's password.

## Task 19: Update Password (Endpoint)

- Implemented the PUT `/reset_password` endpoint to handle password updates.

## Task 20: End-to-End Integration Test

- Created a `main.py` module to perform end-to-end integration tests for various functionalities.

### Usage

To run the project, make sure to have Python and Flask installed. Then, clone the repository and run the Flask app using `python app.py`. You can then test the endpoints using tools like cURL or by running `python main.py`.

