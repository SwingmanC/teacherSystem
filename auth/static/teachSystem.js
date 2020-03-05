//注册模块的js
function StuUsernameIsExist(){
    $('#username_input').bind('blur',function () {
        $.getJSON('/auth/check_student_username',{
            username:$('#username_input').val()
        },function (data) {
            if (data === "exist")
                $('#usernameMsg').val("<font color='red'>此用户名已存在</font>")
            else
                $('#usernameMsg').val("<font color='green'>此用户名可以使用</font>")
        })
    })
}

function TeaUsernameIsExist(){
    $('#username_input').bind('blur',function () {
        $.getJSON('/auth/check_teacher_username',{
            username:$('#username_input').val()
        },function (data) {
            if (data === "exist")
                $('#usernameMsg').val("<font color='red'>此用户名已存在</font>")
            else
                $('#usernameMsg').val("<font color='green'>此用户名可以使用</font>")
        })
    })
}

function passwordIsValid() {
    var pass=document.register_form.password.value;

    var div =document.getElementById("passwordMsg");

    if(pass.trim().length>0&&pass.trim().length<6)
    {
        div.innerHTML="<font color='red'>密码强度太低</font>";
        return false;
    }
    else if(pass.trim().length>=6) {
        div.innerHTML = "<font color='green'>密码可以使用</font>";
        return true;
    }
}

function passwordIsSame(){
    var pass1=document.register_form.password.value;
    var pass2=document.register_form.repeatedPassword.value;

    var div=document.getElementById("repeatedPasswordMsg");

    if(pass1!=pass2&&pass2.trim().length>0){
        div.innerHTML="<font color='red'>两次密码输入不一致</font>";
        return false;
    }
    else if(pass1==pass2&&pass1.trim().length>0)
    {
        div.innerHTML="<font color='green'>√</font>";
        return true;
    }
}

function emailIsValid(){
    var email=document.register_form.email.value;
    console.log(email);
    var div=document.getElementById("emailMsg");

    if(email.trim().length>0) {
        var reg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;
        var isok= reg.test(email);
        if(!isok) {
            div.innerHTML="<font color='red'>邮箱格式错误</font>";
            return false;
        }
        else
        {
            div.innerHTML="<font color='green'>邮箱可以使用</font>";
            return true;
        }
    }
}

function checkAllRegisterForm()
{
    var username=document.register_form.username.value;
    var pass1=document.register_form.password.value;
    var pass2=document.register_form.repeatedPassword.value;
    var email=document.register_form.email.value;

    var div=document.getElementById("usernameMsg").innerText;

    if(username.trim().length==0||pass1.trim().length==0||pass2.trim().length==0||email.trim().length==0)
    {
        alert("Please fill in the information.");
        return false;
    }
    else if(div === "此用户名已存在"||!passwordIsValid()||!passwordIsSame()||!emailIsValid())
    {
        alert("Please fill in the correct information.")
        return false;
    }
    else
        return true;
}

//课程视频模块的js
function addReview(a,b) {
    var text = $('#review_input').val().replace(/\s+/g,"");
    if (text .length > 40)
    {
        $('#tip').text("评论字数过多");
    }
    if (text !== "" && text.length <= 40)
    {
        $('#review_submit').bind('click',function () {
        $.getJSON('/auth/send_review',{
            text:text,
            student_name:a,
            film_id:b
        },function (data) {
            if (data !== "")
            {
                console.log(data);
                var $review_li = $('<li><font color="#a9a9a9">'+data['student_name']+'</font>'+data['text']+'<font color="#a9a9a9">'+data['time']+'</font></li><br>');
                $('ul').append($review_li)
            }

        })
    })
    }

}

//课程讨论区模块的js
/*function addDebate(course_id){
    $.ajax({
        async:true,
        type:'get',
        url:'/auth/add_debate',
        data:{
            'title':$('#debate_input').val(),
            'course_id':course_id
        },
        dataType:'json',
        cache:false,
        success:function (data) {
            if (data === ''){}
            else if (data === 'null')
            {
                $('#tip').val('<font color=\'red\'>讨论主题不可为空</font>');
            }
            else
            {
                var $debate_li = $('<li><h3><a href="">'+data['title']+'</a></h3><br><font color="#a9a9a9">'+data['time']+'</font></li>');
                $('ul').append($debate_li);
            }
        },
        error:function () {

        }
    });
}*/


//课程主页面的js
function deletePPT(ppt_id,course_name) {
    $.ajax({
        async:true,
        type:'get',
        url:'/auth/delete_ppt',
        data:{'ppt_id':ppt_id,
              'course_name':course_name
        },
        dataType:'json',
        cache:false,
        success:function (data) {
            if(data === 'success')
                $('#delete_ppt_'+ppt_id).parent().fadeOut(500);
        },
        error:function () {

        }
    });
}

function deleteFilm(film_id,course_name){
    $.ajax({
        async:true,
        type:'get',
        url:'/auth/delete_film',
        data:{'film_id':film_id,
              'course_name':course_name
        },
        dataType:'json',
        cache:false,
        success:function (data) {
            if(data === 'success')
                $('#delete_film_'+film_id).parent().fadeOut(500);
        },
        error:function () {

        }
    });
}

function deleteHomework(homework_id,course_name) {
        $.ajax({
        async:true,
        type:'get',
        url:'/auth/delete_homework',
        data:{'homework_id':homework_id,
              'course_name':course_name
        },
        dataType:'json',
        cache:false,
        success:function (data) {
            if(data === 'success')
                $('#delete_homework_'+homework_id).parent().fadeOut(500);
        },
        error:function () {

        }
    });
}

