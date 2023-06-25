from typing import Any
import time
from functools import wraps


class StopwatchMaker(object):
    """
    Wrapper class that makes timing functions easier.
    If wrapped the function will be timed unless you pass in the keyword 'timed = False'.
    You can set the loading message with keyword 'loading_msg = ...' and end message with keyword 'end_msg = ...'.
    """

    def __init__(self, f):
        self._f = f

    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        timed: bool = True
        loading_msg: str = None
        end_msg: str = None

        if "timed" in kwds:
            timed = kwds.pop("timed")
        if "loading_msg" in kwds:
            loading_msg = kwds.pop("loading_msg")
        if "end_msg" in kwds:
            end_msg = kwds.pop("end_msg")

        if not timed:
            return self._f(*args, **kwds)


        if loading_msg:
            print(loading_msg)

        timer = time.time()
        ret = self._f(*args, **kwds)
        timer = time.time() - timer

        if end_msg:
            print(end_msg, end='')
        print(timer)
        return ret

    


class StopwatchMessageMaker:
    def __init__(self, loading_msg = None, end_msg = None) -> None:
        self._loading_msg = loading_msg
        self._end_msg = end_msg


    def __call__(self, f) -> any:
        lm = self._loading_msg
        em = self._end_msg

        class Stopwatch:
            def __init__(self, f) -> None:
                self._f = f
            
            def __call__(self, *args: Any, **kwds: Any) -> Any:

                if lm:
                    print(lm)
                
                timer = time.time()
                ret = self._f(*args, **kwds)  #check if you are acessing the right function
                timer = time.time() - timer

                if em:
                    print(em, end='')
                print(timer)
                return ret

        return Stopwatch(f)

                
                




# def stopwatch_factory(loading_msg: str = None, end_msg: str = None):
#     def timer(func, *params):
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
    
#     return timer



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


    


