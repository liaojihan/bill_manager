/**
 * Created by LJH on 2018/3/26.
 */

//验证用户名
$(document).on('click', '#confirm_username', function () {
    var username = $('#confirm-username').val();
    if (username.length === 0 || username === ""){
        layer.msg('请输入用户名');
        $('#confirm-username').focus();
        return;
    }
    $.ajax({
        url: "confirm_username",
        data: {"username": username},
        dataType: 'json',
        type: 'get',
        success: function (data) {
            if (data === "1"){
                window.location.href = "get_id_question";
            }else {
                layer.msg("用户名不存在，请检查");
            }
        }
    });
});

//验证密码问题
$(document).on('click', '#confirm_question', function () {
    var answer = $('#check_answer').val();
    var user_id = $('#user_id_check').val();
    if (answer === 0 || answer.length === 0){
        layer.msg('还没输入答案呢');
        $('#check_answer').focus();
        return;
    }
    $.ajax({
        url: "check_answer",
        dataType: 'json',
        data: {'user_id': user_id, 'answer': answer},
        type: 'get',
        success: function (data) {
            if (data === '1'){
                window.location.href = 'reset_password';
            }else {
                layer.msg(data);
            }
        }
    });
});

//验证新密码
function check_new_password() {
    var password_1 = $('#new_password').val();
    var password_2 = $('#confirm_password').val();
    if (password_2.length === 0 || password_2 === ""){
        return;
    }
    if (password_1 === password_2){
        $('#new_password').css('box-shadow', '');
        $('#confirm_password').css('box-shadow', '');
        return true;
    }
    $('#new_password').css('box-shadow', '0 0 10px #FF3030');
    return false;
}

//验证确认密码输入是否一致
function check_confirm_password() {
    var password_1 = $('#new_password').val();
    var password_2 = $('#confirm_password').val();
    $('#confirm_password').css('box-shadow', '0 0 10px #FF3030');
    if (password_1 === password_2){
        $('#confirm_password').css('box-shadow', '');
        return true;
    }
    return false;
}

//重置密码
$(document).on('click', '#reset', function () {
    var user_id = $('#user_id_reset').val();
    var password_1 = $('#new_password').val();
    var password_2 = $('#confirm_password').val();
    var new_result = check_new_password();
    var confirm_result = check_confirm_password();
    if (password_1.length === 0 || password_1 === ""){
        layer.msg('密码还没输入呢');
        $('#new_password').focus();
        return;
    }
    if (password_2.length === 0 || password_2 === ""){
        layer.msg('请再次输入密码');
        $('#confirm_password').focus();
        return;
    }
    if (!new_result && !confirm_result){
        layer.msg('两次密码输入不一致');
        return;
    }
    $.ajax({
        url: 'reset_user_password',
        dataType: 'json',
        data: {'user_id': user_id, 'password': password_2},
        type: 'POST',
        success: function (data) {
            if (data === '1'){
                layer.msg('重置成功，请牢记密码');
                setTimeout(function () {
                    window.location.href = 'home';
                }, 3000);
            }
        }
    });
});