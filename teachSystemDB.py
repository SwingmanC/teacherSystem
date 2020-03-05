'''
<script type="text/javascript">
   $('form').on('submit', function (event) {
        // 显示进度条
        $('.progress').css('display', 'block');
        // 阻止元素发生默认的行为，此处用来阻止对表单的提交
        event.preventDefault();
        var formData = new FormData(this);
        // jQuery Ajax 上传文件，关键在于设置：processData 和 contentType
        $.ajax({
            xhr: function () {
                var xhr = new XMLHttpRequest();
                xhr.upload.addEventListener('progress', function (e) {
                    if (e.lengthComputable) {
                        var percent = Math.round(e.loaded * 100 / e.total);
                        $('.progress-bar').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');
                    }
                });
                return xhr;
            },
            type: 'POST',
            url: '/manage_course_film/{{ teacher.username }}/{{ course.id }}',
            cache: false,
            data: formData,
            // 告诉 jQuery 不要去处理发送的数据
            processData: false,
            // 告诉 jQuery 不要去设置 Content-Type 请求头
            // 因为这里是由 <form> 表单构造的 FormData 对象，且已经声明了属性 enctype="multipart/form-data"，所以设置为 false
            contentType: false
        }).done(function (res) {
            alert('上传成功!');
        }).fail(function (res) {
            alert('上传失败!');
        });
    });
</script>
'''
