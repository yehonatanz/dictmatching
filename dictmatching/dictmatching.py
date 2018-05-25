import inspect
import itertools

from decorator import contextmanager

from ._dis import dis


@contextmanager
def unpack(dictionary):
    # +1 for unpack and +1 that @contextmanager adds
    dest = _get_with_destination(inspect.currentframe(2))
    if isinstance(dest, tuple):
        yield tuple(dictionary[key] for key in dest)
    else:
        yield dictionary[dest]


def _get_with_destination(unpacker_frame):
    line_ops = (
        op for op in dis(unpacker_frame.f_code)
        if op.lineno == unpacker_frame.f_lineno
    )
    line_ops = list(line_ops)
    # Dispose SETUP_WITH
    after_with = list(itertools.dropwhile(
        lambda op: op.name != 'SETUP_WITH',
        line_ops
    ))[1:]
    if after_with[0].name == 'STORE_FAST':
        # A single variable unpacking
        return after_with[0].desc
    else:
        # Multi variables unpacking, dispose of UNPACK_SEQUENCE
        store_ops = itertools.takewhile(
            lambda op: op.name == 'STORE_FAST',
            after_with[1:]
        )
        return tuple(store_op.desc for store_op in store_ops)
