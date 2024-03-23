import pickle
import six
import sys

sys.setrecursionlimit(10**6)


class MetaNode(type):
    def __new__(mcs, name, bases, dict):
        attrs = list(dict['attrs'])
        dict['attrs'] = list()

        for base in bases:
            if hasattr(base, 'attrs'):
                dict['attrs'].extend(base.attrs)

        dict['attrs'].extend(attrs)

        return type.__new__(mcs, name, bases, dict)


@six.add_metaclass(MetaNode)
class Node(object):
    attrs = ()

    def __init__(self, **kwargs):
        values = kwargs.copy()

        for attr_name in self.attrs:
            value = values.pop(attr_name, None)
            setattr(self, attr_name, value)

        if values:
            raise ValueError('Extraneous arguments')

        self.begin_token = None
        self.end_token = None

    def __equals__(self, other):
        if type(other) is not type(self):
            return False

        for attr in self.attrs:
            if getattr(other, attr) != getattr(self, attr):
                return False

        return True

    def __repr__(self):
        attr_values = []
        for attr in sorted(self.attrs):
            attr_values.append('%s=%s' % (attr, getattr(self, attr)))
        return '%s(%s)' % (type(self).__name__, ', '.join(attr_values))

    def __iter__(self):
        return walk_tree(self)

    def filter(self, pattern):
        for path, node in self:
            if ((isinstance(pattern, (type, tuple)) and isinstance(node, pattern)) or
                (node == pattern)):
                yield path, node

    @property
    def children(self):
        return [getattr(self, attr_name) for attr_name in self.attrs]

    @property
    def begin_pos(self):
        if self.begin_token:
            return self.begin_token.begin_pos

    @property
    def end_pos(self):
        if self.end_token:
            return self.end_token.end_pos

    def tokens(self, type=None):
        if self.begin_token and self.end_token:
            cur_token = self.begin_token
            while True:
                if type is None:
                    yield cur_token
                elif isinstance(cur_token, type):
                    yield cur_token
                if cur_token is self.end_token:
                    break
                cur_token = cur_token.next

def walk_tree(root):
    children = None

    if isinstance(root, Node):
        yield (), root
        children = root.children
    else:
        children = root

    for child in children:
        if isinstance(child, (Node, list, tuple)):
            for path, node in walk_tree(child):
                yield (root,) + path, node

def dump(ast, file):
    pickle.dump(ast, file)

def load(file):
    return pickle.load(file)
