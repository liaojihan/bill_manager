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
        type: 'post',
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
