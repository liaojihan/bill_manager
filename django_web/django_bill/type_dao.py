from bill_models.models import ConsumptionType


def get_type_data():
    type_data = ConsumptionType.objects.all()
    result_data = ''
    for data in type_data:
        result_data += "<option value='{}'>{}</option>".format(data.id, data.name)
    return result_data
