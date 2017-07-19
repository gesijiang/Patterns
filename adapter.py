# -*- coding: UTF-8 -*-
# 场景:跑和跳是不能更改的函数,但客户端只会用execute调用


class ExA1:
    def __init__(self, name):
        self.name = name

    def run(self):
        print self.name+'run'


class ExA2:
    def __init__(self, name):
        self.name = name

    def jump(self):
        print self.name+'jump'


class A3:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print self.name+'execute'


class Adapter:
    def __init__(self, obj, method):
        self.obj = obj
        self.__dict__.update(method)


lists = [A3('Execute')]
a1 = ExA1('Run')
a2 = ExA2('Jump')
#lists.append(Adapter(a1, dict(execute=a1.run)))
#lists.append(Adapter(a2, dict(execute = a2.jump)))
#for i in lists:
#    print i.execute()


i = Adapter(a1, dict(execute=a1.run))
i.execute()






