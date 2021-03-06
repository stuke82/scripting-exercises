from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solutions.py'):
    with reference_based_test('remove_duplicates') as testcase:
        testcase([])
        testcase([1])
        testcase([1, 1])
        testcase([1, 2])
        testcase([2, 1])
        testcase([1, 1, 1])
        testcase([1, 2, 3, 2, 1])
        testcase([5, 8, 6, 7, 8, 6, 3, 5])
        testcase(list(range(1_000_000)))
