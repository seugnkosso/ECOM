from .client import app
from flask import render_template

@app.route('/admin')
def admin():
    return render_template('admin/home.html')