# To-Do List Application

A simple and intuitive To-Do List application built with Flask, SQLAlchemy, and Flask-Login. This app allows users to manage their tasks efficiently, track their completion status, and set priorities and due dates.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (registration, login, logout)
- Create, edit, and delete tasks
- Set task priorities and due dates
- Filter tasks by status (completed, incomplete)
- Export tasks to a CSV file
- View task analytics (total, completed, overdue)

## Technologies

- **Frontend**: HTML, CSS (Bootstrap)
- **Backend**: Flask
- **Database**: SQLite
- **Authentication**: Flask-Login
- **ORM**: SQLAlchemy
- **Data Export**: Pandas
- **Environment Management**: dotenv

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/todo-list-app.git
    cd todo-list-app
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up your environment variables**:  
   Create a `.env` file in the root directory and add the following:
    ```env
    SECRET_KEY=your_secret_key
    MAIL_USERNAME=your_email@example.com
    MAIL_PASSWORD=your_email_password
    ```

6. **Initialize the database**:
    ```bash
    flask run
    ```

## Usage

1. **Run the application**:
    ```bash
    flask run
    ```
   The app will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. **Register a new account or log in with existing credentials**.

3. **Start adding tasks to your To-Do List!**

4. **Use the filter options to view completed or incomplete tasks**.

5. **Export your tasks to a CSV file from the analytics section**.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request.

1. **Fork the repository**.
2. **Create a new branch for your feature or bug fix**.
3. **Make your changes and commit them**.
4. **Push to the branch and create a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
