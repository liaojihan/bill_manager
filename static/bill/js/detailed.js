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
                $('#bill_type').append(data);
            }
        }
    });
}
$(document).ready(function () {
    $('#dataTables-example').DataTable({
        "serverSide": true,
        "retrieve": true,
        "processing": true,
        "ordering": false,
        "searching": false,
        "pagingType": "full_numbers",
        "lengthMenu": [10, 20, 30, 40],
        language: dtLanguage,
        "ajax": {
            url: 'get_table_data',
            type: 'get'
        },
        columnDefs:[
            {
                "targets": [5],
                data: "id",
                "render": function (data, type, row) {
                    return '<a href="#" onclick="detailed_bill(' + row['id'] + ')" class="btn btn-default btn-xs"><i class="fa fa-paperclip"></i>&nbsp;&nbsp;看一看</a>&nbsp;&nbsp;' +
                            '<a href="javascript:void(0)" onclick="edit_bill('+ row['id'] +')" class="btn btn-primary btn-xs" role="button"><i class="fa fa-edit"></i>&nbsp;&nbsp;改一改</a>'
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
function check_amount(data) {

}

$(document).on('blur', '#amount', function () {
    var amount = $('#amount').val();
    var re = /^[0-9]+.?[0-9]*$/;
    if (!re.test(amount)){
        layer.msg('金额请输入数字！');
        $('#amount').focus();
        return;
    }
    if (amount.indexOf('.') > 0){
       return;
    }
    $('#amount').val(amount + '.0');
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
                $('#dataTables-example').DataTable().draw(false);
                $('#amount').val('');
                $('#date').val('');
                $('#remark').val('');
            }else {
                layer.msg(data);
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
            }
        }
    });
});

//删一单
function remove_bill() {
    var table = $('#dataTables-example').DataTable();
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
                        $('#dataTables-example').DataTable().draw(false);
                    }else {
                        layer.msg(data);
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
});