from flask import Flask, render_template, request, redirect, url_for
from models import db, Note

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db.init_app(app)


@app.before_request
def create_tables():
    db.create_all()


@app.route('/')
def index():
    notes = Note.query.order_by(Note.importance.desc()).all()
    return render_template('index.html', notes=notes)


@app.route('/add', methods=['POST'])
def add_note():
    text = request.form['text']
    importance = int(request.form['importance'])
    note = Note(text=text, importance=importance)
    db.session.add(note)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    note = db.session.get(Note, note_id)
    if request.method == 'POST':
        note.text = request.form['text']
        note.importance = request.form['importance']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', note=note)


@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    note = db.session.get(Note, note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
