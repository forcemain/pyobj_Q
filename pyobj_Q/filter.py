#! -*- coding: utf-8 -*-


from pyobj_Q.tree import Node


class Q(Node):
    AND = 'AND'
    OR = 'OR'
    default = AND

    def __init__(self, *args, **kwargs):
        super(Q, self).__init__(children=list(args) + list(kwargs.items()))

    def _combine(self, other, conn):
        obj = type(self)()
        obj.connector = conn
        obj.add(self, conn)
        obj.add(other, conn)
        return obj

    def __or__(self, other):
        return self._combine(other, self.OR)

    def __and__(self, other):
        return self._combine(other, self.AND)


class R(object):
    connector_map = {'OR': any, 'AND': all}

    def __init__(self, obj, q_ins):
        self.obj = obj
        self.q_ins = q_ins

    def _validate(self, func, data):
        return eval(func.replace('__', '.'), {func.split('__')[0]: self.obj})(data)

    def _dispatch(self, children):
        if isinstance(children, tuple):
            return self._validate(*children)
        if isinstance(children, list):
            return map(lambda t: self._validate(*t), children)

    def _qresult(self, q):
        if not filter(lambda q_c: isinstance(q_c, Q), q.children):
            dispatch_res = self._dispatch(q.children)
            return [self.connector_map[q.connector](dispatch_res)]
        q_list = []
        for q_child in q.children:
            if isinstance(q_child, Q):
                q_list.append(self.connector_map[q_child.connector](self._qresult(q_child)))
            else:
                dispatch_res = self._dispatch(q_child)
                q_list.append(dispatch_res)
        return self.connector_map[q.connector](q_list)

    def __call__(self, *args, **kwargs):
        res = self._qresult(self.q_ins)
        if isinstance(res, list):
            return res[0]
        return res
