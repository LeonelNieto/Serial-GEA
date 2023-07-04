import sys
sys.path.append("D:/GEA3 Python/src")

import os
from ATErds import *
from FileCsv import *
from Erd_List import *
from Main import SetBoard
from datetime import datetime

Time = datetime.now().strftime("%H-%M-%S")
Dia = datetime.now().strftime("%d-%m-%Y")

Executable_Path = sys.argv[0]
Actual_Path = os.path.dirname(os.path.abspath(Executable_Path))
file_name_Test = "T1_Results_" + Dia + "_" + Time
file_Test = os.path.join(Actual_Path, file_name_Test + ".csv")

HEADERS = ["Date", "Time", "Action", "ERD", "Expected Data", "Data", "Data to Write", "Result", "Comments"]
Write_Data_CSV(file_Test, HEADERS)

SetBoard(1)

#Action, dst, ERD, Expected data/data to write, path file
Read ("C0", Erd_UI_CycleSelection,              "00",     file_Test)    # Step 1
Read ("C0", Erd_MC_CycleEngineRequestState,     "000005", file_Test)    # Step 2
Read ("C0", Erd_UI_MachineStateEnter,           "00",     file_Test)    # Step 3
Read ("C0", Erd_UI_MachineStateExit,            "00",     file_Test)    # Step 4
Write("C0", Erd_UI_CycleSelection,              "01",     file_Test)    # Step 5
Read ("C0", Erd_LaundryCurrentSelectedCycle,    "05",     file_Test)    # Step 6
Read ("C0", Erd_MC_CycleEngineRequestState,     "000105", file_Test)    # Step 7
Read ("C0", Erd_MC_CycleEngineActualState,      "010A",   file_Test)    # Step 8
Write("C0", Erd_UI_MachineStateEnter,           "08",     file_Test)    # Step 9
Read ("C0", Erd_UI_CycleSelection,              "01",     file_Test)    # Step 10
Read ("C0", Erd_MC_CycleEngineRequestState,     "000101", file_Test)    # Step 11
Read ("C0", Erd_MC_CycleEngineActualState,      "0106",   file_Test)    # Step 12
Read ("C0", Erd_AutoSoakLevelOption,            "00",     file_Test)    # Step 13
Read ("C0", Erd_DeepFillIncrementalOption,      "00",     file_Test)    # Step 14
Read ("C0", Erd_ExtraRinseOption,               "00",     file_Test)    # Step 15
Read ("C0", Erd_SoilLevelOption,                "03",     file_Test)    # Step 16
Read ("C0", Erd_StainRemovalGuideOption,        "00",     file_Test)    # Step 17
Read ("C0", Erd_WaterOnDemandSoapDispenseOption,"00",     file_Test)    # Step 18
Read ("C0", Erd_ControlLockOption,              "00",     file_Test)    # Step 19
Read ("C0", Erd_DelayWashOption,                "00",     file_Test)    # Step 20
Read ("C0", Erd_FabricSoftenerOption,           "00",     file_Test)    # Step 21
Read ("C0", Erd_SpinLevelOption,                "03",     file_Test)    # Step 22
Read ("C0", Erd_WarmRinseOption,                "00",     file_Test)    # Step 23
Read ("C0", Erd_WaterTemperatureOption,         "02",     file_Test)    # Step 24
Write("C0", Erd_UI_CycleSelection,              "03",     file_Test)    # Step 25
Read ("C0", Erd_LaundryCurrentSelectedCycle,    "04",     file_Test)    # Step 26
Read ("C0", Erd_MC_CycleEngineRequestState,     "000305", file_Test)    # Step 27
Read ("C0", Erd_MC_CycleEngineActualState,      "030A",   file_Test)    # Step 28
Read ("C0", Erd_AutoSoakLevelOption,            "01",     file_Test)    # Step 29
Read ("C0", Erd_DeepFillIncrementalOption,      "02",     file_Test)    # Step 30
Read ("C0", Erd_ExtraRinseOption,               "00",     file_Test)    # Step 31
Read ("C0", Erd_SoilLevelOption,                "02",     file_Test)    # Step 32
Read ("C0", Erd_StainRemovalGuideOption,        "05",     file_Test)    # Step 33
Read ("C0", Erd_WaterOnDemandSoapDispenseOption,"00",     file_Test)    # Step 34
Read ("C0", Erd_ControlLockOption,              "01",     file_Test)    # Step 35
Read ("C0", Erd_DelayWashOption,                "00",     file_Test)    # Step 36
Read ("C0", Erd_FabricSoftenerOption,           "00",     file_Test)    # Step 37
Read ("C0", Erd_SpinLevelOption,                "01",     file_Test)    # Step 38
Read ("C0", Erd_WarmRinseOption,                "01",     file_Test)    # Step 39
Read ("C0", Erd_WaterTemperatureOption,         "05",     file_Test)    # Step 40

#Back to start
Write("C0", Erd_Reset,                          "01",     file_Test)
# Write("C0", Erd_UI_CycleSelection,              "00",     file_Test)    # Step 5
