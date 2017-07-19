# -*- coding: UTF-8 -*-


def bold(fn):
    def wrapped():
        return 'bold'+fn()
    return wrapped


def italic(fn):
    def wrapped():
        return 'italic'+fn()
    return wrapped


@bold
@italic
def text():
    return 'hello'

print text()
