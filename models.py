import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db.init_app(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    date = db.Column('Date', db.DateTime, default=datetime.datetime.now)
    skills = db.Column('Skills', db.Text)
    repo_link = db.Column('Repo Link', db.Text)
    description = db.Column('Description', db.Text)

    def __repr__(self):
        return f"""
                \rTitle: {self.title}
                \rDate: {self.date}
                \rSkills: {self.skills}
                \rRepo: {self.repo_link}
                \rDescription: {self.description}
                """
