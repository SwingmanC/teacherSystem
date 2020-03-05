from .__init__ import db
from .reviews import Review

class Films(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer,primary_key=True)
    filename = db.Column(db.String(255),nullable=False)
    course_id = db.Column(db.Integer,db.ForeignKey('courses.id'))

    reviews = db.relationship('Review',backref='film')

    def __repr__(self):
        return '<film: %s %s>' %(self.filename,self.course_id)
