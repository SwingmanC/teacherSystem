from flask import render_template,flash,request,redirect,url_for,send_from_directory,app,jsonify
from . import auth
import os
import time
from domain.__init__ import db
from domain.student import Student
from domain.teacher import Teacher
from domain.course import Course
from domain.classroom import Classroom
from domain.ppts import PPTs
from domain.films import Films
from domain.homework import Homework
from domain.reviews import Review
from domain.results import Result
from domain.debate import Debate
from domain.discuss import Discuss
from domain.good import Good
from werkzeug.utils import secure_filename


ALLOWED_EXTENTION1 = set(['ppt'])
ALLOWED_EXTENTION2 = set(['mp4','rmvb','flv','wmv','mkv'])
ALLOWED_EXTENTION3 = set(['doc','docx'])


def allowed_file_ppt(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENTION1


def allowed_file_film(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENTION2


def allowed_file_homework(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENTION3


@auth.route('/index', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_type = request.form.get('user_type')

        if not all([username,password]):
            flash('请补全用户信息')
        else:
            if user_type == "student":
                student = Student.query.filter_by(username=username, password=password).first()

                if student:
                    return redirect(url_for('auth.main_student',student_username=student.username))
                else:
                    flash('用户名不存在或密码错误')
            else:
                teacher = Teacher.query.filter_by(username=username,password=password).first()

                if teacher:
                    return redirect(url_for('auth.main_teacher',teacher_username=teacher.username))
                else:
                    flash('用户名不存在或密码错误')

    return render_template('login.html')


#AJAX
@auth.route('/check_student_username')
def check_student_username():

    username = request.args.get('username')

    student = Student.query.filter_by(username=username).first()

    if student:
        return jsonify("exist")
    else:
        return jsonify("valid")


#AJAX
@auth.route('/check_teacher_username')
def check_teacher_username():
    username = request.args.get('username')

    teacher = Teacher.query.filter_by(username=username).first()

    if teacher:
        return jsonify("exist")
    else:
        return jsonify("valid")


@auth.route('/register_student',methods=['GET','POST'])
def register_student():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        telephone = request.form.get('telephone')
        email = request.form.get('email')
        classroom_id = request.form.get('classroom')

        student = Student.query.filter_by(username=username).first()

        if not all([username,password,telephone,email,classroom_id]):
            flash('请补全用户信息')

        else:
            if student:
                flash('该用户名已存在')
            else:
                try:
                    new_student = Student(username=username, password=password, telephone=telephone,
                                          email=email,classroom_id=classroom_id)
                    db.session.add(new_student)
                    db.session.commit()
                    return render_template('auth/templates/login.html')
                except Exception as e:
                    print(e)
                    flash('添加用户失败')
                    db.session.rollback()

    return render_template('register_student.html')


@auth.route('/register_teacher',methods=['GET','POST'])
def register_teacher():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        telephone = request.form.get('telephone')
        email = request.form.get('email')

        teacher = Teacher.query.filter_by(username=username).first()

        if not all([username,password,telephone,email]):
            flash('请补全用户信息')

        else:
            if teacher:
                flash('该用户名已存在')
            else:
                try:
                    new_teacher = Student(username=username, password=password, telephone=telephone,
                                          email=email)
                    db.session.add(new_teacher)
                    db.session.commit()
                    return render_template('auth/templates/login.html')
                except Exception as e:
                    print(e)
                    flash('添加用户失败')
                    db.session.rollback()

    return render_template('register_teacher.html')


@auth.route('/main_student/<student_username>',methods=['GET','POST'])
def main_student(student_username):

    student = Student.query.filter_by(username=student_username).first()

    return render_template('main_student.html',student=student)


@auth.route('/main_teacher/<teacher_username>',methods=['GET','POST'])
def main_teacher(teacher_username):

    teacher = Teacher.query.filter_by(username=teacher_username).first()

    return render_template('main_teacher.html',teacher=teacher)


@auth.route('/add_course/<teacher_username>',methods=['GET','POST'])
def add_course(teacher_username):

    teacher = Teacher.query.filter_by(username=teacher_username).first()

    if request.method == 'POST':

        name = request.form.get('course_name')
        classroom_id = request.form.get('classroom_id')

        classroom = Classroom.query.filter_by(id=classroom_id)
        print(classroom)

        if not all([name,classroom_id]):
            flash('请补全课程信息')
        elif classroom is None:
            flash('该班级不存在')
        else:
            try:
                new_course = Course(name=name,teacher_name=teacher_username,classroom_id=classroom_id)
                db.session.add(new_course)
                db.session.commit()
                #D:\PycharmProjects\teachSystem\static\ppt
                os.mkdir('D:\\PycharmProjects\\teachSystem\\auth\\static\\ppt\\%s' %(name))
                os.mkdir('D:\\PycharmProjects\\teachSystem\\auth\\static\\film\\%s' %(name))
                os.mkdir('D:\\PycharmProjects\\teachSystem\\auth\\static\\homework\\%s' %(name))
                flash('课程添加成功')
            except Exception as e:
                print(e)
                flash('课程添加失败')
                db.session.rollback()

    return render_template('add_course.html',teacher=teacher)


@auth.route('/delete_course/<teacher_username>/<course_id>',methods=['GET','POST'])
def delete_course(teacher_username,course_id):

    course = Course.query.get(course_id)

    if course:
        try:
            db.session.delete(course)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除课程出错')
            db.session.rollback()
    else:
        flash('课程不存在')

    return redirect(url_for('main_teacher',teacher_username=teacher_username))


@auth.route('/update_teacher/<teacher_username>',methods=['GET','POST'])
def update_teacher(teacher_username):

    teacher = Teacher.query.filter_by(username=teacher_username).first()

    if request.method == 'POST':

        password = request.form.get('password')
        telephone = request.form.get('telephone')
        email = request.form.get('email')

        try:
            teacher.password = password
            teacher.telephone = telephone
            teacher.email = email
            db.session.commit()
        except Exception as e:
            print(e)
            flash('修改个人信息失败')
            db.session.rollback()

    return render_template('update_teacher.html',teacher=teacher)


@auth.route('/update_student/<student_username>',methods=['GET','POST'])
def update_student(student_username):

    student = Student.query.filter_by(username=student_username).first()

    if request.method == 'POST':

        password = request.form.get('password')
        telephone = request.form.get('telephone')
        email = request.form.get('email')

        try:
            student.password = password
            student.telephone = telephone
            student.email = email
            db.session.commit()
        except Exception as e:
            print(e)
            flash('修改个人信息失败')
            db.session.rollback()

    return render_template('update_student.html',student=student)


@auth.route('/teacher_course/<teacher_username>/<course_id>',methods=['GET','POST'])
def teacher_course(teacher_username,course_id):

    teacher = Teacher.query.filter_by(username=teacher_username).first()
    course = Course.query.get(course_id)
    ppts = PPTs.query.filter_by(course_id=course_id).all()
    films = Films.query.filter_by(course_id=course_id).all()
    homeworks = Homework.query.filter_by(course_id=course_id).all()

    return render_template('teacher_course.html',teacher=teacher,course=course,ppts=ppts,films=films,homeworks=homeworks)


@auth.route('/student_course/<student_username>/<course_id>',methods=['GET','POST'])
def student_course(student_username,course_id):

    student = Student.query.filter_by(username=student_username).first()
    course = Course.query.get(course_id)
    ppts = PPTs.query.filter_by(course_id=course_id).all()
    films = Films.query.filter_by(course_id=course_id).all()
    homeworks = Homework.query.filter_by(course_id=course_id).all()

    return render_template('student_course.html',student=student,course=course,ppts=ppts,films=films,homeworks=homeworks)


@auth.route('/manage_course_ppt/<teacher_username>/<course_id>',methods=['GET','POST'])
def manage_course_ppt(teacher_username,course_id):

    teacher = Teacher.query.filter_by(username=teacher_username).first()
    course = Course.query.get(course_id)

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file_ppt(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('D:/PycharmProjects/teachSystem/auth/static/ppt/%s/' %course.name,filename))
            new_ppt = PPTs(filename=filename, course_id=course_id)
            db.session.add(new_ppt)
            db.session.commit()
            flash('ppt上传成功')
        else:
            flash('文件不存在或文件格式错误')

    return render_template('manage_course_ppt.html',teacher=teacher,course=course)


@auth.route('/manage_course_film/<teacher_username>/<course_id>', methods=['GET', 'POST'])
def manage_course_film(teacher_username, course_id):

    teacher = Teacher.query.filter_by(username=teacher_username).first()
    course = Course.query.get(course_id)

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file_film(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('D:/PycharmProjects/teachSystem/auth/static/film/%s/' %course.name,filename))
            new_film = Films(filename=filename,course_id=course_id)
            db.session.add(new_film)
            db.session.commit()
            flash('视频上传成功')
        else:
            flash('文件不存在或文件格式错误')

    return render_template('manage_course_film.html',teacher=teacher,course=course)


@auth.route('/manage_course_homework/<teacher_username>/<course_id>', methods=['GET', 'POST'])
def manage_course_homework(teacher_username,course_id):

    teacher = Teacher.query.filter_by(username=teacher_username).first()
    course = Course.query.get(course_id)

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file_homework(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('D:/PycharmProjects/teachSystem/auth/static/homework/%s/' %course.name,filename))
            new_homework = Homework(filename=filename,course_id=course_id)
            db.session.add(new_homework)
            db.session.commit()
            flash('作业上传成功')
        else:
            flash('文件不存在或文件格式错误')

    return render_template('manage_course_homework.html',teacher=teacher,course=course)


@auth.route('/teacher_debate/<teacher_username>/<course_id>',methods=['GET', 'POST'])
def teacher_debate(teacher_username,course_id):

    teacher = Teacher.query.filter_by(username=teacher_username).first()
    course = Course.query.get(course_id)
    debates = Debate.query.filter_by(course_id=course_id).all()

    return render_template('teacher_debate.html',teacher=teacher,course=course,debates=debates)


@auth.route('/teacher_main_debate/<teacher_username>/<course_id>/<debate_id>',methods=['GET','POST'])
def teacher_main_debate(teacher_username,course_id,debate_id):

    teacher = Teacher.query.filter_by(username=teacher_username).first()
    course = Course.query.get(course_id)
    debate = Debate.query.filter_by(id=debate_id).first()
    dicusses = Discuss.query.filter_by(debate_id=debate_id).all()

    return render_template('teacher_main_debate.html',teacher=teacher,course=course,debate=debate,discusses=dicusses)


@auth.route('/tea_upload_ppt/<course_id>/<ppt_id>',methods=['GET','POST'])
def tea_upload_ppt(course_id,ppt_id):

    course = Course.query.get(course_id)
    ppt = PPTs.query.get(ppt_id)

    filename = 'D:\\PycharmProjects\\teachSystem\\auth\\static\\ppt\\%s\\%s' %(course.name,ppt.filename)

    return send_from_directory('\\auth\\static\\upload\\', filename, as_attachment=True)


@auth.route('/tea_watch_film/<teacher_username>/<course_id>/<film_id>',methods=['GET','POST'])
def tea_watch_film(teacher_username,course_id,film_id):

    teacher =Teacher.query.filter_by(username=teacher_username).first()
    course = Course.query.get(course_id)
    film = Films.query.get(film_id)
    reviews = Review.query.filter_by(film_id=film_id).all()

    return render_template('tea_watch_film.html',teacher=teacher,course=course,film=film,reviews=reviews)


@auth.route('/student_watch_film/<student_username>/<course_id>/<film_id>',methods=['GET','POST'])
def student_watch_film(student_username,course_id,film_id):

    student = Student.query.filter_by(username=student_username).first()
    course = Course.query.get(course_id)
    film = Films.query.get(film_id)
    reviews = Review.query.filter_by(film_id=film_id).all()

    return render_template('student_watch_film.html',student=student,course=course,film=film,reviews=reviews)


@auth.route('/student_homework/<student_username>/<course_id>',methods=['GET','POST'])
def student_homework(student_username,course_id):

    student = Student.query.filter_by(username=student_username).first()
    course = Course.query.get(course_id)

    homeworks = Homework.query.filter_by(course_id=course_id).all()

    return render_template('student_homework.html',student=student,course=course,homeworks=homeworks)


@auth.route('student_debate/<student_username>/<course_id>',methods=['GET','POST'])
def student_debate(student_username,course_id):

    student = Student.query.filter_by(username=student_username).first()
    course = Course.query.get(course_id)
    debates = Debate.query.filter_by(course_id=course_id).all()

    return render_template('student_debate.html',student=student,course=course,debates=debates)


@auth.route('student_main_debate/<student_username>/<course_id>/<debate_id>',methods=['GET','POST'])
def student_main_debate(student_username,course_id,debate_id):

    student = Student.query.filter_by(username=student_username).first()
    course = Course.query.get(course_id)
    debate = Debate.query.filter_by(id=debate_id).first()
    discusses = Discuss.query.filter_by(debate_id=debate_id).all()

    teacher = Teacher.query.filter_by(username=course.teacher_name).first()

    return render_template('student_main_debate.html',student=student,course=course,debate=debate,discusses=discusses,teacher=teacher)


@auth.route('/hand_in_homework/<student_username>/<course_id>/<homework_id>',methods=['GET','POST'])
def hand_in_homework(student_username,course_id,homework_id):

    student = Student.query.filter_by(username=student_username).first()
    course = Course.query.get(course_id)
    teacher_name = course.teacher_name

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file_homework(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('D:/PycharmProjects/teachSystem/auth/static/upload/%s/' % teacher_name,filename))
            new_result = Result(filename=filename,student_name=student_username, course_id=course_id,homework_id=homework_id)
            db.session.add(new_result)
            db.session.commit()
            flash('作业上传成功')
        else:
            flash('文件不存在或文件格式错误')

    return render_template('student_hand_in_homework.html', student=student, course=course)


@auth.route('/examine_homework/<teacher_username>/<course_id>/<homework_id>',methods=['GET','POST'])
def examine_homework(teacher_username,course_id,homework_id):

    teacher = Teacher.query.filter_by(username=teacher_username).first()
    course = Course.query.get(course_id)
    results = Result.query.filter_by(course_id=course_id,homework_id=homework_id).all()

    return render_template('tea_examine_homework.html',teacher=teacher,course=course,results=results)


@auth.route('/send_review')
def send_review():

    text = request.args.get('text')
    student_name = request.args.get('student_name')
    film_id = request.args.get('film_id')

    if text:
        try:
            str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            new_review = Review(text=text,time=str_time,student_name=student_name,film_id=film_id)
            db.session.add(new_review)
            db.session.commit()

            review = {
                'student_name':new_review.student_name,
                'text':new_review.text,
                'time':new_review.time
            }

            print('success')
            return jsonify(review)
        except Exception as e:
            print(e)
            flash("发送评论失败")
            db.session.rollback()
            return jsonify('')
    else:
        return jsonify('')


@auth.route('/add_debate')
def add_debate():

    title = request.args.get('title')
    course_id = request.args.get('course_id')

    if title:
        try:
            str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            new_debate = Debate(title=title,time=str_time,discuss_count=0,course_id=course_id)
            db.session.add(new_debate)
            db.session.commit()

            debate = {
                'title':new_debate.title,
                'time':new_debate.time,
                'discuss_count':new_debate.discuss_count
            }

            print('success')
            return jsonify(debate)
        except Exception as e:
            print(e)
            flash("发布讨论失败")
            db.session.rollback()
            return jsonify('')
    else:
        return jsonify('null')


@auth.route('/add_discuss')
def add_discuss():

    text = request.args.get('text')
    student_name = request.args.get('student_username')
    debate_id = request.args.get('debate_id')

    if text:
        try:
            str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            new_discuss = Discuss(text=text,time=str_time,good_count=0,student_name=student_name,debate_id=debate_id)
            db.session.add(new_discuss)
            db.session.commit()

            discuss = {
                'student_name':new_discuss.student_name,
                'text': new_discuss.text,
                'time':new_discuss.time,
                'good_count':new_discuss.good_count
            }

            debate = Debate.query.get(debate_id)
            count = debate.discuss_count
            count += 1
            debate.discuss_count = count
            db.session.commit()

            print('success')
            return jsonify(discuss)
        except Exception as e:
            print(e)
            flash('发送评论失败')
            db.session.rollback()
            return jsonify('')
    else:
        return jsonify('null')


@auth.route('/click_good')
def click_good():

    student_name = request.args.get('student_username')
    discuss_id = request.args.get('discuss_id')

    good = Good.query.filter_by(student_name=student_name,discuss_id=discuss_id).first()

    if good:
        return jsonify('exist')
    else:
        try:
            new_good = Good(student_name=student_name, discuss_id=discuss_id)
            db.session.add(new_good)
            db.session.commit()

            discuss = Discuss.query.get(discuss_id)
            count = discuss.good_count
            count += 1
            discuss.good_count = count
            print(count)
            db.session.commit()

            return jsonify(count)
        except Exception as e:
            print(e)
            flash('点赞失败')
            db.session.rollback()
            return jsonify('fail')


@auth.route('/delete_ppt')
def delete_ppt():

    ppt_id = request.args.get('ppt_id')
    course_name = request.args.get('course_name')

    ppt = PPTs.query.filter_by(id=ppt_id).first()

    if ppt:
        try:
            db.session.delete(ppt)
            db.session.commit()
            print(os.getcwd())
            os.remove('D:/PycharmProjects/teachSystem/auth/static/ppt/%s/%s' %(course_name,ppt.filename))
            return jsonify('success')
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify('error')
    else:
        return jsonify('null')


@auth.route('/delete_film')
def delete_film():

    film_id = request.args.get('film_id')
    course_name = request.args.get('course_name')

    film = Films.query.filter_by(id=film_id).first()

    if film:
        try:
            db.session.delete(film)
            db.session.commit()
            os.remove('D:/PycharmProjects/teachSystem/auth/static/film/%s/%s' %(course_name,film.filename))
            return jsonify('success')
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify('error')
    else:
        return jsonify('null')


@auth.route('/delete_homework')
def delete_homework():

    homework_id = request.args.get('homework_id')
    course_name = request.args.get('course_name')

    homework = Homework.query.filter_by(id=homework_id).first()

    if homework:
        try:
            db.session.delete(homework)
            db.session.commit()
            os.remove('D:/PycharmProjects/teachSystem/auth/static/homework/%s/%s' %(course_name,homework.filename))
            return jsonify('success')
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify('error')
    else:
        return jsonify('null')


@auth.route("/download_file/<course_name>/<ppt_filename>", methods=['GET'])
def download_file(course_name,ppt_filename):
    # 此处的filepath是文件的路径，但是文件必须存储在static文件夹下， 比如images\test.jpg
    filepath = auth.root_path+"\\static\\ppt\\"+course_name+"\\"

    return send_from_directory(filepath, ppt_filename)


@auth.route("/download_homework/<course_name>/<homework_filename>", methods=['GET'])
def download_homework(course_name,homework_filename):
    # 此处的filepath是文件的路径，但是文件必须存储在static文件夹下， 比如images\test.jpg
    filepath = auth.root_path+"\\static\\homework\\"+course_name+"\\"

    return send_from_directory(filepath, homework_filename)


@auth.route('/download_result/<teacher_username>/<result_filename>',methods=['GET'])
def download_result(teacher_username,result_filename):

    filepath = auth.root_path+'\\static\\upload\\'+teacher_username+'\\'

    return send_from_directory(filepath,result_filename)

