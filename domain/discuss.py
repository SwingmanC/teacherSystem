from .__init__ import db


class Discuss(db.Model):

    __tablename__ = 'discusses'

    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.Text,nullable=False)
    time = db.Column(db.String(255), nullable=False)
    good_count = db.Column(db.Integer,nullable=False)
    student_name = db.Column(db.String(255),db.ForeignKey('students.username'))
    debate_id = db.Column(db.Integer,db.ForeignKey('debates.id'))

    def __repr__(self):
        return '<discuss: %s %s %s %s>' %(self.text,self.time,self.student_name,self.debate_id)
