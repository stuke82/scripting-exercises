from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solutions.py'):
    with reference_based_test('is_increasing') as testcase:
        testcase([])
        testcase([1])
        testcase([1, 2])
        testcase([1, 1])
        testcase([2, 1])
        testcase([1, 2, 3])
        testcase([1, 3, 6, 8])
        testcase([1, 3, 6, 8, 2])
        testcase([1, 4, 7, 5, 8])
