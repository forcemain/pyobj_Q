#! -*- coding: utf-8 -*-


from pyobj_Q.filter import Q, R
from pyobj_Q.types import Str, Int


def is_right(q):
    r = R(obj, q_ins=q)()

    return r


if __name__ == '__main__':
    obj = type('obj', (object,), {'name': Str('limanman'), 'age': Int(27), 'email': Str('xmdevops@vip.qq.com')})

    # True
    q = Q(obj__name__exact='limanman') & Q(obj__age__exact=27) & Q(obj__email__startswith='xmdevops')
    print is_right(q)

    # False
    q = Q(obj__name__exact='manmanli') | Q(obj__email__contains='manmanli')
    print is_right(q)

    # False
    q = Q(obj__name__exact='manmanli')
    q.add(Q(obj__email__contains='manmanli'), Q.OR)
    print is_right(q)

    # True
    q1 = Q()
    q1.connector = Q.OR
    q1.children.append(('obj__name__exact', 'limanman'))
    q1.children.append(('obj__email__contains', 'limanman'))

    q2 = Q()
    q2.connector = Q.AND
    q2.children.append(('obj__age__exact', '27'))
    q2.children.append(('obj__email__startswith', 'xmdevops'))

    q = Q()
    q.add(q1, Q.OR)
    q.add(q2, Q.OR)

    print is_right(q)




