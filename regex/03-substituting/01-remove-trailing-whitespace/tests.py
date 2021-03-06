from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solutions.py'):
    with reference_based_test('remove_trailing_whitespace') as testcase:
        testcase('''
        fdjfkld jfjs fjdslfk
        ''')

        testcase('''
        fdf qqip saofp k
        fjdklfj f sfjslkf
        fdjfkldjf
        ''')

