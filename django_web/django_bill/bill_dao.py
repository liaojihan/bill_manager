# coding=utf-8
from bill_models.models import Bill, ConsumptionType, User


class GetBillData:
    """账单页面所有值"""

    def __init__(self, user_id):
        self.user_id = user_id

    def get_bill_data(self):
        bill_data = Bill.objects.filter(user_id=self.user_id)
        pass


def bill_add(bill_request, user_id):
    bill_type = bill_request.get('type', '')
    bill_amount = bill_request.get('amount', '')
    bill_create_time = bill_request.get('create_time', '')
    bill_remark = bill_request.get('remark', '')
    consumption_type = ConsumptionType(id=bill_type)
    user = User(id=user_id)
    if bill_type and bill_amount and bill_create_time and bill_remark:
        bill = Bill(amount=float(bill_amount), create_time=bill_create_time,
                    remark=bill_remark, is_delete=False,
                    type=consumption_type, user=user)
        try:
            bill.save()
        except ValueError:
            return u'数据存储异常，请联系管理员'
    return u'1'


def get_bill_data(user_id):
    user_id_object = User(id=user_id)
    result_data = Bill.objects.filter(is_delete=False, user=user_id_object)
    bill_list = list()
    for bill in result_data:
        result = dict()
        result['select'] = "<input id='check' class='select' type='checkbox' onclick='func_select(this)'></input>"
        result['amount'] = bill.amount
        result['date'] = bill.create_time.strftime("%Y-%m-%d %H:%M:%S")
        result['remark'] = bill.remark
        result['type'] = bill.type.name
        result['id'] = bill.id
        bill_list.append(result)
    bill_list_count = len(bill_list)
    return bill_list, bill_list_count


def bill_delete(id_array):
    for array in id_array:
        try:
            bill = Bill.objects.get(id=array)
            bill.is_delete = True
            bill.save()
        except Exception:
            return u'删除失败'
    return u'1'


def get_detailed_data(bill_id):
    try:
        bill = Bill.objects.filter(id=bill_id).first()
    except Exception:
        return ''
    else:
        bill_dict = {'type': bill.type.name,
                     'amount': bill.amount,
                     'date': bill.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                     'remark': bill.remark}
        return bill_dict


def edit_bill_data(bill_id):
    try:
        bill = Bill.objects.filter(id=bill_id).first()
    except Exception:
        return ''
    else:
        bill_dict = {'amount': bill.amount,
                     'date': bill.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                     'remark': bill.remark,
                     'id': bill_id}
        return bill_dict


def update_bill_data(bill_request):
    bill_id = bill_request.get('id', '')
    bill_amount = bill_request.get('amount', '')
    bill_date = bill_request.get('create_time', '')
    bill_remark = bill_request.get('remark', '')
    bill_type_id = bill_request.get('type', '')
    bill_type = ConsumptionType(id=bill_type_id)
    try:
        bill_object = Bill.objects.filter(id=bill_id).first()
        bill_object.amount = bill_amount
        bill_object.date = bill_date
        bill_object.remark = bill_remark
        bill_object.type = bill_type
        bill_object.save()
    except Exception, e:
        print str(e)
        return u'修改失败，请联系管理员'
    return u'1'
