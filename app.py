from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Dummy user data (In a real app, use a database)
users = {}

# Dummy budget data stored in session (in a real app, use a database)
@app.before_request
def setup_session():
    if 'budget' not in session:
        session['budget'] = []

# Home route (index page)
@app.route('/')
def home():
    return render_template('index.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username already exists
        if username in users:
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        # Hash the password and store it
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        users[username] = hashed_password
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username exists
        if username not in users:
            flash('Username does not exist!', 'danger')
            return redirect(url_for('login'))
        
        # Check if the password matches
        if check_password_hash(users[username], password):
            flash('Login successful!', 'success')
            return redirect(url_for('budget'))
        else:
            flash('Incorrect password!', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

# Budget page route - Manage income and expenses
@app.route('/budget', methods=['GET', 'POST'])
def budget():
    if request.method == 'POST':
        # Retrieve the transaction type (string), amount, and date
        transaction_type = request.form['transaction_type']
        amount = float(request.form['amount'])
        date = request.form['date']
        
        # Create a dictionary for the transaction
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'date': date
        }
        
        # Save the transaction to the session
        session['budget'].append(transaction)
        session.modified = True  # Ensure the session is marked as modified
        
        flash(f'Transaction "{transaction_type}" added successfully!', 'success')
        return redirect(url_for('budget'))
    
    # Retrieve the transactions from the session
    transactions = session['budget']
    return render_template('budget.html', transactions=transactions)

if __name__ == "__main__":
    app.run(debug=True)
