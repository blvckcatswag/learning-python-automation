import pytest

from lesson_18.generator import gen_even, gen_fib_upto
from lesson_18.iterators import ReverseListIterator, EvenRange
from lesson_18.decorators import log_call, catch_and_handle

def test_gen_even_basic():
    assert list(gen_even(0)) == [0]
    assert list(gen_even(1)) == [0]
    assert list(gen_even(7)) == [0, 2, 4, 6]
    assert list(gen_even(8)) == [0, 2, 4, 6, 8]

def test_fib_upto_basic():
    assert list(gen_fib_upto(0)) == [0]
    assert list(gen_fib_upto(1)) == [0, 1, 1]
    assert list(gen_fib_upto(10)) == [0, 1, 1, 2, 3, 5, 8]

def test_reverse_list_iterator():
    data = [1, 2, 3]
    assert list(ReverseListIterator(data)) == [3, 2, 1]

def test_even_range_iterator():
    assert list(EvenRange(5)) == [0, 2, 4]
    assert list(EvenRange(0)) == [0]

def test_log_call_decorator(capsys):
    @log_call()
    def mul(a, b): return a * b
    assert mul(2, 3) == 6
    out = capsys.readouterr().out
    assert "[call] mul" in out and "[ret ] mul -> 6" in out

def test_catch_and_handle_default():
    @catch_and_handle(default="Error")
    def div(a, b): return a / b
    assert div(1, 0) == "Error"

def test_catch_and_handle_handler():
    msgs = []
    def handler(e):
        msgs.append(type(e).__name__)
        return "ok"
    @catch_and_handle(handler=handler, exc_types=(ZeroDivisionError,))
    def div(a, b): return a / b
    assert div(1, 0) == "ok"
    assert msgs == ["ZeroDivisionError"]
