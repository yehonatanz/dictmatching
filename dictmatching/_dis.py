import re
import sys

from collections import namedtuple
from contextlib import contextmanager
from dis import dis as _dis

from six.moves import cStringIO as StringIO, map, filter


Op = namedtuple('Op', 'lineno lasti label offset name arg desc'.split())
OP_REGEX = re.compile(
    r'^'
    + r'^(?:(?P<lineno>\d+)\s)?'
    + r'(?:(?:(?P<lasti>-->)|\s{3})\s)?'
    + r'(?:(?:(?P<label>>>)|\s{2})\s)?'
    + r'\s*?(?P<offset>\d+)\s+'
    + r'\s*?(?P<name>\w+)'
    + r'(?:\s+(?P<arg>\d+)(?:\s+\((?P<desc>.*?)\))?)?'
    + r'$'
)


def dis(obj):
    with _capture_stdout() as output:
        _dis(obj)
    return _parse_dis_output(output.getvalue())


def _parse_dis_output(text):
    prev = None
    lines = filter(None, (line.strip() for line in text.splitlines()))
    for line in lines:
        op = _parse_line(line.strip())
        op = op._replace(lineno=op.lineno or prev.lineno)
        yield op
        prev = op


def _parse_line(line):
    matches = OP_REGEX.match(line).groupdict()
    return Op(
        lineno=int(matches['lineno']) if matches.get('lineno') else None,
        lasti=bool(matches.get('lasti')),
        label=bool(matches.get('label')),
        offset=int(matches['offset']),
        name=matches['name'],
        arg=int(matches['arg']) if matches.get('arg') else None,
        desc=matches.get('desc'),
    )


@contextmanager
def _capture_stdout():
    buf = StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        yield buf
    finally:
        sys.stdout = old
