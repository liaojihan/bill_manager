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
    is_empty = User.objects.filter(user_name=username).first()
    if not is_empty:
        return u'用户名不存在，请检查'
    return u'1'


def get_id_question(username):
    result_user = User.objects.filter(user_name=username)
    user_id = 0
    user_question = ""
    for user in result_user:
        user_id = user.id
        user_question = user.question
    return user_id, user_question


def check_user_answer(user_dict):
    user_id = user_dict['user_id']
    user_answer = user_dict['answer']
    result_user = User.objects.filter(id=user_id)
    answer = ""
    for user in result_user:
        answer = user.answer
    if answer == user_answer:
        return u'1'
    return u'答案似乎有问题,请检查'


def reset_password_dao(user_dict):
    user_id = user_dict.get('user_id', '')
    user_password = user_dict.get('password', '')
    User.objects.filter(id=user_id).update(user_password=user_password)
    return u'1'
