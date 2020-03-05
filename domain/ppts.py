from .__init__ import db
class PPTs(db.Model):
    __tablename__  = 'ppts'

    id =db.Column(db.Integer,primary_key=True)
    filename = db.Column(db.String(255),nullable=False)
    course_id = db.Column(db.Integer,db.ForeignKey('courses.id'))

    def __repr__(self):
        return '<ppt: %s %s>' %(self.filename,self.course_id)
