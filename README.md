
## To-Do List Application
A simple and intuitive To-Do List application built with Flask, SQLAlchemy, and Flask-Login. This app allows users to manage their tasks efficiently, track their completion status, and set priorities and due dates.

# Table of Contents
 Features
 Technologies
 Installation
 Usage
 Contributing
 License
# Features
 User authentication (registration, login, logout)
 Create, edit, and delete tasks
 Set task priorities and due dates
 Filter tasks by status (completed, incomplete)
 Export tasks to a CSV file
 View task analytics (total, completed, overdue)
# Technologies
 Frontend: HTML, CSS (Bootstrap)
 Backend: Flask
 Database: SQLite
 Authentication: Flask-Login
 ORM: SQLAlchemy
 Data Export: Pandas
 Environment Management: dotenv
## Installation
# Prerequisites
Python 3.x
pip (Python package installer)
# Steps
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/todo-list-app.git
cd todo-list-app
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Set up your environment variables: Create a .env file in the root directory and add the following:

env
Copy code
SECRET_KEY=your_secret_key
MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_email_password
Initialize the database:

bash
Copy code
flask run
Usage
Run the application:

bash
Copy code
flask run
The app will be available at http://127.0.0.1:5000/.

Register a new account or log in with existing credentials.

Start adding tasks to your To-Do List!

Use the filter options to view completed or incomplete tasks.

Export your tasks to a CSV file from the analytics section.

# Contributing
Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request.

# Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push to the branch and create a pull request.
# License
This project is licensed under the MIT License. See the LICENSE file for details.

