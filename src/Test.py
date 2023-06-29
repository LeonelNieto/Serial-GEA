import Main
import Erd_List as Erdl
import FileCsv
import sys
import os
import time
from datetime import datetime

Executable_Path = sys.argv[0]
Actual_Path = os.path.dirname(os.path.abspath(Executable_Path))
file_name_Test = "T1_Results"
file_Test = os.path.join(Actual_Path, file_name_Test + ".csv")

HEADERS = ["Date", "Time", "Action", "ERD", "Expected Data", "Data", "Data to Write", "Result", "Comments"]
FileCsv.Write_Data_CSV(file_Test, HEADERS)

Main.SetBoard(0)

def Read(dst, ERD, Expected_Data ,Path):
    Time = datetime.now().strftime("%H:%M:%S")
    Dia = datetime.now().strftime("%d-%m-%Y")
    Data = Main.ReadErd(dst, ERD)
    Action = "READ"
    if Data == Expected_Data:
        Result = "PASS"
    else:
        Result = "FAIL"
    Write_Dato = "---" 
    Data_To_Write = [Dia, Time, Action, ERD, Expected_Data, Data, Write_Dato ,Result]
    FileCsv.Write_Data_CSV(Path, Data_To_Write)
    print(Data_To_Write)
    
def Write(dst, ERD, Write_Dato ,Path):
    Time = datetime.now().strftime("%H:%M:%S")
    Dia = datetime.now().strftime("%d-%m-%Y")
    Main.WriteButton(dst, ERD, Write_Dato)
    Action = "WRITE"
    Expected_Data = "---"
    Result = "DONE"
    Data = "---"
    Data_To_Write = [Dia, Time, Action, ERD, Expected_Data, Data, Write_Dato ,Result]
    FileCsv.Write_Data_CSV(Path, Data_To_Write)
    print(Data_To_Write)
    
Read("C0", Erdl.Erd_ResetCount, "000000D2", file_Test)
Read("C0", Erdl.Erd_Reset, "00", file_Test)
Read("C0", Erdl.Erd_MbKeyStatusWord, "00", file_Test)
time.sleep(0.3)
Write("C0", Erdl.Erd_Reset, "01", file_Test)
time.sleep(3.2)