class OrderedSet:
    def __init__(self, iterable=None):
        self._dict = dict()
        if iterable:
            for item in iterable:
                self._dict[item] = None

    def add(self, item):
        self._dict[item] = None

    def discard(self, item):
        self._dict.pop(item, None)

    def __contains__(self, item):
        return item in self._dict

    def __iter__(self):
        return iter(self._dict.keys())

    def __len__(self):
        return len(self._dict)

    def __repr__(self):
        return f"OrderedSet({list(self._dict.keys())})"

def find_first(seq, predicate):
    for elem in seq:
        if predicate(seq):
            return elem
    return None

def build_matrix(width, height, init_value = 0):
    matrix = [[init_value for _ in range(height)] for _ in range(width)]
    return matrix
