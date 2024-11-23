# ALX Backend User Data Project

## Project Overview

This project focuses on handling personal data and logs in a secure and compliant manner. It consists of several tasks aimed at filtering and securing Personally Identifiable Information (PII), implementing logging mechanisms, and connecting to a secure database. This project will help solidify skills in Python, database connectivity, and secure handling of sensitive data.

## Tasks Overview

1. **Regex-ing**  
   Implement a function that uses regex to obfuscate specified fields in a log message.

2. **Log Formatter**  
   Create a custom logging formatter that redacts PII fields in logs.

3. **Create Logger**  
   Set up a logger that filters out sensitive data and uses a custom formatter for logging PII data.

4. **Connect to Secure Database**  
   Implement a function to securely connect to a MySQL database and retrieve data using environment variables for credentials.

5. **Read and Filter Data**  
   Retrieve user data from the database and filter the sensitive fields such as name, email, phone, SSN, and password.

## Technologies Used

- Python 3.7
- MySQL Database
- Regular Expressions
- Logging module
- Environment Variables

## Setup Instructions

To set up and run the project, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/Nadira3/alx-backend-user-data.git
   ```

2. Install the required dependencies:
```
pip3 install -r requirements.txt
```

3. Set up your MySQL server and configure the database:
```
CREATE DATABASE IF NOT EXISTS my_db;
CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON my_db.* TO 'root'@'localhost';
```

4. Set environment variables for database credentials:
```
export PERSONAL_DATA_DB_USERNAME=root
export PERSONAL_DATA_DB_PASSWORD=root
export PERSONAL_DATA_DB_HOST=localhost
export PERSONAL_DATA_DB_NAME=my_db
```

5. Run the main script to test functionality:
```
python3 main.py
```


## Requirements

All files should be executable

Python code must comply with the PEP8 style guide (using pycodestyle)

Documentation for functions, classes, and modules is required

Type annotations for functions


## Example Usage

When you run the project, it will:

1. Filter log messages to obfuscate sensitive data.


2. Format logs using a custom redacting formatter.


3. Connect to a MySQL database using secure credentials and retrieve user data, filtering sensitive fields.



Example output for a filtered log:
```
[HOLBERTON] my_logger INFO 2024-11-19 18:24:25,105: name=***; email=***; ssn=***; password=***;
```
## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
