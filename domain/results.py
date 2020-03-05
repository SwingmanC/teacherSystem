from .__init__ import db


class Result(db.Model):

    __tablename__ = 'results'

    id = db.Column(db.Integer,primary_key=True)
    filename = db.Column(db.String(255),nullable=False)
    student_name = db.Column(db.String(255),db.ForeignKey('students.username'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    homework_id = db.Column(db.Integer,db.ForeignKey('homework.id'))

    def __repr__(self):
        return '<result: %s %s %s %s>' %(self.filename,self.student_name,self.course_id,self.homework_id)
