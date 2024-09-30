import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key')  # Use an env variable for the secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Set up login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Define User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

# Define Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    category = db.Column(db.String(50), nullable=True)
    recurring = db.Column(db.Boolean, default=False)
    recurrence_freq = db.Column(db.String(20), nullable=True)

# Create the database
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    search_query = request.args.get('search')
    filter_status = request.args.get('filter', 'all')
    
    todos = Todo.query.filter_by(user_id=current_user.id)

    if search_query:
        todos = todos.filter(Todo.task.contains(search_query))
    
    if filter_status == 'completed':
        todos = todos.filter_by(completed=True)
    elif filter_status == 'incomplete':
        todos = todos.filter_by(completed=False)
    
    todos = todos.order_by(Todo.priority).all()
    
    return render_template('index.html', todos=todos, search_query=search_query, filter_status=filter_status)

@app.route('/add', methods=['POST'])
@login_required
def add_todo():
    task = request.form.get('todo')
    priority = request.form.get('priority', type=int)
    due_date = request.form.get('due_date', type=str)
    category = request.form.get('category')
    recurring = request.form.get('recurring') == 'on'
    recurrence_freq = request.form.get('recurrence_freq')

    if task:
        new_todo = Todo(task=task, priority=priority, user_id=current_user.id, category=category, recurring=recurring, recurrence_freq=recurrence_freq)
        
        if due_date:
            try:
                new_todo.due_date = datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                flash('Invalid date format. Please use YYYY-MM-DD.', 'danger')
                return redirect(url_for('index'))
        
        db.session.add(new_todo)
        db.session.commit()
        flash('To-Do added successfully!', 'success')
        
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
@login_required
def edit_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if request.method == 'POST':
        todo.task = request.form.get('todo')
        todo.priority = request.form.get('priority', type=int)
        due_date = request.form.get('due_date', type=str)
        todo.category = request.form.get('category')
        todo.recurring = request.form.get('recurring') == 'on'
        todo.recurrence_freq = request.form.get('recurrence_freq')

        if due_date:
            try:
                todo.due_date = datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                flash('Invalid date format. Please use YYYY-MM-DD.', 'danger')
                return redirect(url_for('edit_todo', todo_id=todo_id))

        db.session.commit()
        flash('To-Do updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit.html', todo=todo)

@app.route('/delete/<int:todo_id>')
@login_required
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        flash('To-Do deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
@login_required
def complete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        todo.completed = not todo.completed
        db.session.commit()
        flash('To-Do status updated!', 'success')
    return redirect(url_for('index'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        if username:
            current_user.username = username
        if email:
            current_user.email = email
        if password:
            current_user.password = generate_password_hash(password, method='pbkdf2:sha256')
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    return render_template('profile.html', user=current_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful! Welcome back!', 'success')
            return redirect(url_for('index'))
        flash('Login failed. Check your username and/or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/export')
@login_required
def export_todos():
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    data = [{"Task": todo.task, "Priority": todo.priority, "Due Date": todo.due_date, "Completed": todo.completed} for todo in todos]
    df = pd.DataFrame(data)
    df.to_csv('todos.csv', index=False)
    flash('Tasks exported successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/analytics')
@login_required
def analytics():
    total_tasks = Todo.query.filter_by(user_id=current_user.id).count()
    completed_tasks = Todo.query.filter_by(user_id=current_user.id, completed=True).count()
    overdue_tasks = Todo.query.filter(
        Todo.user_id == current_user.id,
        Todo.completed == False,
        Todo.due_date < datetime.now()
    ).count()
    return render_template('analytics.html', total=total_tasks, completed=completed_tasks, overdue=overdue_tasks)

if __name__ == "__main__":
    app.run(debug=True)
