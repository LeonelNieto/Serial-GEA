from Initialize import *
from ATDocumentation import AutoDocumentation
from ATErds import *
from UiTable import TableResults
from Functions import *

file_Test = Init()

# Test 1: Erd_EndOfCycleReason should be Unknown on init
Step1  = Read ("C0", Erd_EndOfCycleReason,               "00",     file_Test)
Step2  = Read ("C0", Erd_UI_MachineStateEnter,           "00",     file_Test)
Step3  = Read ("C0", Erd_CriticalFault,                  "00",     file_Test)
Step4  = Read ("C0", Erd_OredShutDownUIFaults,           "00",     file_Test)
   
# Test 2: When Erd_CriticalFault is set, the EOC reason should be Fault
Step5  = Write("C0", Erd_UI_MachineStateEnter,           "08",     file_Test)
Step6  = Write("C0", Erd_CriticalFault,                  "01",     file_Test)
Step7  = Read ("C0", Erd_EndOfCycleReason,               "05",     file_Test)

# Test 3: Erd_EndOfCycleReason should be Unknown when Erd_CriticalFault clears
Step8  = Write("C0", Erd_EndOfCycleReason,               "00",     file_Test)
Step9  = Write("C0", Erd_OredShutDownUIFaults,           "01",     file_Test)
Step10 = Write("C0", Erd_CriticalFault,                  "01",     file_Test) 
Step11 = Write("C0", Erd_UI_MachineStateEnter,           "08",     file_Test)
Step12 = Write("C0", Erd_CriticalFault,                  "00",     file_Test)
Step13 = Read ("C0", Erd_EndOfCycleReason,               "00",     file_Test)

# Test 4: Erd_EndOfCycleReason should update to Success when UI transitions from Run to EOC
Step14 = Write("C0", Erd_UI_MachineStateEnter,           "00",     file_Test)
Step15 = Write("C0", Erd_EndOfCycleReason,               "00",     file_Test)
Step16 = Write("C0", Erd_CriticalFault,                  "00",     file_Test)
Step17 = Write("C0", Erd_OredShutDownUIFaults,           "00",     file_Test)
Step18 = Write("C0", Erd_EndOfCycleReason,               "01",     file_Test)
Step19 = Write("C0", Erd_UI_MachineStateEnter,           "20",     file_Test)
Step20 = Read ("C0", Erd_EndOfCycleReason,               "02",     file_Test)

# Test 5: Erd_EndOfCycleReason should update to Power Button when transitions from Run to Idle
Step21 = Write("C0", Erd_UI_MachineStateEnter,           "00",     file_Test)
Step22 = Write("C0", Erd_EndOfCycleReason,               "00",     file_Test)
Step23 = Write("C0", Erd_EndOfCycleReason,               "01",     file_Test)
Step24 = Write("C0", Erd_UI_MachineStateEnter,           "01",     file_Test)
Step25 = Read ("C0", Erd_EndOfCycleReason,               "03",     file_Test)

# Test 6: Erd_EndOfCycleReason should update to Cycle Knob when UI transitions form Run to StandBy
Step26 = Write("C0", Erd_UI_MachineStateEnter,           "00",     file_Test)
Step27 = Write("C0", Erd_EndOfCycleReason,               "00",     file_Test)
Step28 = Write("C0", Erd_EndOfCycleReason,               "01",     file_Test)
Step29 = Write("C0", Erd_UI_MachineStateEnter,           "02",     file_Test)
Step30 = Read ("C0", Erd_EndOfCycleReason,               "04",     file_Test)
ResetUnit()

lst = [HEADERS, Step1, Step2, Step3, Step4, Step5, Step6, Step7, Step8, Step9, Step10, 
    Step11, Step12, Step13, Step14, Step15, Step16, Step17, Step18, Step19, Step20, 
    Step21, Step22, Step23, Step24, Step25, Step26, Step27, Step28, Step29, Step30]

TableResults(lst, "T427")

texto = """Test 1: Erd_EndOfCycleReason should be Unknown on init

Read Erd_EndOfCycleReason, shall be EndOfCycleReason_Unknown (00)
Read Erd_UI_MachineStateEnter, shall be UiState_Bootup (00)
Read Erd_CriticalFault, shall be false (00)
Read Erd_OredShutDownUIFaults, shall be false (00)

Test 2: When Erd_CriticalFault is set, the EOC reason should be Fault
Write UiState_Run (08) to Erd_UI_MachineStateEnter
Write true (01) to Erd_CriticalFault
Read Erd_EndOfCycleReason, shall be EndOfCycleReason_Fault (05)

Test 3: Erd_EndOfCycleReason should be Unknown when Erd_CriticalFault clears
Write EndOfCycleReason_Unknown (00) to Erd_EndOfCycleReason
Write true (01) to Erd_OredShutDownUIFaults
Write true (01) to Erd_CriticalFault
Write UiState_Run (08) to Erd_UI_MachineStateEnter
Write false (00) to Erd_CriticalFault
Read Erd_EndOfCycleReason, shall be EndOfCycleReason_Unknown (00)

Test 4: Erd_EndOfCycleReason should update to Success when UI transitions from Run to EOC
Write UiState_Bootup(00) to Erd_UI_MachineStateEnter
Write EndOfCycleReason_Unknown(00) to Erd_EndOfCycleReason
Write false(00) to Erd_CriticalFault
Write false(00) to Erd_OredShutDownUIFaults
Write EndOfCycleReason_Running (01) to Erd_EndOfCycleReason
Write UiState_EndOfCycle(20) to Erd_UI_MachineStateEnter
Read Erd_EndOfCycleReason, shall be EndOfCycleReason_Success(02)

Test 5: Erd_EndOfCycleReason should update to Power Button when transitions from Run to Idle
Write UiState_Bootup(00) to Erd_UI_MachineStateEnter
Write EndOfCycleReason_Unknown(00) to Erd_EndOfCycleReason
Write EndOfCycleReason_Running (01) to Erd_EndOfCycleReason
Write UiState_Idle(01) to Erd_UI_MachineStateEnter
Read Erd_EndOfCycleReason, shall be EndOfCycleReason_PowerButton(03)

Test 6: Erd_EndOfCycleReason should update to Cycle Knob when UI transitions form Run to StandBy
Write UiState_Bootup(00) to Erd_UI_MachineStateEnter
Write EndOfCycleReason_Unknown(00) to Erd_EndOfCycleReason
Write EndOfCycleReason_Running (01) to Erd_EndOfCycleReason
Write UiState_Standby(02) to Erd_UI_MachineStateEnter
Read Erd_EndOfCycleReason, shall be EndOfCycleReason_CycleKnob(04)"""

AutoDocumentation(texto)