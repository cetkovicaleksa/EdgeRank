



from typing import Any
import time


class StopwatchMaker(object):
    """Self calling. Sluzi za tajmiranje ucitavanja podataka koji se ucitavaju odmah pri pokretanju
    programa. """

    def __init__(self, f):
        self._f = f


    # def __init__(self, *args, loading_msg = None, end_msg = None):
    #     self._loading_msg = loading_msg
    #     self._end_msg = end_msg
    #     self._args = args


    # def __call__(self, f):

    #     if self._loading_msg:
    #         print(self._loading_msg)

    #     timer = time.time()
    #     ret = f(*self._args)
    #     timer = time.time() - timer

    #     if self._end_msg:
    #         print(self._end_msg, end='')
        
    #     print(timer)
    #     return ret
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if "loading_msg" in kwds:
            print(kwds["loading_msg"])

        timer = time.time()
        ret = self._f(*args)
        timer = time.time() - timer

        if "end_msg" in kwds:
            print(kwds["end_msg"], end='')
        print(timer)
        return ret
    







def stopwatch_factory(loading_msg: str = None, end_msg: str = None):
    def timer(func, *params):
        if loading_msg: print(loading_msg)
        
        timer = time.time()
        try:
            ret = func(*params) if params and func else func() if func else None
        except BaseException as e:
            raise    
        timer = time.time() - timer

        if end_msg: print(end_msg, end="")
        print(f'{timer:^4}')
        return ret
    
    return timer



# @staticmethod
#     def timed(func: callable = lambda *args: None, *params,  loading_msg: str = None, end_msg: str = None) -> any:
#         """Prints out a loading_msg and calls the passed func with given params.
#         After the execution of given function prints out the end_msg followed by the time it took func to complete."""

#         if loading_msg: print(loading_msg)
        
#         timer = time.time()
#         try:
#             ret = func(*params) if params and func else func() if func else None
#         except BaseException as e:
#             raise    
#         timer = time.time() - timer

#         if end_msg: print(end_msg, end="")
#         print(f'{timer:^4}')
#         return ret


    


