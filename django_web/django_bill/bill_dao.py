# coding=utf-8
from bill_models.models import Bill


class GetBillData:
    """账单页面所有值"""

    def __init__(self, user_id):
        self.user_id = user_id

    def get_bill_data(self):
        bill_data = Bill.objects.filter(user_id=self.user_id)
        pass
