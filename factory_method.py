# -*- coding: UTF-8 -*-
# 通过传入参数,控制实例化用户对象或其他对象


class UserConnector:
    def __init__(self):
        self.name = 'i am a user'

    @property
    def name(self):
        return self.name


class OtherConnector:
    def __init__(self):
        self.name = 'i am others'

    @property
    def name(self):
        return self.name


def factory_method(category):
    categories = dict(user=UserConnector(), other=OtherConnector())
    return categories[category]


if __name__ == '__main__':
    a1 = factory_method('user')
    a2 = factory_method('other')

    print a1.name
    print a2.name
