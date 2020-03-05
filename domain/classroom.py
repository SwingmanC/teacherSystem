from .__init__ import db
class Classroom(db.Model):
    __tablename__ = 'classrooms'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)

    students = db.relationship('Student',backref='classroom')
    courses = db.relationship('Course',backref='classroom')

    def __repr__(self):
        return '<classroom: %s>' % self.name

