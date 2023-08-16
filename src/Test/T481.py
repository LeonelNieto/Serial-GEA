from Initialize import *
from ATDocumentation import AutoDocumentation
from ATErds import *
from UiTable import TableResults
from Functions import *

file_Test = Init()

# Step1 = ActionPassOrFail("Temp and spin level leds shall turn on")
# Step2 = ActionPassOrFail("Verify both lights shall be ON")
# Step3 = ToDoTimedAction(10, "Press and Hold Lid for 10 seconds")
# Step4 = ActionDone("Disconnect and connect the unit")

Step1  = Write("C0", Erd_MabeCommunicationConfiguration,  "01",     file_Test)
Step3  = Write("C0", Erd_MabeCommunicationRequest1Levels, "0011",   file_Test)
Step2  = ActionPassOrFail("Temp and spin level leds shall turn on in level 1")
Step4  = Write("C0", Erd_MabeCommunicationRequest1Levels, "0022",   file_Test)
Step5  = ActionPassOrFail("Temp and spin level leds shall turn on in level 2")
Step6  = Write("C0", Erd_MabeCommunicationRequest1Levels, "0033",   file_Test)
Step7  = ActionPassOrFail("Temp and spin level leds shall turn on in level 3")
Step8  = Write("C0", Erd_MabeCommunicationRequest1Levels, "0044",   file_Test)
Step9  = ActionPassOrFail("Temp and spin level leds shall turn on in level 4")
Step10 = Write("C0", Erd_MabeCommunicationRequest1Levels, "0055",   file_Test)
Step11 = ActionPassOrFail("Temp and spin level leds shall turn on in level 5")
Step10 = Write("C0", Erd_MabeCommunicationRequest1Levels, "0000",   file_Test)
Step11 = ActionPassOrFail("Temp and spin level leds shall turn off")
# Step10 = Read ("C0", Erd_EndOfCycleReason,               "00",     file_Test)

# Step11 = Write("C0", Erd_UI_MachineStateEnter,           "00",     file_Test)
# Step12 = Write("C0", Erd_EndOfCycleReason,               "00",     file_Test)
# Step13 = Write("C0", Erd_CriticalFault,                  "00",     file_Test)
# Step14 = Write("C0", Erd_OredShutDownUIFaults,           "00",     file_Test)
# Step15 = Write("C0", Erd_EndOfCycleReason,               "01",     file_Test)
# Step16 = Write("C0", Erd_UI_MachineStateEnter,           "20",     file_Test)
# Step17 = Read ("C0", Erd_EndOfCycleReason,               "02",     file_Test)

# ResetUnit()

lst = [HEADERS, Step1, Step2, Step3, Step4]

# lst = [HEADERS, Step1, Step2, Step3, Step4, Step5, Step6, Step7, Step8, Step9, Step10, 
#     Step11, Step12, Step13, Step14, Step15, Step16, Step17]

TableResults(lst, "T481")

texto = """"""

AutoDocumentation(texto)