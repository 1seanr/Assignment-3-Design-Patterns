"""
>>> controller = Cc(Cv(), Ev(), Dbv(), Mpv(), Dbpv())
Opened successfully
Inserted Initial DB Entries
>>> print("a1")
a1
>>> controller.import_from_excel("TestFile.xls")
... #doctest: +NORMALIZE_WHITESPACE
The data imported is:
[['A123', 'M', 16.0, 123.0, 'Normal', 23.0, '20-10-2000'],
['A124', 'F', 16.0, 124.0, 'Normal', 24.0, '21-11-2000'],
['A125', 'M', 22.0, 129.0, 'Underweight', 29.0, '10-9-1994'],
['A126', 'M', 22.0, 129.0, 'Underweight', 29.0, '10-9-1994'],
['A127', 'M', 24.0, 127.0, 'Overweight', 27.0, '8-7-1992'],
['A128', 'F', 23.0, 128.0, 'Overweight', 28.0, '9-8-1993'],
['A129', 'M', 22.0, 129.0, 'Underweight', 29.0, '10-9-1994'],
['A130', 'F', 21.0, 130.0, 'Underweight', 30.0, '11-10-1995'],
['A131', 'M', 36.0, 131.0, 'Normal', 31.0, '3-4-1980'],
['A132', 'F', 31.0, 132.0, 'Overweight', 32.0, '8-7-1985']]


>>> print("a2")
a2
>>> controller.import_from_excel("TestingDir\TestFile.xls")
... #doctest: +NORMALIZE_WHITESPACE
The data imported is:
[['A123', 'M', 16.0, 123.0, 'Normal', 23.0, '20-10-2000'],
['A124', 'F', 16.0, 124.0, 'Normal', 24.0, '21-11-2000'],
['A125', 'M', 22.0, 129.0, 'Underweight', 29.0, '10-9-1994'],
['A126', 'M', 22.0, 129.0, 'Underweight', 29.0, '10-9-1994'],
['A127', 'M', 24.0, 127.0, 'Overweight', 27.0, '8-7-1992'],
['A128', 'F', 23.0, 128.0, 'Overweight', 28.0, '9-8-1993'],
['A129', 'M', 22.0, 129.0, 'Underweight', 29.0, '10-9-1994'],
['A130', 'F', 21.0, 130.0, 'Underweight', 30.0, '11-10-1995'],
['A131', 'M', 36.0, 131.0, 'Normal', 31.0, '3-4-1980'],
['A132', 'F', 31.0, 132.0, 'Overweight', 32.0, '8-7-1985']]


>>> print("a4")
a4
>>> controller.import_from_excel("hello")
['Invalid use of the command']


>>> print("b1")
b1
>>> controller.load_from_db("")  #doctest: +NORMALIZE_WHITESPACE
[('T123', 'M', 20, 654, 'Normal', 56, '1996-10-18'),
('G834', 'M', 54, 213, 'Overweight', 566, '1990-12-4'),
('S931', 'F', 80, 986, 'Obesity', 852, '2001-5-1'),
('P912', 'M', 34, 43, 'Underweight', 135, '1998-7-26'),
('B720', 'F', 67, 867, 'Normal', 741, '1993-1-6')]

>>> print("b2")
b2
>>> controller.load_from_db("EMPID Age>20")
[('G834',), ('S931',), ('P912',), ('B720',)]

>>> print("b3")
b3
>>> controller.load_from_db("EMPID")
'Invalid use of the command'

>>> print("b4")
b4
>>> controller.load_from_db("Age>20")
'Invalid use of the command'


>>> print("d1")
d1
>>> controller.validate_data()
'Data is valid you can now save'
>>> controller.save_to_db()
'Saved successfully'

>>> print("d2")
d2
>>> controller.import_from_excel("TestingDir\\Test"
... "FileWithClashingPrimaryKeys.xls") #doctest: +NORMALIZE_WHITESPACE
The data imported is:
[['A200', 'M', 22.0, 129.0, 'Underweight', 29.0, '10-9-1994'],
['T123', 'F', 21.0, 130.0, 'Underweight', 30.0, '11-10-1995'],
['P912', 'M', 36.0, 131.0, 'Normal', 31.0, '3-4-1980'],
['A201', 'F', 31.0, 132.0, 'Overweight', 32.0, '8-7-1985']]
>>> controller.validate_data()
'Data is valid you can now save'
>>> controller.save_to_db() #doctest: +NORMALIZE_WHITESPACE
Could not save data to the data base due to conflicting primary
keys or other compromised data
On line 2
All other rows have been saved
Could not save data to the data base due to conflicting primary
keys or other compromised data
On line 3
All other rows have been saved
'Saved successfully'

>>> print("d3")
d3
>>> controller.import_from_excel("TestFile.xls")#doctest: +NORMALIZE_WHITESPACE
The data imported is:
[['A123', 'M', 16.0, 123.0, 'Normal', 23.0, '20-10-2000'],
['A124', 'F', 16.0, 124.0, 'Normal', 24.0, '21-11-2000'],
['A125', 'M', 22.0, 129.0, 'Underweight', 29.0, '10-9-1994'],
['A126', 'M', 22.0, 129.0, 'Underweight', 29.0, '10-9-1994'],
['A127', 'M', 24.0, 127.0, 'Overweight', 27.0, '8-7-1992'],
['A128', 'F', 23.0, 128.0, 'Overweight', 28.0, '9-8-1993'],
['A129', 'M', 22.0, 129.0, 'Underweight', 29.0, '10-9-1994'],
['A130', 'F', 21.0, 130.0, 'Underweight', 30.0, '11-10-1995'],
['A131', 'M', 36.0, 131.0, 'Normal', 31.0, '3-4-1980'],
['A132', 'F', 31.0, 132.0, 'Overweight', 32.0, '8-7-1985']]
>>> controller.save_to_db()
"Please validate the data using the 'validate' command"
"""
from cmd_controller import CmdController as Cc
from cmd_view import CmdView as Cv
from db_pickle_view import DBPickleView as Dbpv
from db_view import DBView as Dbv
from excel_import_view import ExcelView as Ev
from matplot_view import MatPlotView as Mpv

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
