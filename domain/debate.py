from .__init__ import db
from .discuss import Discuss


class Debate(db.Model):

    __tablename__ = 'debates'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.Text,nullable=False)
    time = db.Column(db.String(255),nullable=False)
    discuss_count = db.Column(db.Integer,nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    discusses = db.relationship('Discuss',backref='debate')

    def __repr__(self):
        return '<debate: %s %s>' %(self.subject,self.course_id)
