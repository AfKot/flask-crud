from application import app, db
from application.models import Games

@app.route('/add/<gname>')
def add(gname):
    new_game = Games(name=gname)
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<old_name>/<new_name>')
def update(old_name, new_name):
    old_name = Games.query.filter_by(name=old_name).first()
    old_name.name= new_name
    db.session.commit()
    return old_name.name

#@app.route('/update/<name>')
#def update(name):
#    first_game = Games.query.first()
#    first_game.name = name
#    db.session.commit()
#    return first_game.name

@app.route('/delete/<gname>')
def delete(gname):
    to_del = Games.query.filter_by(name=gname).first()
    db.session.delete(to_del)
    db.session.commit()
    return 'First entry deleted'

@app.route('/count')
def count():
    total = Games.query.count()
    return str(total)