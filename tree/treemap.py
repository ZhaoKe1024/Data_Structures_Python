# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2025-02-26 0:44
class KeyValue(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Map(object):
    def __init__(self):
        self.mapset = set()

    def is_empty(self):
        return len(self.mapset) > 0

    def size(self):
        pass

    def put(self, key, value):
        kv = KeyValue(key=key, value=value)
        if kv not in self.mapset:
            self.mapset.add(kv)
        else:
            self.remove(key)
            self.mapset.add(KeyValue(key, value))

    def remove(self, key):
        v = None
        for item in self.mapset:
            if key == item.key:
                v = item.value
                self.mapset.remove(item)
        return v

    def get(self, key):
        pass

    def containsKey(self, key):
        pass

    def values(self):
        pass


class SortedKeyValue(KeyValue):
    def __init__(self, key, value):
        super().__init__(key, value)

    def compareTo(self, kv):
        return self.key - kv.key


class TreeMap(object):
    pass
