import sys
sys.path.append("D:/GEA3 Python/src")

import os
from ATErds import *
from FileCsv import *
from Erd_List import *

Executable_Path = sys.argv[0]
Actual_Path = os.path.dirname(os.path.abspath(Executable_Path))
file_name_Test = "T1_Results"
file_Test = os.path.join(Actual_Path, file_name_Test + ".csv")

HEADERS = ["Date", "Time", "Action", "ERD", "Expected Data", "Data", "Data to Write", "Result", "Comments"]

Write_Data_CSV(file_Test, HEADERS)
Read("C0", Erd_Reset, "00", file_Test)
Read("C0", Erd_MbKeyStatusWord, "000000", file_Test)
Read("C0", Erd_ResetCount, "0000C9", file_Test)