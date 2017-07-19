# -*- coding: UTF-8 -*-
# 场景:已经运算过的存到缓存中


def memoize(fn):
    cache = dict()

    def memoizer(x):
        if x not in cache:
            cache[x] = fn(x)
        return cache[x]
    return memoizer


@memoize
def fib(n):
    if n in (0, 1):
        return n
    else:
        return fib(n-1)+fib(n-2)


print fib(10)

