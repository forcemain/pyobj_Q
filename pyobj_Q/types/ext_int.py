#! -*- coding: utf-8 -*-


class Int(int):
    def __init__(self, *args, **kwargs):
        super(Int, self).__init__()

    def exact(self, data):
        return self == data
