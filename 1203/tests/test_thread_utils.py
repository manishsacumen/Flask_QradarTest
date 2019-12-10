from app.thread_utils import terminate_thread

import threading


class TestTerminateThread(object):
    def test_terminate_thread_isalive_false(self, mocker):
        thread_obj = threading.Thread()
        mocker.patch('threading.Thread.isAlive', return_value=False)
        terminate_thread(thread_obj)

    def test_terminate_thread_isalive_true(self, mocker):
        thread_obj = threading.Thread()
        mocker.patch('threading.Thread.isAlive', return_value=True)
        mocker.patch('threading.Thread.ident', return_value=8)
        terminate_thread(thread_obj)
