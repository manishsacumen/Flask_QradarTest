__author__ = 'Sacumen(www.sacumen.com)'

import ctypes


def terminate_thread(thread):
    """Terminates thread

    :param thread: Thread instance
    """
    if not thread.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
