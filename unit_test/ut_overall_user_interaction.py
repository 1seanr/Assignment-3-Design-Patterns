import unittest
from unittest.mock import patch
from contextlib import contextmanager
from io import StringIO
import sys

from cmd_controller import CmdController
from cmd_view import CmdView
from db_pickle_view import DBPickleView
from db_view import DBView
from excel_import_view import ExcelView
from matplot_view import MatPlotView


class OverallUserInteraction(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.con = CmdController(CmdView(), ExcelView(), DBView(),
                                 MatPlotView(), DBPickleView())

        self.con_view = CmdView()
        self.con_view.set_controller(self.con)

    def tearDown(self):
        # be executed after each test case
        print('End of Test\n\n')

    def runTests2(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer), \
             patch('sys.stdout', new=StringIO()) as output:
            sys.argv.append('load')
            print(sys.argv[1])
            self.con.go(self.con)
            self.assertEqual(expected_out, output.getValue().strip())

    def runTests(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer), \
             patch('sys.stdout', new=StringIO()) as output:
            self.con.go(self.con)
            self.assertEqual(expected_out, output.getValue().strip())

    def test_set_controller(self):
        self.runTests("quit", "Bye")

    def test_set_controller2(self):
        self.runTests2("quit", "Bye")

    @contextmanager
    def captured_output(self):
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    def test_run_quit(self):
        with self.captured_output() as (out, err):
            self.con_view.do_quit('')
        output = out.getvalue().strip()
        self.assertEqual(output, 'Bye')

    def test_run_output_list(self):
        with self.captured_output() as (out, err):
            self.con_view.output_list(['a', 'b'])
        output = out.getvalue().strip()
        self.assertEqual(output, 'a\nb')

    def test_run_load(self):
        with self.captured_output() as (out, err):
            self.con_view.do_load('')
        output = out.getvalue().strip()
        self.assertEqual(output, "[('T123', 'M', 20, 654, 'Normal', 56, "
                                 "'1996-10-18'), ('G834', 'M', 54, 213, "
                                 "'Overweight', 566, '1990-12-4'), ('S931', "
                                 "'F', 80, 986, 'Obesity', 852, '2001-5-1'), "
                                 "('P912', 'M', 34, 43, 'Underweight', 135, "
                                 "'1998-7-26'), ('B720', 'F', 67, 867, "
                                 "'Normal', 741, '1993-1-6')]")

    def test_run_save(self):
        with self.captured_output() as (out, err):
            self.con_view.do_save('')
        output = out.getvalue().strip()
        self.assertEqual(output, "Please validate the data using the "
                                 "'validate' command")

    def test_run_import(self):
        with self.captured_output() as (out, err):
            self.con_view.do_import('')
        output = out.getvalue().strip()
        self.assertEqual(output, 'Invalid use of the command')

    def test_run_validate(self):
        with self.captured_output() as (out, err):
            self.con_view.do_validate('')
        output = out.getvalue().strip()
        self.assertEqual(output, 'Data is valid you can now save')

    def test_run_view(self):
        with self.captured_output() as (out, err):
            self.con_view.do_view('')
        output = out.getvalue().strip()
        self.assertEqual(output, '')

    def test_run_matplot(self):
        with self.captured_output() as (out, err):
            self.con_view.do_matplot('')
        output = out.getvalue().strip()
        self.assertEqual(output, '')

    def test_run_savebd(self):
        with self.captured_output() as (out, err):
            self.con_view.do_savedb('')
        output = out.getvalue().strip()
        self.assertEqual(output, 'Invalid use of the command')

    def test_run_loaddb(self):
        with self.captured_output() as (out, err):
            self.con_view.do_loaddb('')
        output = out.getvalue().strip()
        self.assertEqual(output, 'Invalid use of the command')





    # def test_load_command(self):
    #     with patch('sys.stdout', new=StringIO()) as output:
    #         self.con_view.do_load('')
    #     expected = []
    #     self.assertEqual(expected, output.getValue().strip())


        #self.runTests("loaddb", "Bye")

    # def test_set_controller(self):
    #     self.runTests("quit", "Bye")
    #
    # def test_set_controller(self):
    #     self.runTests("quit", "Bye")
    #
    # def test_set_controller(self):
    #     self.runTests("quit", "Bye")
    #
    # def test_set_controller(self):
    #     self.runTests("quit", "Bye")
    #
    # def test_set_controller(self):
    #     self.runTests("quit", "Bye")


