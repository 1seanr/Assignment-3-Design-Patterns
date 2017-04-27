from unit_test.ut_db_handling import *
from unit_test.ut_graph_displaying import *
from unit_test.ut_pickle_saving_and_loading import *
from unit_test.ut_validating_and_viewing_imported_data import *
from unit_test.ut_excel_import import *
from unit_test.ut_overall_user_interaction import *


def suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(DBSavingAndLoadingTests))
    the_suite.addTest(unittest.makeSuite(ExcelImportingTests))
    the_suite.addTest(unittest.makeSuite(GraphingTests))
    the_suite.addTest(unittest.makeSuite(PickleSaveAndLoadTests))
    the_suite.addTest(unittest.makeSuite(ValidatingAndViewingTests))
    the_suite.addTest(unittest.makeSuite(OverallUserInteraction))
    return the_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    # runner = unittest.TextTestRunner(descriptions=True, verbosity=2)
    test_suite = suite()
    runner.run(test_suite)
