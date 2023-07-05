import sys
import os
Executable_Path = sys.argv[0]
sys.path.append((os.path.dirname(os.path.abspath(Executable_Path))).replace("\\", "/")[0:-5])
from Main import SetBoard, ReadErd
from Erd_List import *
from FileCsv import Write_Data_CSV
from datetime import datetime


def Init(HEADERS, Board=1):
    Time = datetime.now().strftime("%H-%M-%S")
    Dia = datetime.now().strftime("%d-%m-%Y")

    Executable_Path = sys.argv[0]
    Actual_Path = os.path.dirname(os.path.abspath(Executable_Path))
    file_name_Test = "Results_" + Dia + "_" + Time
    file_Test = os.path.join(Actual_Path, file_name_Test + ".csv")

    SetBoard(Board)

    Write_Data_CSV(file_Test, ["App Version", ReadErd("C0", Erd_ApplicationVersion)])
    Write_Data_CSV(file_Test, ["Build Hash", ReadErd("C0", Erd_GitHash)[0:8]])
    Write_Data_CSV(file_Test, ["Build Number", ReadErd("C0", Erd_BuildNumber)])
    Write_Data_CSV(file_Test, ["Parametric Version", ReadErd("C0", Erd_ParametricVersion)])
    Write_Data_CSV(file_Test, ["MC Bootloader Version", ReadErd("C0", Erd_BootLoaderVersion)])
    Write_Data_CSV(file_Test, HEADERS)
    
    return file_Test