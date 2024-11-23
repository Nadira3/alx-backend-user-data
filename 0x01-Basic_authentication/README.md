# 0x01. Basic Authentication  

This project focuses on implementing basic authentication mechanisms for backend applications. It is part of the **ALX Backend User Data** curriculum and introduces the foundational concepts of securing APIs with authentication.  

## Learning Objectives  
By completing this project, you will:  
- Understand the purpose of authentication and how it works.  
- Learn about Base64 encoding and how it is used in Basic Authentication.  
- Implement Basic Authentication in a Python web framework.  
- Validate user credentials securely.  

## Technologies Used  
- **Language:** Python  
- **Framework:** Flask  
- **Tools/Libraries:**  
  - `base64` for encoding and decoding credentials.  
  - `bcrypt` for secure password hashing.  
  - `uuid` for generating unique user tokens.  

## Project Tasks  
### 1. Simple API  
- Implement a simple Flask application with public routes.  

### 2. Base64 Encode/Decode  
- Write functions to encode and decode data using Base64.  

### 3. Basic Authentication Header  
- Parse the `Authorization` header to extract the username and password.  

### 4. Validate Credentials  
- Create a user model and validate credentials securely.  

### 5. Protect Routes  
- Use the Basic Authentication mechanism to protect specific routes in your application.  

### 6. User Management  
- Add functionality to register and manage user accounts.  

## Setup and Installation  
To run this project locally:  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/PreciousAitanun/alx-backend-user-data.git  
   cd 0x01-Basic_authentication
   ```

2. Set up a virtual environment and install dependencies:
```
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt
```

3. Run the application:
```
python3 app.py
```


## Usage

Use an API testing tool (like Postman) or curl to test the endpoints.

Include the Authorization header in your requests in the format:

Authorization: Basic <Base64-encoded credentials>

Replace <Base64-encoded credentials> with a Base64-encoded string of username:password.


## Example Request

curl -X GET http://127.0.0.1:5000/protected -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ="

License

Developed as part of the ALX Software Engineering Program.



