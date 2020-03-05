from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@127.0.0.1:3306/teachSystem?charset=utf8"
db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'students'

    username = db.Column(db.String(255),primary_key=True)
    password = db.Column(db.String(16),nullable=False)
    telephone = db.Column(db.String(11),nullable=False)
    email = db.Column(db.String(255),nullable=False)
    classroom_id = db.Column(db.Integer,db.ForeignKey('classrooms.id'))

    results = db.relationship('Result', backref='student')
    discusses = db.relationship('Discuss',backref='student')

    def __repr__(self):
        return '<Student: %s %s %s %s>' %(self.username,self.telephone,self.email,self.classroom_id)


class Course(db.Model):
    __tablename__  = 'courses'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    teacher_name = db.Column(db.String(255),db.ForeignKey('teachers.username'))
    classroom_id = db.Column(db.Integer,db.ForeignKey('classrooms.id'))

    ppts = db.relationship('PPTs',backref='course')
    films = db.relationship('Films',backref='course')
    homework = db.relationship('Homework',backref='course')
    results = db.relationship('Result',backref='course')
    debates = db.relationship('Debate',backref='course')

    def __repr__(self):
        return '<Course: %s %s %s>' %(self.name,self.teacher_name,self.classroom_id)


class Debate(db.Model):

    __tablename__ = 'debates'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.Text,nullable=False)
    time = db.Column(db.String(255),nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    discusses = db.relationship('Discuss',backref='debate')

    def __repr__(self):
        return '<debate: %s %s>' %(self.title,self.course_id)


class Discuss(db.Model):

    __tablename__ = 'discusses'

    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.Text,nullable=False)
    time = db.Column(db.String(255), nullable=False)
    student_name = db.Column(db.String(255),db.ForeignKey('students.username'))
    debate_id = db.Column(db.Integer,db.ForeignKey('debates.id'))

    def __repr__(self):
        return '<discuss: %s %s %s %s>' %(self.text,self.time,self.student_name,self.debate_id)


class Good(db.Model):

    __tablename__ = 'goods'

    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(255), db.ForeignKey('students.username'))
    discuss_id = db.Column(db.Integer, db.ForeignKey('discusses.id'))


db.create_all()


@app.route('/')
def hello_world():
    return 'success'


if __name__ == 'main':
    app.run()