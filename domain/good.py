from .__init__ import db


class Good(db.Model):

    __tablename__ = 'goods'

    id = db.Column(db.Integer,primary_key=True)
    student_name = db.Column(db.String(255),db.ForeignKey('students.username'))
    discuss_id = db.Column(db.Integer,db.ForeignKey('discusses.id'))

