/**
 * Created by LJH on 2018/3/21.
 */

// --- 登录
$(document).on('click', '#submit', function () {
   var username = $('#form-username').val().trim();
   var password = $('#form-password').val().trim();
   if (username.length === 0 || username === ""){
        layer.msg('用户名还没输入呢');
        $('#form-username').focus();
        return;
   }
   if (password.length === 0 || password === ""){
        layer.msg('密码还没输入呢');
        $('#form-password').focus();
        return;
   }
   $.ajax({
        url: 'user_login',
        dataType: 'json',
        type: 'get',
        data: $('#bill_form').serializeArray(),
        success: function (data) {
            if (data === '1'){
                window.location.href = 'bill';
            }else {
                layer.alert('账户信息有误，请重新输入！');
            }
        }
   });
});

// --- 触发注册model
function add_user() {
    $('#form_user_add').find('input').val("");
    $('#add_user_model').modal({backdrop: 'static', keyboard: false});
}

// --- 注册
$(document).on('click', '#add_user', function () {
    var user_name = $('#new_name').val().trim();
    var user_password = $('#new_password').val().trim();
    var question = $('#question').val().trim();
    var answer = $('#answer').val().trim();
    if (user_name.length === 0 || user_name === ""){
        layer.msg('用户名还没输入呢');
        $('#new_name').focus();
        return;
    }
    if (user_password.length === 0 || user_password === ""){
        layer.msg('密码还没输入呢');
        $('#new_password').focus();
        return;
    }
    if (question === '--请选择一个问题--'){
        layer.msg('请选择一个问题');
        return;
    }
    if (answer.length === 0 || answer === ""){
        layer.msg('答案还没输入呢！');
        $('#answer').focus();
        return;
    }
    $.ajax({
        url: "user_add",
        dataType: 'json',
        type: 'post',
        data: $('#form_user_add').serializeArray(),
        success: function (data) {
            if (data === '1'){
                layer.msg('注册成功，请牢记密码提示问题\r\n用于找回密码');
                $('#add_user_model').modal('hide');
            }else {
                layer.alert(data);
            }
        }
    });
});

