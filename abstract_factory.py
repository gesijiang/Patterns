# -*- coding: UTF-8 -*-
# 场景:有卖水果的,有卖宠物的。水果和宠物对象的创建由工厂完成


class AbstractFactory:
    def __init__(self, factory=None):
        self.factory = factory

    def show_best(self):
        self.factory.get_best_selling()

    def show_worse(self):
        self.factory.get_worse_selling()


class Apple:
    def __init__(self):
        print 'Apple'


class Pear:
    def __init__(self):
        print 'Pear'


class FruitFactory:
    def get_best_selling(self):
        return Apple()

    def get_worse_selling(self):
        return Pear()


class Dog:
    def __init__(self):
        print 'Dog'


class Cat:
    def __init__(self):
        print 'Cat'


class PetFactory:

    def get_best_selling(self):
        return Dog()

    def get_worse_selling(self):
        return Cat()


if __name__ == '__main__':
    f1 = AbstractFactory(FruitFactory())
    f1.show_best()

    f2 = AbstractFactory(PetFactory())
    f2.show_worse()

