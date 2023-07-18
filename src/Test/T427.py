from Initialize import *
from ATDocumentation import AutoDocumentation
from ATErds import *
from UiTable import TableResults

file_Test = Init(Board=1)

Step1  = Read ("C0", Erd_EndOfCycleReason,               "00",     file_Test)    # Step 1
Step2  = Read ("C0", Erd_UI_MachineStateEnter,           "00",     file_Test)    # Step 2
Step3  = Read ("C0", Erd_CriticalFault,                  "00",     file_Test)    # Step 3
Step4  = Read ("C0", Erd_OredShutDownUIFaults,           "00",     file_Test)    # Step 4
# Test 2: When Erd_CriticalFault is set, the EOC reason should be Fault
Step5  = Write("C0", Erd_UI_MachineStateEnter,           "08",     file_Test)    # Step 5
Step6  = Write("C0", Erd_CriticalFault,                  "01",     file_Test)    # Step 6
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
Step27 = Read ("C0", Erd_EndOfCycleReason,               "00",     file_Test)
Step28 = Read ("C0", Erd_EndOfCycleReason,               "01",     file_Test)
Step29 = Write("C0", Erd_UI_MachineStateEnter,           "02",     file_Test)
Step30 = Read ("C0", Erd_EndOfCycleReason,               "04",     file_Test)

lst = [HEADERS,Step1, Step2, Step3, Step4, Step5, Step6, Step7, Step8, Step9, Step10, Step11,
    Step12, Step13, Step14, Step15, Step16, Step17, Step18, Step19, Step20, Step21,
    Step22, Step23, Step24, Step25, Step26, Step27, Step28, Step29, Step30]

TableResults(lst)