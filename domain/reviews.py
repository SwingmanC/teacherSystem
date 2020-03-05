from .__init__ import db

class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.Text,nullable=False)
    time = db.Column(db.String(255), nullable=False)
    student_name = db.Column(db.String(255),db.ForeignKey('students.username'))
    film_id = db.Column(db.Integer,db.ForeignKey('films.id'))

    def __repr__(self):
        return '<review: %s %s %s %s>' %(self.text,self.time,self.student_name,self.film_id)
