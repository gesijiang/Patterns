# -*- coding: UTF-8 -*-
# 场景: 创建一个LazyProperty类,用作一个修饰器。当它修饰某个特性时,延迟加载,同时实现不重复的加载。


# 注意要有参数object
class LazyLoad(object):
    def __init__(self, method):
        self.method = method

    def __get__(self, obj, cls):
        if obj is None:
            return None
        value = self.method(obj)
        setattr(obj, self.method.__name__, value)
        return value


class Test:
    def __init__(self):
        self.x = 1
        self._y = 2

    @LazyLoad
    def resource(self, x=2):
        print('initializing')  # 仅一次
        self.x = x
        self._y += 1
        return self.x*self._y+1


t = Test()

print t.x
t.resource
print t.x
print t.resource

print t.__dict__

