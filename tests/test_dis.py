from dictmatching import _dis


def test_dis_parsing():
    # Not actual bytecode!
    code_to_dis = '''
 25           0 LOAD_GLOBAL              0 (_capture_stdout)
              3 CALL_FUNCTION            0
              6 SETUP_WITH              17 (to 26)
              9 STORE_FAST               1 (output)

 26          12 LOAD_GLOBAL              1 (_dis)
             15 LOAD_FAST                0 (obj)
        >>   18 CALL_FUNCTION            1
             21 POP_TOP
             22 POP_BLOCK
             23 LOAD_CONST               0 (None)
    --> >>   26 WITH_CLEANUP
             27 END_FINALLY

 27          28 LOAD_GLOBAL              2 (_parse_dis_output)
             31 LOAD_FAST                1 (output)
             34 LOAD_ATTR                3 (getvalue)
             37 CALL_FUNCTION            0
             40 CALL_FUNCTION            1
             43 RETURN_VALUE
'''
    ops = list(_dis.parse_dis_output(code_to_dis))
    assert ops[0] == (25, False, False, 0, 'LOAD_GLOBAL', 0, '_capture_stdout')
    assert ops[1] == (25, False, False, 3, 'CALL_FUNCTION', 0, None)
    assert ops[2] == (25, False, False, 6, 'SETUP_WITH', 17, 'to 26')
    assert ops[6] == (26, False, True, 18, 'CALL_FUNCTION', 1, None)
    assert ops[10] == (26, True, True, 26, 'WITH_CLEANUP', None, None)
    assert ops[-1] == (27, False, False, 43, 'RETURN_VALUE', None, None)


def test_capturing():
    with _dis._capture_stdout() as buf:
        print('hi')
    assert buf.getvalue() == 'hi\n'
