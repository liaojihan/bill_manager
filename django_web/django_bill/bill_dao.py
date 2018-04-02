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
        bill = Bill(amount=bill_amount, create_time=bill_create_time,
                    remark=bill_remark, is_delete=False,
                    type=consumption_type, user=user)
        try:
            bill.save()
        except ValueError:
            return u'数据存储异常，请联系管理员'
    return u'1'


def get_bill_data():
    result_data = Bill.objects.all()
    bill_list = list()
    for bill in result_data:
        result = dict()
        result['select'] = "<input id='check' class='select' type='checkbox'></input>"
        result['amount'] = bill.amount
        result['date'] = bill.create_time.strftime("%Y-%m-%d %H:%M:%S")
        result['remark'] = bill.remark
        result['type'] = bill.type.name
        result['id'] = bill.id
        bill_list.append(result)
    bill_list_count = len(bill_list)
    return bill_list, bill_list_count
