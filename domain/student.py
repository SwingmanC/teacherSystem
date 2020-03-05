from .__init__ import db
from .results import Result
from .discuss import Discuss


class Student(db.Model):
    __tablename__ = 'students'

    username = db.Column(db.String(255),primary_key=True)
    password = db.Column(db.String(16),nullable=False)
    telephone = db.Column(db.String(11),nullable=False)
    email = db.Column(db.String(255),nullable=False)
    classroom_id = db.Column(db.Integer,db.ForeignKey('classrooms.id'))

    results = db.relationship('Result', backref='student')
    discusses = db.relationship('Discuss',backref='student')

    def __repr__(self):
        return '<Student: %s %s %s %s>' %(self.username,self.telephone,self.email,self.classroom_id)

