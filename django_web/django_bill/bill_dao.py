# coding=utf-8
from bill_models.models import Bill, ConsumptionType, User
from django.db.models import Sum, Count, Max, Min, Avg
from django.db import connection

# 获取游标对象
cursor = connection.cursor()


class BillData:
    """账单总览"""

    def __init__(self, user_id):
        self.user_id = user_id

    def get_pie_chart(self):
        """获取账单类型占比"""
        amount_count = Bill.objects.filter(user=self.user_id).aggregate(Sum('amount'))['amount__sum']
        bill_sql = '''SELECT SUM(b.amount) as sum_amount, c.`name` FROM 
                      bill b LEFT JOIN consumption_type c on b.type_id=c.id 
                      WHERE user_id={} and is_delete=0 GROUP BY b.type_id 
                      ORDER BY sum_amount DESC limit 4'''.format(self.user_id)
        cursor.execute(bill_sql)
        raw = cursor.fetchall()
        bill_data_list = list()
        for bill in raw:
            bill_dict = dict()
            proportion = round(bill[0] / amount_count * 100, 2)
            bill_dict['proportion'] = proportion
            bill_dict['name'] = bill[1]
            bill_data_list.append(bill_dict)
        return bill_data_list

    def get_line_chart(self):
        """获取折线图数据"""
        bill_sql = '''SELECT SUM(amount) as sum_amount, YEAR(create_time) as year 
                      FROM bill WHERE user_id= {} GROUP BY YEAR(create_time)'''.format(self.user_id)
        cursor.execute(bill_sql)
        raw = cursor.fetchall()
        line_list = list()
        for line in raw:
            line_dict = dict()
            line_dict['year'] = line[1]
            line_dict['data'] = line[0]
            line_list.append(line_dict)
        return line_list

    ep_list = {
        'data': [11, 11, 11, 11, 11, 11],
        'year': [2010, 2011, 2012, 2013, 2014, 2015, 2016],
        'name': ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg']
    }

    def get_bar_chart(self):
        bill_sql = '''SELECT MAX(amount), type_id, YEAR(create_time) as year FROM bill GROUP BY year'''
        cursor.execute(bill_sql)
        raw = cursor.fetchall()
        bar_list = list()
        for bar in raw:
            bar_dict = dict()
            bar_dict['amount'] = bar[0]
            type_object = ConsumptionType.objects.filter(id=int(bar[1])).first()
            bar_dict['name'] = type_object.name
            bar_dict['year'] = bar[2]
            bar_list.append(bar_dict)
        return bar_list

    def get_area_chart(self):
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


def get_bill_data(user_id, page_data):
    page_start = int(page_data.get('start'))
    page_length = int(page_data.get('length'))
    user_id_object = User(id=user_id)
    result_data = Bill.objects.filter(is_delete=False, user=user_id_object).all()
    bill_count = len(result_data)
    bill_list = list()
    consumption_amount = 0
    for bill in result_data:
        result = dict()
        result['select'] = "<input id='check' class='select' type='checkbox' onclick='func_select(this)'></input>"
        result['amount'] = bill.amount
        result['date'] = bill.create_time.strftime("%Y-%m-%d %H:%M:%S")
        result['remark'] = bill.remark
        result['type'] = bill.type.name
        result['id'] = bill.id
        bill_list.append(result)
        consumption_amount += float(bill.amount)
    return bill_list[page_start: page_start + page_length], bill_count, consumption_amount


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
        bill_object.create_time = bill_date
        bill_object.remark = bill_remark
        bill_object.type = bill_type
        bill_object.save()
    except Exception, e:
        print str(e)
        return u'修改失败，请联系管理员'
    return u'1'


def get_search_bill(bill_form, user_id):
    start_time = bill_form.get('start_time', '')
    end_time = bill_form.get('end_time', '')
    type_id = bill_form.get('type_id', '')
    remark = bill_form.get('remark', '')
    page_start = int(bill_form.get('start'))
    page_length = int(bill_form.get('length'))
    filter_option = ''
    if start_time:
        filter_option += '''AND create_time >= {}'''.format(start_time)
    if end_time:
        filter_option += '''AND create_time <= {}'''.format(end_time)
    if type_id:
        filter_option += '''AND type_id = {}'''.format(type_id)
    if remark:
        filter_option += '''AND remark like "%{}%" '''.format(remark)
    bill_sql = '''select * from bill WHERE user_id={} AND is_delete=0 '''.format(user_id) + filter_option
    result = Bill.objects.raw(bill_sql)
    bill_list = list()
    for item in result:
        bill_dict = dict()
        bill_dict['id'] = item.id
        bill_dict['select'] = "<input id='check' class='select' type='checkbox' onclick='func_select(this)'></input>"
        bill_dict['type'] = item.type.name
        bill_dict['amount'] = item.amount
        bill_dict['date'] = item.create_time.strftime("%Y-%m-%d %H:%M:%S")
        bill_dict['remark'] = item.remark
        bill_list.append(bill_dict)
    return bill_list[page_start: page_start + page_length], len(bill_list)
