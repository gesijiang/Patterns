# -*- coding: UTF-8 -*-


class Publisher(object):
    def __init__(self):
        self._observers = []

    def register(self, observe):
        if observe not in self._observers:
            self._observers.append(observe)
        else:
            print 'Fail to register'

    def remove(self, observe):
        try:
            self._observers.remove(observe)
        except ValueError:
            print 'Fail to remove'

    def notify(self, modifier=None):
        for i in self._observers:
            if modifier != i:
                i.update(self)


class News(Publisher):
    def __init__(self, msg=''):
        Publisher.__init__(self)
        self._msg = msg

    @property
    def message(self):
        return self._msg

    @message.setter
    def message(self, value):
        self._msg = value
        self.notify()

    @message.deleter
    def message(self):
        del self._msg


class User:
    def __init__(self, username):
        self.username = username

    def update(self, publisher):
        print (u'User %s get msg %s from publisher' % (self.username, publisher.message))


if __name__ == '__main__':
    news = News()
    user1 = User('user1')
    user2 = User('user2')
    news.register(user1)
    news.register(user2)

    news.message = 'msg1'
    news.message = 'msg2'


