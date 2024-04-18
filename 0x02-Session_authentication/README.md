# 0. Et moi et moi et moi!

## Introduction

This project is a continuation of the 0x06. Basic authentication project. In this version, we have implemented a Basic authentication for giving you access to all User endpoints:

- GET /api/v1/users
- POST /api/v1/users
- GET /api/v1/users/<user_id>
- PUT /api/v1/users/<user_id>
- DELETE /api/v1/users/<user_id>

We have added a new endpoint: GET /users/me to retrieve the authenticated User object.

## Setup

1. Copy all your work of the 0x06. Basic authentication project into this new folder.
2. Copy folders models and api from the previous project 0x06. Basic authentication

Please make sure all mandatory tasks of this previous project are done at 100% because this project (and the rest of this track) will be based on it.

## Updates

- Update @app.before_request in api/v1/app.py:
  - Assign the result of auth.current_user(request) to request.current_user
- Update method for the route GET /api/v1/users/<user_id> in api/v1/views/users.py:
  - If <user_id> is equal to me and request.current_user is None: abort(404)
  - If <user_id> is equal to me and request.current_user is not None: return the authenticated User in a JSON response (like a normal case of GET /api/v1/users/<user_id> where <user_id> is a valid User ID)
  - Otherwise, keep the same behavior

## Testing

You can test the application using the following commands:

```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
In a second terminal:
curl "http://0.0.0.0:5000/api/v1/status"
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
Repository
GitHub repository: alx-backend-user-data Directory: 0x02-Session_authentication File: api/v1/app.py, api/v1/views/users.py

1. Empty session
Introduction
In this task, we create a class SessionAuth that inherits from Auth. For the moment this class will be empty. It’s the first step for creating a new authentication mechanism:

validate if everything inherits correctly without any overloading
validate the “switch” by using environment variables
Updates
Update api/v1/app.py for using SessionAuth instance for the variable auth depending of the value of the environment variable AUTH_TYPE, If AUTH_TYPE is equal to session_auth:

import SessionAuth from api.v1.auth.session_auth
create an instance of SessionAuth and assign it to the variable auth
Otherwise, keep the previous mechanism.
Testing
You can test the application using the following commands:

API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
