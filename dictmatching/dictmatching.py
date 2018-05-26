import inspect
import itertools

from decorator import contextmanager

from ._dis import dis


@contextmanager
def unpack(dictionary):
    # +1 for unpack and +1 that @contextmanager adds
    dest = _get_with_destination(inspect.currentframe().f_back.f_back)
    if isinstance(dest, tuple):
        yield tuple(dictionary[key] for key in dest)
    else:
        yield dictionary[dest]


def _get_with_destination(unpacker_frame):
    after_unpack = (
        op for op in dis(unpacker_frame.f_code)
        if op.offset >= unpacker_frame.f_lasti and op.name != 'EXTENDED_ARG'
    )
    # Dispose SETUP_WITH
    after_unpack = list(after_unpack)[1:]
    if after_unpack[0].name == 'STORE_FAST':
        # A single variable unpacking
        return after_unpack[0].desc
    else:
        # Multi variables unpacking, dispose of UNPACK_SEQUENCE
        store_ops = itertools.takewhile(
            lambda op: op.name == 'STORE_FAST',
            after_unpack[1:]
        )
        return tuple(store_op.desc for store_op in store_ops)
