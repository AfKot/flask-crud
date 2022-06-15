from application import app, db
from application.models import ToDo
from flask import redirect, url_for

@app.route('/')
def index():
    todo = ToDo.query.all()
    empstr = ""
    for t_name in todo:
        empstr += f'{t_name.id} {t_name.task_name} {t_name.completed} <br>'
    return empstr

@app.route('/add/<t_name>')
def add(t_name):
    task = ToDo(task_name=t_name) 
    db.session.add(task)
    db.session.commit()
    return "Added to ToDo List"

@app.route('/complete/<int:id>')
def complete(id):
    todo = ToDo.query.get(id)
    todo.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>/<newtask>')
def update(id, newtask):
    todo = ToDo.query.get(id)
    todo.task_name = newtask
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<t_name>')
def delete(t_name):
    task_del = ToDo.query.filter_by(task_name=t_name).first()
    db.session.delete(task_del)
    db.session.commit()
    return redirect(url_for('index'))