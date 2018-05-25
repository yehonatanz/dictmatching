import inspect
import itertools

from decorator import contextmanager

from ._dis import dis


@contextmanager
def unpack(dictionary):
    key = _get_with_dest()
    yield dictionary[key]


def _get_with_dest():
    unpacker_frame = inspect.currentframe(3)
    line_ops = (
        op for op in dis(unpacker_frame.f_code)
        if op.lineno == unpacker_frame.f_lineno
    )
    after_with = itertools.dropwhile(
        lambda op: op.name != 'SETUP_WITH',
        line_ops
    )
    # Dispose SETUP_WITH
    next(after_with)
    dest_op = next(after_with)
    assert dest_op.name == 'STORE_FAST'
    return dest_op.desc
