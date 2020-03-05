from .__init__ import db
from .results import Result


class Homework(db.Model):

    __tablename__ = 'homework'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    results = db.relationship('Result', backref='homework')

    def __repr__(self):
        return '<homework: %s %s>' % (self.filename, self.course_id)
