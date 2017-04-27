import unittest

import sys

sys.path.append("..")

from unit_test.ut_db_handling import *
from unit_test.ut_graph_displaying import *
from unit_test.ut_pickle_saving_and_loading import *
from unit_test.ut_validating_and_viewing_imported_data import *
from unit_test.ut_excel_import import *


def suite():
    the_suite = unittest.TestSuite()
    '''
    suite1.addTest(FooTests1("test_one"))
    suite1.addTest(FooTests1("test_two"))
    suite1.addTest(FooTests1("test_hello_world"))
    suite1.addTest(FooTests2("test_three"))
    '''
    the_suite.addTest(unittest.makeSuite(DBSavingAndLoadingTests))
    the_suite.addTest(unittest.makeSuite(ExcelImportingTests))
    the_suite.addTest(unittest.makeSuite(GraphingTests))
    the_suite.addTest(unittest.makeSuite(PickleSaveAndLoadTests))
    the_suite.addTest(unittest.makeSuite(ValidatingAndViewingTests))
    return the_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    # runner = unittest.TextTestRunner(descriptions=True, verbosity=2)
    test_suite = suite()
    runner.run(test_suite)