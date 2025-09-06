class ReverseListIterator:
    def __init__(self, data):
        self._data = list(data)
        self._idx = len(self._data)  

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx == 0:
            raise StopIteration
        self._idx -= 1
        return self._data[self._idx]



class EvenRange:
    def __init__(self, n: int):
        self._n = n
        self._cur = 0 if n >= 0 else 2

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur > self._n:
            raise StopIteration
        val = self._cur
        self._cur += 2
        return val
