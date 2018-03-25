# coding=utf-8
from bill_models.models import User


def user_login(user_dict):
    user_name = user_dict['username']
    user_password = user_dict['password']
    try:
        User.objects.get(user_name=user_name, user_password=user_password).first()
    except Exception:
        return u'账户信息有误，请检查'
    else:
        return u'1'


def user_add(user_dict):
    user_name = user_dict['new_name']
    user_password = user_dict['new_password']
    user_question = user_dict['question']
    user_answer = user_dict['answer']
    try:
        User.objects.get(user_name=user_name).first()
    except Exception:
        user = User(user_name=user_name,
                    user_password=user_password,
                    question=user_question,
                    answer=user_answer,
                    is_delete=False)
        user.save()
    else:
        return u'该用户名已被注册'
    return u"1"


def update_forget_password(username):
    pass
