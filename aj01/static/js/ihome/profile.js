function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$('#form-avatar').submit(function () {
   // $('.error_msg').hide();
   $(this).ajaxSubmit({
       url: '/user/profile/',
       type: 'PATCH',
       dataType: 'json',
       success: function (msg) {
           $('#user-avatar').attr('src', '/static/' + msg.image_url);
       },
       error: function (msg) {
           alert('图片上传失败')
       }
   });
   return false;
});


$('#form-name').submit(function () {
    $('.error-msg2').hide();
    var username = $('#user-name').val();
    $.ajax({
        url: '/user/proname/',
        type: 'patch',
        data: {'name': username},
        success: function (data) {
            if(data.code == '1008'){
            //
            }else{
                $('.error-msg2').html('<i class="fa fa-exclamation-circle"></i>' + data.msg);
                $('.error_msg2').show();
            }
        },
        error: function (msg) {
            alert('请求错误')
        }
    });
    return false;
});

function delete_msg() {
    $('.error-msg').hide()
}