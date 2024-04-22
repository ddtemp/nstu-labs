from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(30), nullable=False)
    importance = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Заметка {self.text}'
