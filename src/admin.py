from .client import app
from flask import render_template

@app.route('/admin/home')
def home_admin():
    return render_template('admin/home.html')