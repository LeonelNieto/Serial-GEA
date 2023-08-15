from Initialize import *
from ATDocumentation import AutoDocumentation
from ATErds import *
from UiTable import TableResults
from Functions import *

file_Test = Init()

Step1  = Write("C0", Erd_MabeCommunicationConfiguration, "01",     file_Test)
# Step2  = 
# Step3  = 
# Step4  = 
   
# Step5  = 
# Step6  = 
# Step7 =  
# Step8 = 
# Step9 = 
# Step10 = Read ("C0", Erd_EndOfCycleReason,               "00",     file_Test)

# Step11 = Write("C0", Erd_UI_MachineStateEnter,           "00",     file_Test)
# Step12 = Write("C0", Erd_EndOfCycleReason,               "00",     file_Test)
# Step13 = Write("C0", Erd_CriticalFault,                  "00",     file_Test)
# Step14 = Write("C0", Erd_OredShutDownUIFaults,           "00",     file_Test)
# Step15 = Write("C0", Erd_EndOfCycleReason,               "01",     file_Test)
# Step16 = Write("C0", Erd_UI_MachineStateEnter,           "20",     file_Test)
# Step17 = Read ("C0", Erd_EndOfCycleReason,               "02",     file_Test)

# ResetUnit()

# lst = [HEADERS, Step1, Step2, Step3, Step4, Step5, Step6, Step7, Step8, Step9, Step10, 
#     Step11, Step12, Step13, Step14, Step15, Step16, Step17]

# TableResults(lst, "T427")

texto = """"""

AutoDocumentation(texto)