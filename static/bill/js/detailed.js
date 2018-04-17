$(function () {
    get_bill_type();
});

function get_bill_type() {
    $.ajax({
        url: 'get_type',
        dataType: 'json',
        type: 'get',
        success: function (data) {
            if (data){
                $('#bill_type').html(data);
                $('#select_type').html(data);
            }
        }
    });
}


$(document).ready(function () {
    $('#bill_table').DataTable({
        "serverSide": true,
        "retrieve": true,
        "processing": true,
        "ordering": false,
        "searching": false,
        "autoWidth": false,
        "pagingType": "full_numbers",
        "lengthMenu": [10,20,40,60],
        language: dtLanguage,
        "ajax": {
            url: 'get_table_data',
            type: 'get'
        }
        ,
        columnDefs:[
            {
                "targets": [5],
                data: "id",
                "render": function (data, type, row) {
                    return '<a href="#" onclick="detailed_bill(' + row['id'] + ')" class="btn btn-default btn-xs"><i class="fa fa-paperclip"></i>&nbsp;&nbsp;看一看</a>&nbsp;&nbsp;' +
                            '<a href="javascript:void(0)" onclick="edit_bill('+ row['id'] +')" class="btn btn-success btn-xs" role="button"><i class="fa fa-cog"></i>&nbsp;&nbsp;改一改</a>'
                }
            }
        ],
        columns: [
            {data: 'select'},
            {data: 'type'},
            {data: 'amount'},
            {data: 'date'},
            {data: 'remark'}
        ]
    });
});

function set_model_attribute() {
    $('#addBill').modal({
        "backdrop": "static",
         "keyboard": false
    });
    $('#addBill').modal('show');
}

function set_show_modal() {
    $('#addType').modal({
        "backdrop": "static",
        "keyboard": false
    });
    $('#addType').modal('show');
}

function func_check_all() {
    if ($("#checkall").is(':checked') == true) {
        $('.select').each(function () {
            $(this).prop('checked', true);
            // $(this).attr('checked', true);
            $('.select').on("click", func_add(this));
        });
    } else {
        $('.select').each(function () {
            $(this).prop('checked', false);
            // $(this).attr('checked', false);
            $('.select').on("click", func_remove(this));
        });
    }
}

function func_add(doc) {
    $(doc).parent().parent().addClass('selected');
}

function func_remove(doc) {
    $(doc).parent().parent().removeClass('selected');
}
function func_select(doc) {
    $(doc).parent().parent().toggleClass('selected');
}

function refresh_data(){
    window.location.href = 'detailed';
}

//校检金额
function check_amount(data, amount_id) {
    if (data.length === 0 || data === ""){
        layer.msg('请输入金额');
        return;
    }
    var re = /^[0-9]+.?[0-9]*$/;
    if (!re.test(data)){
        layer.msg('金额请输入数字！');
        $('#' + amount_id).focus();
        return;
    } else if (data.indexOf('.') > 0){
        return;
    }
    $('#' + amount_id).val(data + '.0');
}

$(document).on('blur', '#amount', function () {
    var amount = $('#amount').val();
    check_amount(amount, 'amount');
});

$(document).on('blur', '#edit_amount', function () {
    var amount = $('#edit_amount').val();
    check_amount(amount, 'edit_amount');
});

//记一笔
$(document).on('click', '#save_bill',  function () {
    var amount = $('#amount').val();
    var date = $('#date').val();
    var remark = $('#remark').val().trim();
    if (amount.length === 0 || amount === ""){
        layer.msg('请输入金额');
        $('#amount').focus();
        return;
    }
    if (date.length === 0 || date === ""){
        layer.msg('请选择日期');
        $('#date').focus();
        return;
    }
    if (remark.length === 0 || remark === ""){
        layer.msg('请输入备注');
        $('#remark').focus();
        return;
    }
    $.ajax({
        url: 'bill_data_add',
        data: $('#bill_add_form').serializeArray(),
        dataType: 'json',
        type: 'POST',
        success: function (data) {
            if (data === '1'){
                layer.msg('记录成功');
                $('#addBill').modal('hide');
                $('#bill_table').DataTable().draw(false);
                $('#amount').val('');
                $('#date').val('');
                $('#remark').val('');
            }else {
                layer.alert(data);
            }
        }
    });
});

