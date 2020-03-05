from .__init__ import db
from .homework import Homework
from .results import Result
from .debate import Debate


class Course(db.Model):
    __tablename__  = 'courses'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    teacher_name = db.Column(db.String(255),db.ForeignKey('teachers.username'))
    classroom_id = db.Column(db.Integer,db.ForeignKey('classrooms.id'))

    ppts = db.relationship('PPTs',backref='course')
    films = db.relationship('Films',backref='course')
    homework = db.relationship('Homework',backref='course')
    results = db.relationship('Result',backref='course')
    debates = db.relationship('Debate',backref='course')

    def __repr__(self):
        return '<Course: %s %s %s>' %(self.name,self.teacher_name,self.classroom_id)
