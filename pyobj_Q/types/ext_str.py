#! -*- coding: utf-8 -*-


import re


class Str(str):
    def __init__(self, *args, **kwargs):
        super(Str, self).__init__()

    def exact(self, data):
        return self == data

    def not_exact(self, data):
        return not self.exact(data)

    def iexact(self, data):
        return self.lower() == data.lower()

    def not_iexact(self, data):
        return not self.iexact(data)

    def contains(self, data):
        return data in self

    def not_contains(self, data):
        return not self.contains(data)

    def icontains(self, data):
        return data.lower() in self.lower()

    def not_icontains(self, data):
        return not self.icontains(data)

    def not_startswith(self, data):
        return not self.startswith(data)

    def istartswith(self, data):
        return self.lower().startswith(data.lower())

    def not_istartswith(self, data):
        return not self.istartswith(data)

    def not_endswith(self, data):
        return not self.endswith(data)

    def iendswith(self, data):
        return self.lower().endswith(data.lower())

    def not_iendswith(self, data):
        return not self.iendswith(data)

    def regexp(self, data):
        return re.search(data, self)

    def not_regexp(self, data):
        return not self.regexp(data)



