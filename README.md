# pyobj_Q
#### 简单介绍:
>[pyobj_Q](https://github.com/xmdevops/pyobj_Q) 主要用于对任意PY对象构造动态条件查询判断,支持无限级递归,完全兼容Djago Q语法,兼容PY2.7+

***


#### 开发环境:
> SY_ENV: MacOS 10.12.6 \
> PY_ENV: Python2.7.10 

***

#### 快速安装:
`git clone https://github.com/xmdevops/pyobj_Q` \
`cd pyobj_Q` \
`python setup.py install` 

***

#### 使用方法:
```python
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
```
***

#### Copyright:
2017.12.08  (c) Limanman <xmdevops@vip.qq.com>

