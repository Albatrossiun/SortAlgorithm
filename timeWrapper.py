# coding=utf-8
import time
 
def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        fn(*args, **kwargs)
        print("[{}]花费了[{}s]的时间完成排序".format(fn.__name__, time.perf_counter() - start))
    return _wrapper