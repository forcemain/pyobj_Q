#! -*- coding: utf-8 -*-


import copy


class Node(object):
    default = 'DEFAULT'

    def __init__(self, children=None, connector=None):
        self.children = children[:] if children else []
        self.connector = connector or self.default

    @classmethod
    def _new_instance(cls, children=None, connector=None):
        obj = Node(children, connector)
        obj.__class__ = cls
        return obj

    def __str__(self):
        template = '(%s: %s)'
        return repr(template % (self.connector, ', '.join(repr(c) for c in self.children)))

    def __repr__(self):
        return str("<%s: %s>") % (self.__class__.__name__, self)

    def __deepcopy__(self, memodict):
        obj = Node(connector=self.connector)
        obj.__class__ = self.__class__
        obj.children = copy.deepcopy(self.children, memodict)
        return obj

    def __len__(self):
        return len(self.children)

    def __bool__(self):
        return bool(self.children)

    def add(self, data, conn_type):
        if data in self.children:
            return data
        if self.connector == conn_type:
            if data.connector == conn_type or len(data) == 1:
                self.children.extend(data.children)
            else:
                self.children.append(data)
        else:
            obj = self._new_instance(self.children, self.connector,)
            self.connector = conn_type
            self.children = [obj, data]