$(document).on('click', '#save_type', function () {
    var type_name = $('#type_name').val();
    if (type_name.length === 0 || type_name === ""){
        layer.msg('名称还未填写！');
        $('#type_name').focus();
        return;
    }
    $.ajax({
        url: 'type_add',
        dataType: 'json',
        type: 'POST',
        data: $('#type_add_form').serializeArray(),
        success: function (data) {
            if (data === '1'){
                layer.msg('添加成功');
                get_bill_type();
                $('#addType').modal('hide');
                $('#type_name').val('');
            }else {
                layer.msg(data);
            }
        }
    });
});

//删一单
function remove_bill() {
    var table = $('#bill_table').DataTable();
    var data = table.rows('.selected').data();
    var bills_id = [];
    for (var i=0 ; i < data.length ; i++) {
        var id = data[i]['id'];
        bills_id.push(id);
    }
    if (bills_id.length){
        layer.confirm('确认删除吗?', {icon: 3, title: '提示'}, function (index) {
            $.ajax({
                url: 'bill_data_delete',
                dataType: 'json',
                traditional: true,
                type: 'POST',
                data: {'bills_id': bills_id},
                success: function (data) {
                    if (data === '1'){
                        layer.msg('操作成功');
                        $('#bill_table').DataTable().draw(false);
                    }else {
                        layer.alert(data);
                    }
                    layer.close(index);
                }
            });
        });
    }else {
        layer.msg('请至少选择一项！');
    }
}

//详情
function detailed_bill(id){
    $.ajax({
        url: 'get_detailed',
        dataType: 'json',
        type: 'GET',
        data: {"id": id},
        success: function (data) {
            if (data){
                $('#detailed_type').val(data['type']);
                $('#detailed_amount').val(data['amount']);
                $('#detailed_date').val(data['date']);
                $('#detailed_remark').val(data['remark']);
                $('#detailedModal').modal({
                    "backdrop": "static",
                    "keyboard": false
                });
                $('#detailedModal').modal('show');
            }
        }
    });
}

//修改
function edit_bill(id) {
    $.ajax({
        url: 'edit_bill',
        dataType: 'json',
        type: 'GET',
        data: {'id': id},
        success: function (data) {
            edit_bill_type(id);
            $('#edit_amount').val(data['amount']);
            $('#edit_date').val(data['date']);
            $('#edit_remark').val(data['remark']);
            $('#edit_id').val(data['id']);
            $('#editBill').modal({
                "backdrop": "static",
                "keyboard": false
            });
            $('#editBill').modal('show');
        }
    });
}
function edit_bill_type(id) {
    $.ajax({
        url: 'get_edit_type',
        dataType: 'json',
        type: 'GET',
        data: {'bill_id': id},
        success: function (data) {
            if (data){
                $('#edit_type').append(data);
            }
        }
    });
}

//更新入库
$(document).on('click', '#save_edit', function () {
    var amount = $('#edit_amount').val().trim();
    var date = $('#edit_date').val();
    var remark = $('#edit_remark').val().trim();
    if (amount.length === 0 || amount === ""){
        layer.msg('请输入金额');
        $('#edit_amount').focus();
        return;
    }
    if (date.length === 0 || date === ""){
        layer.msg('请选择日期');
        $('#edit_date').focus();
        return;
    }
    if (remark.length === 0 || remark === ""){
        layer.msg('请输入备注');
        $('#edit_remark').focus();
        return;
    }
    $.ajax({
        url: 'update_bill',
        dataType: 'json',
        type: 'POST',
        data: $('#bill_edit_form').serializeArray(),
        success: function (data) {
            if (data === '1'){
                layer.msg('操作成功');
                $('#bill_table').DataTable().draw(false);
                $('#editBill').modal('hide');
            }
        }
    });
});

//模糊查询
function search_bill() {
    var start_time = $('#start_time').val();
    var end_time = $('#end_time').val();
    var select_type = $('#select_type').val();
    var search_remark = $('#search_remark').val();
    if (end_time.length !== 0 || end_time !== "") {
        if (start_time > end_time) {
            layer.alert('开始时间不能大于结束时间');
            $('#start_time').focus();
            return;
        }
    }
    $('#bill_table').DataTable().ajax.
    url('search_bill?start_time='+start_time+"&end_time="+end_time+"&type_id="+select_type+"&remark="+search_remark).draw(false);
}
