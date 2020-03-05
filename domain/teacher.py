from .__init__ import db
class Teacher(db.Model):
    __tablename__ = 'teachers'

    username = db.Column(db.String(255),primary_key=True)
    password = db.Column(db.String(16),nullable=False)
    telephone = db.Column(db.String(11),nullable=False)
    email = db.Column(db.String(255),nullable=False)

    courses = db.relationship('Course',backref='teacher')

    def __repr__(self):
        return '<Teacher: %s %s %s>' %(self.username,self.telephone,self.email)

