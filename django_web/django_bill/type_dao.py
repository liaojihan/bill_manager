# coding=utf-8
from bill_models.models import ConsumptionType, Bill


def get_type_data():
    """获取所有的账单类型"""
    type_data = ConsumptionType.objects.all()
    result_data = ''
    for data in type_data:
        result_data += "<option value='{}'>{}</option>".format(data.id, data.name)
    return result_data


def add_type_data(type_name):
    type_is_empty = ConsumptionType.objects.filter(name=type_name).first()
    if type_is_empty:
        return_msg = u'您输入的类型已经存在，请重新输入'
    else:
        try:
            consumption_type = ConsumptionType(name=type_name)
            consumption_type.save()
            return_msg = u'1'
        except Exception:
            return_msg = u'存储失败，请联系管理员'
    return return_msg


def get_edit_type_data(bill_id):
    type_id = Bill.objects.filter(id=int(bill_id)).first().type.id
    type_data = ConsumptionType.objects.all()
    result_type = ''
    for data in type_data:
        if data.id == type_id:
            result_type += "<option value='{}' selected='selected'>{}</option>".format(data.id, data.name)
            continue
        result_type += "<option value='{}'>{}</option>".format(data.id, data.name)
    return result_type
