/**
 * Created by LJH on 2018/3/26.
 */

$(document).on('click', '#confirm', function () {
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
                window.location.href = "xxx";
            }else {
                layer.msg("用户名不存在，请检查");
            }
        }
    });
});